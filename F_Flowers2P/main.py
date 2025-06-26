from collections import deque, defaultdict
import sys
input = sys.stdin.readline


def shortest_trails(start, end, trails):
    """
    Calculates the shortest trails from start to end and returns
    the length of the shortest trail and how many shortest trails there are.
    """
    queue = deque([start])
    distances = {start: 0}
    trails_count = defaultdict(int)
    trails_count[start] = 1

    while queue:
        current = queue.popleft()

        for neighbour, length in trails[current]:
            new_distance = distances[current] + length
            if neighbour not in distances or new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                trails_count[neighbour] = trails_count[current]
                queue.append(neighbour)

            elif new_distance == distances[neighbour]:
                trails_count[neighbour] += trails_count[current]

    return distances.get(end), trails_count.get(end)


num_cases = int(input())
for case in range(num_cases):
    line = input().strip()
    if not line:
        line = input().strip()

    num_points_of_interest, num_trails = map(int, line.split())

    trails = [[] for _ in range(num_points_of_interest)]
    for _ in range(num_trails):
        point_a, point_b, length = map(int, input().split())
        trails[point_a].append((point_b, length))
    shortest_trail_length, shortest_trail_count = shortest_trails(
        0, num_points_of_interest - 1, trails)

    result = shortest_trail_length * shortest_trail_count * 2
    print(f"Case #{case + 1}: {result}")
