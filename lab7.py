import csv

def find_parent(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_sets(parent, rank, node1, node2):
    root1 = find_parent(parent, node1)
    root2 = find_parent(parent, node2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1
        return True
    return False

def get_minimum_cable_length(filename):
    edges = []
    nodes = set()

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(',')
                if len(parts) == 3:
                    node1 = parts[0].strip()
                    node2 = parts[1].strip()
                    distance = int(parts[2].strip())
                    
                    edges.append((distance, node1, node2))
                    nodes.add(node1)
                    nodes.add(node2)
    except FileNotFoundError:
        return -1

    if not nodes:
        return 0

    edges.sort()

    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}

    min_cable_length = 0
    edges_used = 0

    for distance, node1, node2 in edges:
        if union_sets(parent, rank, node1, node2):
            min_cable_length += distance
            edges_used += 1

    if edges_used == len(nodes) - 1:
        return min_cable_length
    else:
        return -1

if __name__ == "__main__":
    file_name = "communication_wells.txt"
    result = get_minimum_cable_length(file_name)
    print(result)