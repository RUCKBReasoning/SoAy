 # -*- coding: utf-8 -*-
from model import *
import argparse

parser = argparse.ArgumentParser(description='SoAy Main')

parser.add_argument('--gpt_version', type = str, default='gpt-4', help = 'the same as the version string of OpenAI GPT series')
parser.add_argument('--openai_key', type = str, help = 'openai key from https://www.openai.com/')

args = parser.parse_args()
openai_api = OpenAI(gpt_version = args.gpt_version, openai_key = args.openai_key)
aminer_api = aminer_soay()

def aminer_searchPublication():
    result = aminer_api.searchPublication(publication_info = 'Performance Analysis Of Ieee 802.16 Multicast And Broadcast Polling Based Bandwidth Request')
    return result

def aminer_getPublication():
    result = aminer_api.getPublication(pub_id = '53e9b010b7602d9703a67046')
    return result

def aminer_getCoauthors():
    result = aminer_api.getCoauthors(person_id = '542cdcaddabfae216e634e60')
    return result

def aminer_searchPersonComp():
    result = aminer_api.searchPersonComp(organization = 'Northwestern Polytechnical University')
    return result

def aminer_getPersonBasicInfo():
    result = aminer_api.getPersonBasicInfo(person_id='542cdcaddabfae216e634e60')
    return result

def aminer_getPersonInterest():
    getPersonInterest = aminer_api.getPersonInterest
    result = getPersonInterest(person_id='542cdcaddabfae216e634e60')
    return result

def aminer_getPersonPubs():
    result = aminer_api.getPersonPubs(person_id='542a63f1dabfae646d55b020')
    return result

def chatgpt():
    response = openai_api.generate_response_chatgpt(query = 'hi')
    result = response['choices'][0]['message']['content']
    return result
    # print(response)
    # print()

api_list = [chatgpt, aminer_searchPersonComp, aminer_searchPublication, aminer_getPublication, aminer_getPersonBasicInfo, aminer_getPersonInterest, aminer_getPersonPubs]

for each in api_list:
    try:
        each()
        print('{} is working'.format(each.__name__))
    except:
        print('something wrong with {}, pleaes check'.format(each.__name__))