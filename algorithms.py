from collections import deque
import heapq

def bfs_shortest_path(city_graph, start, destination):
    queue = deque([[start]])
    visited = set()
    print(f"Running BFS: Start={start}, Destination={destination}")
    while queue:
        path = queue.popleft()

        current_intersection = path[-1]

        if current_intersection == destination:
            return path

        if current_intersection not in visited:
            visited.add(current_intersection)

            #add all neighbors to the queue as a new path
            for neighbor in city_graph.get(current_intersection,[]):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

def dfs_maze_solver(maze_graph, start, destination, path=None, visited=None):
    #initialize the path and visited set
    if path is None:
        path = [start] #defiinge start note
    if visited is None:
        visited = set() #use a set to store visiting nodes

    visited.add(start)

    if start == destination:
        return path
    #explore neighboring nodes of the current node
    for neighbor in maze_graph.get(start,[]):
        if neighbor not in visited:
            result_path = dfs_maze_solver(maze_graph, neighbor,destination, path + [neighbor], visited)

            if result_path:
                return result_path

    #no path return none
    return None

def dijkstra(graph, source, destination):
    #initialize distances to infinity and set source distance

    #distances = {node: float('inf') for node in graph}
    distances = {node: float('inf') for node in graph.nodes()}

    distances[source]=0
    #priority queue to store distance and node information
    priority_queue = [(0, source)]
    #dictionary to keep track of shortest path

    #previous_nodes = {node: None for node in graph}
    previous_nodes = {node: None for node in graph.nodes()}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node == destination:
            break
        #if current distance is already higher than the recorded one, then  skip it
        if current_distance > distances[current_node]:
            continue

       # for neighbor, weight in graph[current_node].items():
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']

            #calc new distance to the neighbor
            distance = current_distance + weight

            #if new distance is shorter update the distance and path
            if distance < distances[neighbor]:
                distances[neighbor]= distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous_nodes[current]

    path.reverse()#reverse the path to start from the source node

    #returning the shortest distance and path
    return distances[destination],path