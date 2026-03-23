def calculate_marriages(n, edges):
    """
    Функція суто для розрахунків. 
    Приймає кількість пар і список ребер. Повертає результат.
    """
    graph = {}
    nodes = set()
    
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
            
        graph[u].append(v)
        graph[v].append(u)
        
        nodes.add(u)
        nodes.add(v)
        
    visited = set()
    tribes = []
    total_girls = 0
    
    for node in nodes:
        if node not in visited:
            boys_count = 0
            girls_count = 0
            
            stack = [node]
            visited.add(node)
            
            while stack:
                curr = stack.pop()
                
                if curr % 2 != 0:
                    boys_count += 1
                else:
                    girls_count += 1
                    
                for neighbor in graph.get(curr, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            
            tribes.append({'boys': boys_count, 'girls': girls_count})
            total_girls += girls_count
            
    valid_pairs = 0
    for tribe in tribes:
        valid_pairs += tribe['boys'] * (total_girls - tribe['girls'])
        
    return valid_pairs

def main():
    """
    Функція для ручного запуску. Зчитує дані з консолі.
    """
    n = int(input())
    edges = []
    for _ in range(n):
        u, v = map(int, input().split())
        edges.append((u, v))

    result = calculate_marriages(n, edges)
    print(result)

if __name__ == '__main__':
    main()