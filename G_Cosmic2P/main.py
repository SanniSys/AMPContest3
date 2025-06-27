from collections import deque
from math import gcd
import sys
input = sys.stdin.readline

# read input
num_planets, num_light_trains, num_wormholes = map(int, input().split())
wormhole_nodes = set(map(int, input().split()))

adjacency_list = [[] for _ in range(num_planets + 1)]
for _ in range(num_light_trains):
    planet_a, planet_b = map(int, input().split())
    adjacency_list[planet_a].append(planet_b)
    adjacency_list[planet_b].append(planet_a)


def bfs(source):
    distance = [-1] * (num_planets + 1)
    distance[source] = 0
    queue = deque([source])
    while queue:
        current_planet = queue.popleft()
        for neighbour in adjacency_list[current_planet]:
            if distance[neighbour] == -1:
                distance[neighbour] = distance[current_planet] + 1
                queue.append(neighbour)
    return distance


distance_from_start = bfs(1)
distance_to_goal = bfs(num_planets)

# this should never happen
if distance_from_start[num_planets] == -1:
    print("impossible")
    sys.exit()

total_goal_distance = sum(distance_to_goal[w] for w in wormhole_nodes)

optimal_numerator = distance_from_start[num_planets]
optimal_denominator = 1

for wormhole_start in wormhole_nodes:
    candidate_numerator = (
        distance_from_start[wormhole_start] * (num_wormholes - 1)
        + total_goal_distance
        - distance_to_goal[wormhole_start]
    )
    candidate_denominator = (num_wormholes - 1)
    if candidate_numerator * optimal_denominator < optimal_numerator * candidate_denominator:
        optimal_numerator, optimal_denominator = candidate_numerator, candidate_denominator

gcd_value = gcd(optimal_numerator, optimal_denominator)
print(f"{optimal_numerator // gcd_value}/{optimal_denominator // gcd_value}")
