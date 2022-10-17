#This was taken from https://www.geeksforgeeks.org/shortest-path-unweighted-graph/
#Modified only slightly to work with a dict of string->int instead of int->int

def BFS(adj, src, dest, v, pred, dist):
    # a queue to maintain queue of vertices whose
    # adjacency list is to be scanned as per normal
    # DFS algorithm
    queue = []

    # boolean array visited[] which stores the
    # information whether ith vertex is reached
    # at least once in the Breadth first search
    visited = {}
    for x in adj.keys():
        visited[x] = False

    # initially all vertices are unvisited
    # so v[i] for all i is false
    # and as no path is yet constructed
    # dist[i] for all i set to infinity
    for x in adj.keys():
        dist[x] = 1000000
        pred[x] = -1

    # now source is first to be visited and
    # distance from source to itself should be 0
    visited[src] = True
    dist[src] = 0
    queue.append(src)

    # standard BFS algorithm
    while (len(queue) != 0):
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):

            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])

                # We stop BFS when we find
                # destination.
                if (adj[u][i] == dest):
                    return True

    return False


def printShortestDistance(adj, s, dest, v):
    # predecessor[i] array stores predecessor of
    # i and distance array stores distance of i
    # from s
    pred = {}
    dist = {}
    for x in adj.keys():
        pred[x] = ""
        dist[x] = 0

    if (BFS(adj, s, dest, v, pred, dist) == False):
        print("Given source and destination are not connected")

    # vector path stores the shortest path
    path = []
    crawl = dest
    path.append(crawl)

    while (pred[crawl] != -1):
        path.append(pred[crawl])
        crawl = pred[crawl]

    # distance from source is in distance array
    print("Shortest path length is : " + str(dist[dest]), end='')

    # printing path from source to destination
    print("\nPath is")

    for i in range(len(path) - 1, -1, -1):
        print(path[i], end=' ')

