import re

import networkx as nx

print(",".join(sorted(sorted(nx.find_cliques(nx.Graph(re.findall(r"(\w+)-(\w+)", open("input.txt").read()))), key=len)[-1])))  # noqa: SIM115
