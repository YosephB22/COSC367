network = {
    'A': {
        'Parents': ["C"],
        'CPT': {
            (True,): 0.1,
            (False,): 0.4
            }},
    'B': {
        'Parents': ["A", "D"],
        'CPT': {
            (True, True): 0.1,
            (True, False): 0.2,
            (False, True): 0.4,
            (False, False): 0.3
            }},
            
    'C': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
    'D': {
        'Parents': [],
        'CPT': {
            (False,): 0.1
            }},
}
from numbers import Number
assert type(network) is dict
for node_name, node_info in network.items():
    assert type(node_name) is str
    assert type(node_info) is dict
    assert set(node_info.keys()) == {'Parents', 'CPT'}
    assert type(node_info['Parents']) is list
    assert all(type(s) is str for s in node_info['Parents'])
    for assignment, prob in node_info['CPT'].items():
        assert type(assignment) is tuple
        assert isinstance(prob, Number)

print("OK")