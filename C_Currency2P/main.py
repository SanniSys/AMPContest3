from math import inf, log, exp
from collections import namedtuple
import sys
# Idee: kürzeste Wege mit negaativen Kanten = Belman ford


def bellman_ford(s):
    dist[s] = 0
    for _ in range(n - 1):
        changed = False
        for e in edges:
            if dist[e.i] + e.w < dist[e.j]:
                dist[e.j] = dist[e.i] + e.w
                pred[e.j] = e.i
                changed = True
        if not changed:
            break # Vorzeitiger Abbruch wenn es keine Änderungen an den Kanten gibt


def has_negative_cycle():
    # check if "Jackpot"
    # Detects negative cycles: if any distance can still be improved after n–1 iterations,
    # there must be a negative-weight cycle (⇒ profitable arbitrage ⇒ Jackpot).
    for e in edges:
        if dist[e.i] + e.w < dist[e.j]:
            return True
    return False

Edge = namedtuple("Edge", ["i", "j", "w"])
input = sys.stdin.readline
t = int(input())
for case in range(1, t+1):
    if case > 1:
        line = input()
    line = input()
    n, m = map(int, line.split())
    edges = []
    """
    # Konstruiere gerichteten Graphen (n Knoten, m Kanten)
    # mit Kantengewichten
    for _ in range(m):
      i, j, w = (int(st) for st in input().split())
      edges.append(Edge(i, j, w))
    """
    for _ in range(m):
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        c = float(c)
        weight = log(c)
        edges.append(Edge(a, b, weight))

    dist = [inf] * (n + 1)
    pred = [None] * (n + 1)

    bellman_ford(1)
    if has_negative_cycle():
        result = "Jackpot"
    elif dist[n] == inf:
        result = "impossible"
    else:
        # exp(sum(log(ci))) = product(ci)
        result = "{:.6f}".format(exp(dist[n])) # credits to stackoverflow

    print(f"Case #{case}: {result}")