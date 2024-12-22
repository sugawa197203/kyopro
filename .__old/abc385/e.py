from collections import defaultdict, deque, Counter

def solve(N, edges):
    # グラフの構築
    graph = defaultdict(list)
    degree = [0] * (N + 1)  # 出次数

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1

    # BFS を実装
    def bfs(start):
        visited = [-1] * (N + 1)
        queue = deque([start])
        visited[start] = 0
        farthest_node = start
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = visited[node] + 1
                    queue.append(neighbor)
                    farthest_node = neighbor
        return farthest_node, visited

    # BFS 1: 適当な点から最遠点を求める
    farthest_node1, _ = bfs(1)
    # BFS 2: 最遠点からもう一度 BFS を行い、全体の最遠距離を求める
    farthest_node2, distances_from_u = bfs(farthest_node1)
    _, distances_from_v = bfs(farthest_node2)

    # 結果を計算
    results = []
    for i in range(1, N + 1):
        # 各頂点での最遠距離は 2 回の BFS から最大値を取得
        max_distance = max(distances_from_u[i], distances_from_v[i])
        results.append((max_distance, degree[i]))

    return results

# 入力例
N = int(input())
edge = []
for _ in range(N - 1):
	a, b = map(int, input().split())
	edge.append((a, b))
result = solve(N, edge)

distanceCount = Counter([x[0] for x in result])
print(distanceCount)
if 1 == min(distanceCount, key=distanceCount.get):
    print(0)
    exit()
    
for i, (distance, degree) in enumerate(result, start=1):
    print(f"頂点 {i}: 最遠距離 = {distance}, 出次数 = {degree}")
