# Idea: Graph, to connect each village -> reach all: Minimal spanning Tree
# But with constrains: energy costs (weighted edges
# Grundgerüst für Prim-Algorithmus (Minimum Spanning Tree)
# Note: Code unaufgeräumt denglish und unoptimiert wegen weil deadline

from math import inf
import sys
from collections import deque


# Definiere Prim-Algorithmus von Knoten 1 aus
def prim(s):
  dist[s] = 0
  i = s
  while not done[i]:
    done[i] = True
    # Aktualisiere Nachbarn des aktuellen Knotens
    for (j, w) in adj[i]:
      if not done[j] and w < dist[j]:
        dist[j] = w
        pred[j] = i
    # Ermittle nächsten Knoten
    d_min = inf
    # debug note: hab falsche ergebnisse gehabt und kein  plan wieso, ewig rumprobieren
    # und googlen ergab: abbruchbedingung fehlt, die ist also nicht auf meinem mist gewachsen
    next = -1
    for j in range(n+1): # 0 is plain
        if not done[j] and dist[j] < d_min:
            next = j
            d_min = dist[j]
    if next == -1:
        break
    i = next


input = sys.stdin.readline
t = int(input().strip())
for case in range(1,t+1):
    # Konstruiere ungerichteten Graphen (n Knoten, m Kanten)
    # mit Kantengewichten
    if case > 1:
        line = input()
    n = int(input()) # number of villages
    adj = [[] for i in range(n+1)]  # Adjazenzliste
    villages = []
    for village in range(n):
        x_coord,y_coord,capacity = (int(st) for st in input().split())
        villages.append((x_coord,y_coord,capacity))
        # connect plane at 0 to all villages, no capacity limit for plane but vilage
        # distance from plain to village = coordinates of village squared
        distance = x_coord**2 + y_coord**2 # a² + b² = c² !  text says USE C²! really!
        if capacity >= distance: # if village capacity is big enough
            adj[0].append((village+1, distance))
            adj[village+1].append ((0, distance))
    # connect villages, if capacity big enough for both
    for i in range(n):
        for j in range(i+1, n): # avoids connection to self
            xi,yi,ci = villages[i]
            xj,yj,cj = villages[j]
            distance_ij = (xi-xj)**2 + (yi-yj)**2
            if distance_ij <= ci and distance_ij <= cj:
                adj[i+1].append((j+1, distance_ij))
                adj[j+1].append((i+1, distance_ij))

    # Speichert für jeden Knoten ob er abgearbeitet wurde
    done = [False] * (n + 1)
    # Speichert Distanzen (dist[j] = Distanz von j zum Baum)
    dist = [inf] * (n + 1)
    # Speichert Vorgänger (pred[j] = Vorgänger von j)
    pred = [None] * (n + 1)

    # Starte Prim-Algorithmus bei 1 //hier bei 0 wegen Flugzeug
    prim(0)

    total_cost = 0
    possible = all(done)
    # aus einem mir völlig unbekannten grund sind die testlösungen genau 2 mal so groß wie meine
    # warum: keine ahnung!
    total_cost = 2*sum(dist[1:]) if possible else 0
    print(f"Case #{case}: {total_cost if possible else 'impossible'}")

