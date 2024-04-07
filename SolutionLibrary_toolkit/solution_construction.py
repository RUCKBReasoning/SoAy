from collections import deque
import jsonlines
from collections import defaultdict
from pyvis.network import Network
import itertools

class solution_toolkit():
    def __init__(self, domain) -> None:
        self.domain = domain
        self.n = 3 # road sampling hop maximum

    def collectInformation(self, config_file_path):
        info_dict_list = []
        file_name = config_file_path
        with jsonlines.open(file_name, 'r') as f:
            for line in f:
                info_dict_list.append(line)
        # print('info_dict_list: {}'.format(info_dict_list))
        
        return info_dict_list

    def buildGraph(self, info_dict_list):
        graph = defaultdict(list)
        # Populate the graph
        for func in info_dict_list:
            for other_func in info_dict_list:
                # if func['function_name'] != other_func['function_name']:
                    # Check if any return value of func is a parameter of other_func
                if any(ret_val in other_func['parameters'] for ret_val in func['return']):
                    graph[func['function_name']].append(other_func['function_name'])
        return graph

    def samplePaths(self, graph, start):
        n = self.n
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

    def sampleIO(self, path, info_dict_list):
        head_api = path[0]
        tail_api = path[-1]
        print
        for each in info_dict_list:
            if each['function_name'] == head_api:
                head_input = each['parameters']
            if each['function_name'] == tail_api:
                tail_output = each['return']
        input_c = []
        output_c = []

        for i in range(len(head_input)):
            for each in list(itertools.combinations(head_input, i)):
                input_c.append(each)

        # #output笛卡尔积版本
        # for i in range(len(tail_output)):
        #     for each in list(itertools.combinations(tail_output, i)):
        #         output_c.append(each)

        #output线性枚举版本  
        for each in tail_output:
            output_c.append(each)

        combination_list = []

        print("path: {}, input_c: {}\n, output_c: {}".format(path, head_input, output_c))
        for input in input_c:
            for output in output_c:
                if input != () and output != ():
                    combination_list.append({'intput' : input, 'output' : output})
        return combination_list

    def showGraph(self, graph):
    # 字典形式的单向边
        edges = graph

        nt = Network("500px", "1000px")
        # 获取所有独特的节点
        all_nodes = set()
        for node, neighbors in edges.items():
            all_nodes.add(node)
            all_nodes.update(neighbors)
        # 添加所有节点
        for node in all_nodes:
            nt.add_node(node)
        # 再添加边
        for node, neighbors in edges.items():
            for neighbor in neighbors:
                nt.add_edge(node, neighbor)
        # 保存图形到本地HTML文件
        nt.save_graph("./results/{}/graph.html".format(self.domain))

    def sampleCombination(self, paths):
        combination_library = []
        for path in paths:
            print(' -> '.join(path))
            combination_list = toolkit.sampleIO(path = path, info_dict_list=info_dict_list)
            for each in combination_list:
                combination_library.append({'path' : ' -> '.join(path), 'io_combinations' : each})
        return combination_library
        

if __name__ == '__main__':
    #Instantiate
    domain = 'OpenLibrary'
    toolkit = solution_toolkit(domain = domain)

    #Configs
    config_file_path = '../config/{}_function_config.jsonl'.format(domain)
    info_dict_list = toolkit.collectInformation(config_file_path)
    # start_node_list = ['searchPerson', 'searchPublication']
    start_node_list = ["searchBook", "searchAuthor", "searchSubject"]

    #API Graph building and saving
    graph = dict(toolkit.buildGraph(info_dict_list=info_dict_list))
    toolkit.showGraph(graph)
    print('------------------------------------------------')

    #Sulution Paths sampling & Combinations sampling
    combination_library = []
    for start_node in start_node_list:
        sampled_paths = toolkit.samplePaths(graph, start_node)
        path_combination_library = toolkit.sampleCombination(sampled_paths)
        combination_library.extend(path_combination_library)

    # Combinations Saving
    with jsonlines.open('results/{}/combinations.jsonl'.format(domain), 'w') as f:
        for each in combination_library:
            f.write(each)