import random

from ..constants import MEMBERS

#  =================================================
#           UPDATE GROUPINGS WITH NEW GROUPINGS
#  =================================================

def find_excluded_member(existing_groups):
    def get_previously_excluded_members(existing_groups):
        excluded_members = set()
        for pairing in existing_groups:
            excluded_member = pairing['excluded']
            if excluded_member is None:
                continue
            excluded_members.update(excluded_member)
        return excluded_members

    excluded_member = None
    if len(MEMBERS) % 2 == 0:
        return excluded_member
    while excluded_member is None or excluded_member in get_previously_excluded_members(existing_groups):
        excluded_member = random.choice(MEMBERS)
    return excluded_member

def generate_new_groups(graph, existing_groups, n=2):
    groups = list()
    members = list(graph.keys())
    if len(members) % n == 1:
        excluded_member = find_excluded_member(existing_groups)
        groups.append([excluded_member])
        members.remove(excluded_member)

    while len(members) > n:
        group_size = 0
        group = list()

        member = None
        while group_size < n:
            if group_size == 0:
                member = random.choice(members)
            else:
                # possibly inefficient as graph size grows
                possible_partners = list(set(members) & set(graph[member]))
                partner = random.choice(possible_partners)

                # update graph
                graph[member].remove(partner)
                graph[partner].remove(member)
                member = partner

            members.remove(member)
            group.append(member)
            group_size += 1
    
        groups.append(group)
    
    if len(members) > 0:
        groups.append(members)

    return groups, graph
