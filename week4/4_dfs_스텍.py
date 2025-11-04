"""
Q. 인접 리스트가 주어질 때, 모든 노드를 DFS 순서대로 방문하시오. 
"""
# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
stack= [] # [], [2,5,9], [2,5], [2,5,10], [2,5], [2], [2,6,8], [2,6], [2], [2,7], [2], [], [3], [], [4], [],
visited = [] # 1, 9, 10, 5, 8, 6, 7, 2, 3, 4
def dfs_stack(adjacent_graph, start_node):
    visited.append(start_node)
    candidate_list = adjacent_graph.get(start_node, None)
    for candidate in candidate_list:
        if candidate in visited:
            continue
        stack.append(candidate)
    if len(stack) == 0:
        return visited
    next_node = stack.pop()
    # print(f"현재스텍: {stack}")
    # print(f"다음노드: {next_node}")
    # print(f"visited: {visited}")
    dfs_stack(adjacent_graph, next_node)
    return visited

print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!