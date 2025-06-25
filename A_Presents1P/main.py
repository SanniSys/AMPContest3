import sys
from collections import deque

# Kanten auf s-t-Pfad rekonstruieren (parent[i] =
# Index des Vorgängers von Knoten i auf dem Pfad)
def getPath(t, parent):
  edges = []
  i = t
  while parent[i] != -1:
    edges.append((parent[i], i))
    i = parent[i]
  return edges

def bfs(s, t, n):
  done = False
  visited = [False]*(n+1)
  parent = [-1]*(n+1)
  visited[s] = True
  queue = deque([s])
  while queue and not done:
    i = queue.popleft()
    for j in adj[i]:
      if not visited[j] and cap[i][j] > flow[i][j]:
        visited[j] = True
        parent[j] = i
        # Vorzeitiger Abbruch sobald t gefunden
        if j == t:
          done = True
          break
        else:
          queue.append(j)
  # Pfad zurückgeben (leerer Pfad falls t nicht erreicht)
  return getPath(t, parent)


def parse_preferences(pref_string):
    """Parse preference string like '1,10,3,5-8' into list of presents"""
    if not pref_string.strip():
        return []

    presents = []
    parts = pref_string.split(',')

    for part in parts:
        part = part.strip()
        if '-' in part: # Handle ranges
            start, end = map(int, part.split('-'))
            presents.extend(range(start, end + 1))
        else:
            # Handle single number
            presents.append(int(part))

    return presents

input = sys.stdin.readline
t = int(input())
for case in range(1, t + 1):
    if case > 1:
        input()
    n, m = (int(st) for st in input().split())
    # Graphen aufbauen, adjazenzliste, kapazitätenliste und flowmatrix
    # Quelle = 0, Geschenke = 1..m, Freunde = m+1..m+n, Senke = m+n+1 (jah Haskell verseuchte 2 Punkte! Nein 3 sind mir zu viel!)
    N = m + n + 2 # Größe des Netzwerks
    source = 0
    sink = m + n + 1
    adj = [[] for _ in range(N)]
    cap = [[0] * N for _ in range(N)]
    flow = [[0] * N for _ in range(N)]
    # Quelle mit Geschenken verbinden, Kapazität 1
    for g in range(1, m + 1):
        adj[source].append(g)
        adj[g].append(source)
        cap[source][g] = 1
    #Freunde mit Senke verbinden, Kapazität 1
    for f in range(m + 1, m + n + 1):
        adj[f].append(sink)
        adj[sink].append(f)
        cap[f][sink] = 1
    #Geschenk mit Freund verbinden, falls gemocht
    for i in range(n):
        prefs = parse_preferences(input())
        friend_node = m + 1 + i
        for gift in prefs:
            if 1 <= gift <= m:
                adj[gift].append(friend_node)
                adj[friend_node].append(gift)
                cap[gift][friend_node] = 1
    #Edmond-Karp
    s, t = source, sink  # Quelle und Senke festlegen
    while True:
        # Berechne augmentierenden s-t-Pfad im Residualgraphen
        edges = bfs(s, t, N-1)
        if not edges:
            break
        # Berechne min. Residualkapazität einer Kante auf dem Pfad
        df = min(cap[i][j] - flow[i][j] for (i, j) in edges)
        # Erhöhe Fluss entlang des Pfades
        for (i, j) in edges:
            flow[i][j] += df
            flow[j][i] -= df

    # Berechne Gesamtfluss in die Senke
    fmax = sum(flow[i][t] for i in range(N))
    # Perfect matching wenn fmax = freundeanzahl
    result = "yes" if fmax == n else "no"
    print(f"Case #{case}: {result}")

