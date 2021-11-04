from itertools import product
def joint_prob(network, assignment):
    p = 1 # p will enentually hold the value we are interested in
    for variable, assign, in assignment.items():
        value = network[variable]
        result_parent = []
        for parent in value['Parents']:
            result_parent.append(assignment[parent])
        tuple_result_parent = tuple(result_parent)
        cpt = network[variable]["CPT"][tuple_result_parent]
        if assignment[variable] == True:
            cpt = network[variable]["CPT"][tuple_result_parent]
            p *= cpt
        else:
            p *= (1 - cpt)

    return p

def query(network, query_var, evidence):
    
    # If you wish you can follow this template
    
    # Find the hidden variables
    # Initialise a raw distribution to [0, 0]
    assignment = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        probability_sum = 0
        # Update the assignment to include the query variable
        hidden_vars = network.keys() - evidence.keys() - {query_var}
        for values in product((True, False), repeat=len(hidden_vars)):
            # the hidden assignment only contains the possible assignment of the hidden assignment 
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            # here we add the the query assignment to the hidden assignment
            hidden_assignments.update({query_var: query_value})
            hidden_assignments.update(evidence)
            # now we can add up all the value of one possible assignment for the query variable
            probability_sum += joint_prob(network, hidden_assignments)
        assignment[query_value] = probability_sum
    # we add up all the assignment values and use that value to normalize it.
    result = 0
    for value in assignment.values():
        if value not in [True, False]:
            result += value
    # narmalization
    for var, val in assignment.items():
        assignment[var] = val / result
    return assignment


network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.8,
            }},
    }
 
answer = query(network, "A", {})
print("P(B=true) = {:.5f}".format(answer[True]))
print("P(B=false) = {:.5f}".format(answer[False]))