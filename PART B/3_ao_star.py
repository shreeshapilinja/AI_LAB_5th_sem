from heapq import heappush, heappop

def ao_star(start, goal, neighbors, heuristic):
  # Initialize the open set and the closed set
  open_set = [(heuristic(start, goal), start)]
  closed_set = set()

  # Initialize the g-score (the cost to get from the start to a given node) and the f-score (the estimated total cost to get from the start to the goal through a given node)
  g_score = {start: 0}
  f_score = {start: heuristic(start, goal)}

  # Initialize the came_from dictionary, which will be used to reconstruct the path from the start to the goal
  came_from = {}

  # While there are nodes in the open set
  while open_set:
    # Find the node in the open set with the lowest f-score
    current = heappop(open_set)[1]

    # If the current node is the goal, we have found the path
    if current == goal:
      return reconstruct_path(came_from, current)

    # Add the current node to the closed set
    closed_set.add(current)

    # Consider each of the current node's neighbors
    for neighbor in neighbors(current):
      # If the neighbor is already in the closed set, skip it
      if neighbor in closed_set:
        continue

      # Calculate the tentative g-score for the neighbor (the cost to get from the start to the neighbor)
      tentative_g_score = g_score[current] + 1

      # If the neighbor is not in the open set, or if the new g-score is lower than the existing g-score, update the g-score and f-score of the neighbor and add it to the open set
      if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
        came_from[neighbor] = current
        g_score[neighbor] = tentative_g_score
        f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
        heappush(open_set, (f_score[neighbor], neighbor))

  # If we get here, it means that we have not found a path from the start to the goal
  return None

def reconstruct_path(came_from, current):
  # Base case: we are at the start
  if current in came_from:
    return reconstruct_path(came_from, came_from[current]) + [current]
  else:
    return [current]
# Define the graph as a dictionary of node: neighbor_list pairs
graph = {
  'A': ['B', 'C', 'D'],
  'B': ['A', 'E', 'F'],
  'C': ['A', 'G', 'H'],
  'D': ['A', 'I', 'J'],
  'E': ['B'],
  'F': ['B'],
  'G': ['C'],
  'H': ['C'],
  'I': ['D'],
  'J': ['D']
}

# Define a function to return the neighbors of a given node
def get_neighbors(node):
  return graph[node]

# Define a heuristic function that estimates the cost to get from one node to another
# In this example, we use the Manhattan distance as the heuristic

def manhattan_distance(node1, node2):
  # Check that both node1 and node2 have at least two characters
  if len(node1) < 2 or len(node2) < 2:
    return 0

  # Calculate the x and y distance between the two nodes
  x_distance = abs(ord(node1[0]) - ord(node2[0]))
  y_distance = abs(int(node1[1]) - int(node2[1]))

  # Return the sum of the x and y distances
  return x_distance + y_distance

""""
#OR 


def manhattan_distance(node1, node2):
  try:
    # Calculate the x and y distance between the two nodes
    x_distance = abs(ord(node1[0]) - ord(node2[0]))
    y_distance = abs(int(node1[1]) - int(node2[1]))

    # Return the sum of the x and y distances
    return x_distance + y_distance
  except IndexError:
    # If an index error occurs, return 0
    return 0

"""


# Find the shortest path from node 'A' to node 'H' using the AO* algorithm
path = ao_star('A', 'H', get_neighbors, manhattan_distance)

# Print the path
print(path)
