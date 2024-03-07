from collections import deque

def sample_paths(graph, start, n):
    # 初始化队列和结果列表
    queue = deque([(start, [start])])  # 每个元素是一个元组，包含当前节点和到达该节点的路径
    paths = []  # 存储所有n跳以内的路径
    # BFS
    while queue:
        current_node, path = queue.popleft()
        # 检查路径长度是否超过n跳
        if len(path) > n:
            continue  # 超过n跳的路径不再添加到队列中
        # 将当前路径添加到结果列表中
        paths.append(path)
        # 将邻居节点添加到队列中
        if current_node in graph:
            for neighbor in graph[current_node]:
                queue.append((neighbor, path + [neighbor]))
    return paths

if __name__ == '__main__':
    # 示例图（使用字典表示）
    # 图中的键是节点，值是与每个节点直接连接的节点列表
    example_graph = {
        '1': ['3', '4', '5', '6', '7'],
        '2': ['5'],
        '3': ['1', '3', '4'],
        '4': [],
        '5': ['1', '4', '6'],
        '6': [],
        '7': ['5']
    }
    # 给定起始节点
    start_node_list = ['1', '2']
    # 给定跳数
    max_hops = 3

    for start_node in start_node_list:
        sampled_paths = sample_paths(example_graph, start_node, max_hops)
        # 打印结果
        # print(f"所有{max_hops}跳以内的路径：")
        for path in sampled_paths:
            print(path)