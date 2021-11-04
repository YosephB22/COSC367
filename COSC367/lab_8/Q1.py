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
            (False,): 0.7,
            }},
    }
 
p = joint_prob(network, {'A': False, 'B':True})
print("{:.5f}".format(p)) 