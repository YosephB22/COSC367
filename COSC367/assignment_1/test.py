


map_str = """\
+-------+
|  9  XG|
|X XXX  |
| S  0FG|
+-------+
"""

inner_l = []
upper_l = []
for m in map_str:
    if m == "\n":
        upper_l.append(inner_l)
        inner_l = []
    else:
        inner_l.append(m)
print(upper_l)
