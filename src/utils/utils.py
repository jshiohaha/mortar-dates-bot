import itertools

def format_groupings_to_readable_format(groupings, excluded_member):
    response = "Mortar Dates 🤟🏼\n\n"
    for idx in range(len(groupings)):
        group = groupings[idx]
        response += "{}: {} & {}\n".format((idx+1), group[0], group[1])
    response += ("\n{} was left out this week 🙁 Join another date or "
    "wait until next week.").format(excluded_member)
    return response

#  ===================================
#            GRAPH UTILS
#  ===================================

def build_empty_graph(items):
    graph = dict()
    for item in items:
        graph[item] = list()
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