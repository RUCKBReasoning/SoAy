from collections import deque
import jsonlines
from collections import defaultdict

def information_collection(source):
    info_dict_list = []
    if source == 'input':
        while(True):
            Function_name = input('function name: (e for ending, s for skip)\n')
            if Function_name == 'e':
                break
            elif Function_name == 's':
                continue
            else:
                parameters_list = []
                while(True):
                    p_name = input('parameter name: (e for ending, s for skip)\n')
                    if p_name == 'e':
                        break
                    elif p_name == 's':
                        continue
                    else:
                        parameters_list.append(p_name)
                return_list = []
                while(True):
                    r_name = input('return info name: (e for ending, s for skip)\n')
                    if r_name == 'e':
                        break
                    elif r_name == 's':
                        continue
                    else:
                        return_list.append(r_name)
                info_dict_list.append({'function_name' : Function_name, 'parameters' : parameters_list, 'returns' : return_list})
        # print('info_dict_list: {}'.format(info_dict_list))

    elif source == 'file':
        file_name = 'config/function_config.jsonl'
        with jsonlines.open(file_name, 'r') as f:
            for line in f:
                info_dict_list.append(line)
        # print('info_dict_list: {}'.format(info_dict_list))
        
    return info_dict_list

def build_graph(info_dict_list):
    graph = defaultdict(list)
    # Populate the graph
    for func in info_dict_list:
        for other_func in info_dict_list:
            # if func['function_name'] != other_func['function_name']:
                # Check if any return value of func is a parameter of other_func
            if any(ret_val in other_func['parameters'] for ret_val in func['return']):
                graph[func['function_name']].append(other_func['function_name'])
    return graph

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
    info_dict_list = information_collection(source = "file")
    # print('info_dict_list: {}'.format(info_dict_list))
    graph = dict(build_graph(info_dict_list=info_dict_list))
    # print(graph)

    # # 示例图（使用字典表示）图中的键是节点，值是与每个节点直接连接的节点列表
    # example_graph = {
    #     '1': ['3', '4', '5', '6', '7'],
    #     '2': ['5'],
    #     '3': ['1', '3', '4'],
    #     '4': [],
    #     '5': ['1', '4', '6'],
    #     '6': [],
    #     '7': ['5']
    # }

    # # 给定起始节点
    start_node_list = ['searchPerson', 'searchPublication']
    # 给定跳数
    max_hops = 3

    for start_node in start_node_list:
        sampled_paths = sample_paths(graph, start_node, max_hops)
        # 打印结果
        # print(f"所有{max_hops}跳以内的路径：")
        for path in sampled_paths:
            print(' -> '.join(path))
    