from functions import auto_Aminer
import jsonlines
import time
import argparse

parser = argparse.ArgumentParser(description='SoAy Main')

parser.add_argument('--mode', type = str, choices = ['experiment', 'inference'], default = 'inference', help = 'Choose the system\'s operating mode, you can select either \'inference\' or \'experiment\'')
parser.add_argument('--gpt_version', type = str, default='gpt-4', help = 'the same as the version string of OpenAI GPT series')
parser.add_argument('--openai_key', type = str, help = 'openai key from https://www.openai.com/')

def experiment():
    for i in range(0, 18):
        with open('soayBench/v1aminer/queries_en/scholar_00{}.txt'.format(i), 'r') as query_file:
            with jsonlines.open('experiments/soaybench_experiments/soay_implementation/results_soay_4/00{}.jsonl'.format(i), 'w') as result_file:
                queries = query_file.read()
                query_list = queries.split('\n')
                for each in query_list:
                    start_time = time.time()
                    print('query: {}'.format(each))
                    route = system.parse_route(query=each)
                    print('rout e: {}'.format(route))
                    result = system.execute_wo_web(original_query=each, route = route)
                    end_time = time.time()
                    exe_time = end_time - start_time
                    doc = {'route' : route, 'result' : result, 'exe_time' : exe_time}
                    result_file.write(doc)
                    # result_file.write('{}\t{}\n'.format(route, result))
                    print('result: {}'.format(result))
                result_file.close()
            query_file.close()

def inference():
    query = input('query : ')
    start_time = time.time()
    route = system.parse_route(query = query)
    print('route:', route)
    process = system.route2process(original_query = query, route = route)
    print('Process Code:\n{}\n'.format(process))
    result = system.process2result(original_query=query, process=process)
    end_time = time.time()
    exe_time = end_time - start_time
    print('Result: ', result, '\nexe_time: ', exe_time)
    answer = system.result2nl(original_query=query, aminer_result=result)
    print('nl Answer: {}'.format(answer))
    # print('route: {}\nprocess: {}\nexe_time: {}\n'.format(route, process, exe_time))

if __name__ == '__main__':
    args = parser.parse_args()
    system = auto_Aminer(version='1101', gpt_version = args.gpt_version, openai_key = args.openai_key)
    if args.mode == 'experiment':
        experiment()
    elif args.mode == 'inference':
        inference()