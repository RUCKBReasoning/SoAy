 # -*- coding: utf-8 -*-
from model import *
import datetime
import re
import jsonlines
import time
import traceback

class auto_Aminer():
    def __init__(self, version, gpt_version, openai_key):
        self.prompt_lib = []
        with jsonlines.open('prompts/prompt_json/prompt_dict_{}.json'.format(version), 'r') as f:
            for each in f:
                self.prompt_lib.append(each)
            f.close()
        self.prompt_lib = self.prompt_lib[0]
        # print(prompt_lib)
        self.route_lib = []
        for each in self.prompt_lib.keys():
            self.route_lib.append(each)

        self.openai_api = OpenAI(gpt_version = gpt_version, openai_key = openai_key)
        self.aminer_api = aminer_soay()

    def get_llm_answer(self, prompt):
        error_count = 0
        while True:
            try:
                if error_count == 3:
                    print('backbone down')
                    result = 'backbone down'
                    break

                response = self.openai_api.generate_response_chatgpt(query = prompt)
                result = response['choices'][0]['message']['content'] # chatGPT
                break
            except:
                print('parsing waiting...')
                error_count += 1
                error_info = traceback.format_exc()
                print(error_info)
                time.sleep(3)
                continue
        with jsonlines.open(('log/{}-{}.jsonl'.format(datetime.date.today().month, datetime.date.today().day)), "a") as f:
            f.write({'input' : prompt, 'response': str(response)})
            f.close() 
        return result

    def parse_route(self, query):
        parse_prompt = self.prompt_lib['parser'] + '\nQuery: ' + query + '\nSolution: '
        route = self.get_llm_answer(prompt = parse_prompt)
        return route
    
    def generate_process_from_route(self, original_query, query_prompt, route):
        pfr_prompt = query_prompt + 'Query: ' + original_query + '\n' + route + '\n--\n'
        process = self.get_llm_answer(prompt = pfr_prompt)
        return process
    
    def generate_result_from_process(self, process):
        global searchPerson 
        global searchPublication
        global getCoauthors 
        global getPersonInterest
        global getPersonPubs
        global getPersonBasicInfo
        global getPublication
        searchPerson = self.aminer_api.searchPersonComp
        searchPublication = self.aminer_api.searchPublication
        getCoauthors = self.aminer_api.getCoauthors
        getPersonInterest = self.aminer_api.getPersonInterest
        getPersonPubs = self.aminer_api.getPersonPubs
        getPersonBasicInfo = self.aminer_api.getPersonBasicInfo
        getPublication = self.aminer_api.getPublication
        # print('generated process: \n', process)   
        try: 
            # final_result = ''
            exec(process, globals())
            result = final_result
            return result
        except Exception as e:
            error_info = traceback.format_exc()
            print(error_info)
            return 'exe error'
    
    def execute_wo_web(self, original_query, route):
        try:
            process = self.generate_process_from_route(original_query, self.prompt_lib[route], route)
        except:
            process = self.generate_process_from_route(original_query, self.prompt_lib['except'], route)
        
        aminer_result = self.generate_result_from_process(process = process)
        # print('aminer_result: {}'.format(aminer_result))
        return aminer_result
    
    def route2process(self, original_query, route):
        l = list(self.prompt_lib.keys())
        try:
            process = self.generate_process_from_route(original_query, self.prompt_lib[route], route)
        except:
            process = 'parsing not available'
        return process
    
    def process2result(self, original_query, process):
        aminer_result = self.generate_result_from_process(process = process)
        return aminer_result
    
    def result2nl(self, original_query, aminer_result):
        print('query:{}, aminer_result:{}'.format(original_query, aminer_result))
        result = self.get_llm_answer(prompt=self.prompt_lib['nl'] + 'Query:\n' + original_query + '\nResult:\n' + aminer_result + '\nAnswer:\n')
        return result