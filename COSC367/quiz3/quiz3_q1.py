from itertools import product

model = []
truth_table = list(product((True, False), repeat=3))
for p, q, r in truth_table:
    if p & (not(q)):
        model.append((p, q, r))
for m in model:
    print(m)
