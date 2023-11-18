 # -*- coding: utf-8 -*-
import openai
import requests
import json

class OpenAI():
    def __init__(self, gpt_version, openai_key) :
        self.gpt_version = gpt_version
        self.key = openai_key
        openai.api_key=self.key

    def generate_response_chatgpt(self, query):
        messages = [{'role':'user', 'content' : query}]
        response = openai.ChatCompletion.create(
            model=self.gpt_version, #gpt-4
            messages=messages,
            temperature=0
        )
        return response
    
def wrapUrlParameter(url, **kwargs):
    if len(kwargs):
        url+="?"
        url+='&'.join([f"{k}={v}" for k,v in kwargs.items()])
    return url

class aminer_soay:
    def __init__(self):
        self.addr = 'https://soay.aminer.cn/'
    
    def searchPersonComp(self, **kwargs):
        personList = []
        addr = self.addr + 'searchPerson'
        headers = {
            'Content-Type' : 'application/json'
        }
        searchKeyWordList = []
        if 'name' in kwargs:
            searchKeyWordList.append({
                        "operate": "0",
                        "wordType": 4,
                        "keyword": kwargs['name'],
                        "advanced": True,
                        "needTranslate": True
                    })
        if 'interest' in kwargs:
            searchKeyWordList.append({
                        "operate": "0",
                        "wordType": 2,
                        "keyword": kwargs['interest'],
                        "advanced": True,
                        "needTranslate": True
                    })
        if 'organization' in kwargs:
            searchKeyWordList.append({
                        "operate": "0",
                        "wordType": 5,
                        "keyword": kwargs['organization'],
                        "advanced": True,
                        "needTranslate": True
                    })
        json_content = json.dumps({
            "sort": [{'asc': False, 'field' : 'n_citation'}],
            "searchKeyWordList": searchKeyWordList,
            "needDetails" : True
        })
        response = requests.post(
            url=addr,
            headers = headers,
            data = json_content
        )
        result = response.json()
        for each in result['data']['hitList']:
            # print(each)
            try:
                personList.append(
                    {
                        'person_id' : each['id'],
                        'name' : each['name'],
                        'interests' : [each['interests'][i]['t'] for i in range(min(len(each['interests']), 10))],
                        # 'nation': each['nation'], 
                        'num_citation' : each['ncitation'],
                        'num_pubs': each['npubs'],
                        'organization' : each['contact']['affiliation']
                    }
                )
            except:
                continue
        return personList
    
    def searchPublication(self, publication_info):
        addr = self.addr + 'searchPublication'
        pubList = []
        headers = {
            'Content-Type' : 'application/json'
        }
        json_content = json.dumps({
            "query" : publication_info,
            'needDetails' : True,
            'page' : 0,
            'size' : 10,
            "sort": [{'asc': False, 'field' : 'n_citation'}],
        })
        response = requests.post(
            url=addr,
            headers = headers,
            data = json_content
        )
        result = response.json()
        for each in result['data']['hitList']:
            try:
                pubList.append({
                    'pub_id' : each['id'],
                    'title' : each['title'],
                    'year' : each['year']
                })
            except:
                continue

        return pubList

    def getPublication(self, pub_id):
        addr = self.addr + 'getPublication'
        addr = wrapUrlParameter(addr, id = pub_id)
        # addr = addr + '?AppCode=' + self.appcode + '&id=' + id
        response = requests.get(url = addr)
        result = response.json()['data'][0]['pub']
        info_dict = {}
        try:
            info_dict['abstract'] = result['abstract']
        except:
            info_dict['abstract'] = 'paper abstract'
        author_list = []
        for each in result['authors']:
            try:
                author_list.append({'person_id' : each['id'], 'name' : each['name']})
            except:
                continue
        if author_list != []:
            info_dict['author_list'] = author_list
        try:
            info_dict['num_citation'] = result['num_citation']
        except:
            pass
        try:
            info_dict['year'] = result['year']
        except:
            pass
        try:
            info_dict['pdf_link'] = result['pdf']
        except:
            pass
        try:
            info_dict['venue'] = result['venue']
        except:
            pass
        return info_dict
    
    def getPersonInterest(self, person_id):
        addr = self.addr + 'getPersonInterest'
        addr = wrapUrlParameter(addr, id = person_id)
        # addr = addr + '?AppCode=' + self.appcode + '&id=' + id
        response = requests.get(url = addr)
        try:
            result = response.json()['data'][0]['data']['data']['data']
        except:
            return []
        interest_list = [result[i]['t'] for i in range(len(result))]
        return interest_list

    def getCoauthors(self, person_id):
        addr = self.addr + 'getCoauthors'
        addr = wrapUrlParameter(addr, id = person_id)
        response = requests.get(url=addr)
        result = response.json()['data'][0]['data']['crs']
        coauthorsList = []
        for each in result:
            try:
                coauthorsList.append({
                    'person_id' : each['id'],
                    'name' : each['name'],
                    'relation' : each['relation']
                })
            except:
                continue
        # coauthorsList = [{'person_id' : result[i]['id'], 'relation' : result[i]['relation']} for i in range(min(len(result), 10))]
        return coauthorsList
    
    def getPersonPubs(self, person_id):
        addr = self.addr + 'getPersonPubs'
        addr = wrapUrlParameter(addr, id = person_id, offset = 0, size = 10, order = 'citation')
        response = requests.get(url=addr)
        result = response.json()['data'][0]['data']['pubs']
        pub_list = []
        for each in result:
            try:
                pub_list.append({
                    # 'abstract' : result[i]['abstract'],
                    'pub_id' : each['id'],
                    'title' : each['title'],
                    'num_citation' : each['ncitation'],
                    'year' : each['year'],
                    'authors_name_list' : [each['authors'][j]['name']for j in range(len(each['authors']))]
                })
            except:
                continue
        return pub_list
    
    def getPersonBasicInfo(self, person_id):
        addr = self.addr + 'getPersonBasicInfo'
        addr = wrapUrlParameter(addr, id = person_id)

        response = requests.get(url=addr)
        result = response.json()['data'][0]['data']
        # print(response)
        info_dic = {
                    'person_id' : person_id,
                    'name' : result['name'],
                    'gender' : result['gender'],
                    'organization' : result['aff'],
                    'position' : result['position'],
                    'bio' : result['bio'],
                    'education_experience' : result['edu'],
                    'email' : result['email']
                    # 'ncitation' : result['num_citation']
                }
        return info_dic
