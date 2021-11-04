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