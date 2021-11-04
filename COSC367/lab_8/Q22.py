import itertools
from collections import defaultdict

def joint_prob(network, assignment):
    """doing a joint probability"""
    joint_probability = 1
    for assin in assignment:
        parent_network = network[assin]["Parents"]
        cpt_tuple = ()
        for parent in parent_network:
            cpt_tuple += (assignment[parent], )
        CPT_value = network[assin]["CPT"][cpt_tuple]
        if assignment[assin] == False:
            joint_probability *= (1 - CPT_value)
        else:
            joint_probability *= CPT_value
    return  joint_probability

def query(network, query_var, evidence):
    """solving bayesian network.
    return the P(query_var = true|evidence) and P(query_var = false|evidence)
    we will also need to normalaze it.
    """
    result = defaultdict(float)
    for query in (True, False):      
        hidden_vars = network.keys() - evidence.keys() - {query_var}
        for values in itertools.product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            hidden_assignments.update(evidence)
            hidden_assignments.update({query_var:query})
            joint_p = joint_prob(network, hidden_assignments)
            if query not in result:
                result[query] = joint_p
            else:
                result[query] += joint_p
    total_probability = sum(result.values())
    for key, value in result.items():
        result[key] = value/total_probability
    return result
network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }
 
answer = query(network, 'Burglary', {'John': True, 'Mary': True})
print("Probability of a burglary when both\n"
      "John and Mary have called: {:.3f}".format(answer[True]))  