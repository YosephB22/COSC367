from itertools import product
def csp_relation():  
    var_domains = {var:{0,1,2} for var in 'ab'}
    print(var_domains, var_domains.keys())
    rule = ("a" > "b") and ("b" > 0)
    variable = (var_domains.keys())
    assignmet = {}
    print(variable)
    for v in product(*var_domains.values()):
        possible_assignment = {key: v[index] for index, key in enumerate(var_domains.keys())}
        print(possible_assignment)
        pass


print(csp_relation())