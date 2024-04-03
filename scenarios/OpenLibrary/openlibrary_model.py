import requests
import json

class openlibrary_soay:
    def __init__(self):
        self.addr = 'https://openlibrary.org'
    
    def searchBook(self, book_info):
        addr = self.addr + '/search.json'
        bookList = []
        headers = {
            'Content-Type' : 'application/json'
        }
        params = {
            "q": book_info,
            "sort": "rating",
        }
        response = requests.get(
            url = addr,
            headers = headers,
            params = params
        )
        result = response.json()
        for each in result['docs']:
            try:
                bookList.append({
                    'book_key' : each['key'],
                    'title' : each['title'],
                    'author_name' : each['author_name'],
                    'year': each['first_publish_year']
                })
            except:
                continue
        return bookList

    def getBook(self, book_key):
        addr = self.addr + book_key + '.json' 
        # book_key example: /works/OL27448W
        # API location: /works/OL27448W.json
        # addr = wrapUrlParameter(addr, id = book_key)
        response = requests.get(url = addr)
        result = response.json()
        info_dict = {}
        try:
            info_dict['description'] = result['description']['value']
        except:
            info_dict['description'] = 'book description'
        author_list = []
        for each in result['authors']:
            try:
                author_list.append({'author_key' : each['author']['key']})
            except:
                continue
        if author_list != []:
            info_dict['author_list'] = author_list
        try:
            info_dict['title'] = result['title']
        except:
            pass
        try:
            info_dict['first_publish'] = result['first_publish_date']
        except:
            pass
        try:
            info_dict['subjects'] = result['subjects']
        except:
            pass
        return info_dict

    def searchAuthor(self, author_info):
        addr = self.addr + '/search/authors.json'
        authorList = []
        headers = {
            'Content-Type' : 'application/json'
        }
        params = {
            "q" : author_info,
        }
        response = requests.get(
            url = addr,
            headers = headers,
            params = params
        )
        result = response.json()
        for each in result['docs']:
            try:
                authorList.append({
                    'author_key' : each['key'],
                    'name' : each['name'],
                    'alternate_names' : each['alternate_names'],
                })
            except:
                continue
        return authorList
    
    def getAuthorBasicInfo(self, author_key):
        addr = self.addr + '/authors/' + author_key + '.json'
        response = requests.get(url=addr)
        result = response.json()
        info_dict = {}
        try:
            info_dict['name'] = result['name']
        except:
            pass
        try:
            info_dict['alternate_names'] = result['alternate_names']
        except:
            pass
        try:
            info_dict['birth_date'] = result['birth_date']
        except:
            pass
        try:
            info_dict['work_count'] = result['work_count']
        except:
            pass
        try:
            info_dict['top_work'] = result['top_work']
        except:
            pass
        try:
            info_dict['top_subjects'] = result['top_subjects']
        except:
            pass
        return info_dict
    
    def getAuthorWorks(self, author_key, amount):
        addr = self.addr + '/authors/' + author_key + '/works.json'
        headers = {
            'Content-Type' : 'application/json'
        }
        json_content = json.dumps({
            "limit" : amount,
        })
        response = requests.get(
            url=addr,
            headers = headers,
            data = json_content
        )
        result = response.json()
        workList = []
        for each in result['entries']:
            try:
                workList.append({
                    'book_key': each['key'],
                    'title': each['title'],
                    'subjects': each['subjects'],
                })
            except:
                continue
        return workList
    
    def searchSubject(self, subject):
        addr = self.addr + '/subjects/' + subject + '.json'
        headers = {
            'Content-Type' : 'application/json'
        }
        json_content = json.dumps({})
        response = requests.get(
            url=addr,
            headers = headers,
            data = json_content
        )
        result = response.json()
        workList = []
        for each in result['works']:
            try:
                workList.append({
                    'book_key': each['key'],
                    'title': each['title'],
                })
            except:
                continue
        return workList
    