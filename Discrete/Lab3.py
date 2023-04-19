def generate_permutations(cities):
    if len(cities) == 0:
        return []
    if len(cities) == 1:
        return [cities]
    permutations = []
    for i in range(len(cities)):
        remaining_cities = cities[:i] + cities[i+1:]
        sub_permutations = generate_permutations(remaining_cities)
        for permutation in sub_permutations:
            permutations.append([cities[i]] + permutation)
    return permutations

def calculate_distance(tour, distance_matrix):
    distance = 0
    for i in range(len(tour) - 1):
        if distance_matrix[tour[i]][tour[i+1]] == 0:
            return float('inf')
        distance += distance_matrix[tour[i]][tour[i+1]]
    if distance_matrix[tour[-1]][tour[0]] == 0:
        return float('inf')
    distance += distance_matrix[tour[-1]][tour[0]]
    return distance

with open('l3-1.txt', 'r') as f:
    distance_matrix = []
    for line in f:
        distances = [int(x) for x in line.split()]
        distance_matrix.append(distances)

num_cities = len(distance_matrix)
cities = list(range(num_cities))

shortest_distance = float('inf')
shortest_tour = None

for tour in generate_permutations(cities):
    distance = calculate_distance(tour, distance_matrix)
    if distance < shortest_distance:
        shortest_distance = distance
        shortest_tour = tour

if shortest_distance == float('inf'):
    print("No valid Hamiltonian contour")
else:
    print("Hamiltonian Contour:", shortest_tour)
