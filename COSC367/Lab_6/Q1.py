from csp import *
import itertools

def generate_and_test(csp):
    result = []
    constraint = csp.constraints
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {n: values[index] for index, n in enumerate(names)}
        all_constraint = [(satisfies(assignment, c)) for c in constraint]
        if all(all_constraint):
            result.append(assignment)
    return result

csp = CSP(
   var_domains = {var:{-1,0,1} for var in 'bc'},
   constraints = {
      lambda a, b: a * b > 0,
      lambda b, c: b + c > 0,
      }
    )
solutions = generate_and_test(csp)
for s in solutions:
    print(s.values())