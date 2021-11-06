import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    Author: Kourosh Neshatian

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = r"\s*(?P<HEAD>{ATOM})\s*".format(**locals())
    BODY   = r"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*".format(**locals())
    CLAUSE = r"{HEAD}(:-{BODY})?\.".format(**locals())
    KB     = r"^({CLAUSE})*\s*$".format(**locals())

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")
def forward_deduce(kb):
    k_b = list(clauses(kb))
    c = set()
    found = False
    while found is False:
        is_c_changed = c.copy()
        for clause_index, (atom, body) in enumerate(k_b):
            if len(body) == 0:
                c.add(atom)
                k_b.pop(clause_index)
            else:
                subset_body = set(body)
                if subset_body.issubset(c) == True:
                    c.add(atom)
                    k_b.pop(clause_index)
        if len(is_c_changed) == len(c):
            found = True
    return c
        
kb = """
a :- h.
b :- f.  
a :- g. 
c :- d, f.
d :- k. 
e :- f.
c.
g.
"""

print(", ".join(sorted(forward_deduce(kb))))