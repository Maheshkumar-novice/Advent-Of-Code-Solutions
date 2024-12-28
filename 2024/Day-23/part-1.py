import re

import networkx as nx

print(sum((len(k) == 3 and "t" in (k[0][0], k[1][0], k[2][0])) for k in nx.enumerate_all_cliques(nx.Graph(re.findall(r"(\w+)\-(\w+)", open("input.txt").read())))))  # noqa: PLR2004, SIM115
