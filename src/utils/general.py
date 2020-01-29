import itertools


def build_empty_graph(items):
    graph = {}
    for item in items:
        graph[item] = []
    return graph


def build_graph(items, graph=None):
    if graph is None:
        graph = build_empty_graph(items)
    # constant 2 dictates combination size
    for group in list(itertools.combinations(items, 2)):
        n1, n2 = group[0], group[1]
        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph
