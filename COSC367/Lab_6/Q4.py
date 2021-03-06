import itertools, copy 
from csp import *

def arc_consistent(csp):
    to_do = {(x, c) for c in csp.constraints for x in scope(c)} # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c): # COMPLETE
                    new_domain.add(xval) # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                   for z in scope(cprime): # COMPLETE
                       if x != z: # COMPLETE
                           to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     #COMPLETE
    return csp


csp_instance = CSP(
   var_domains = {var:{1,2,3,4} for var in 'abcd'},
   constraints = {
      lambda a, b: a >= b,
      lambda a, b: b >= a,
      lambda a, b, c: c > a + b,
      lambda d: d <= d,
   }
)
arc_consistent(csp_instance)

assert type(csp_instance) is CSP
print(sorted(csp_instance.var_domains.keys()))
print(len(csp_instance.constraints))