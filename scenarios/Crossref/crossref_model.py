import requests
import json

class crossref:
    def __init__(self):
        self.addr = "https://api.crossref.org/"

    def searchPublisherBySubject(self, subject):
        addr = self.addr + "journals?query=" + subject + "&rows=5"
        journal_list = []
        headers = {
            'Content-Type' : 'application/json'
        }
        response = requests.get(
            url = addr,
            headers = headers
        )
        result = response.json()
        for journal in result['message']['items']:
            try:
                publisher = journal['publisher']
                total_dois = journal['counts']['total-dois']
                journal_list.append({
                    'publisher': publisher,
                    'doi_count': total_dois
                })
            except:
                continue
        return journal_list
        
    def getWorksByDoi(self, doi):
        addr = self.addr + "works/" + doi
        works_info = []
        headers = {
            'Content-Type' : 'application/json'
        }
        # json_content = json.dumps({
            
        # })
        response = requests.get(
            url = addr,
            headers = headers
            #data = json_content
        )
        result = response.json()
        try:
            author_info = result['message']['author'][0]
            works_info.append({
                "author_name" : f"{author_info['given']} {author_info['family']}",
                "work_title" : result['message']['title'][0],
                "publisher" : result['message']['publisher'],
                "type" : result['message']['type'],
                "reference_count" : result['message']['reference-count'],
            })
        except:
            pass
        return works_info
        
        
        
    def searchWorksByTitle(self, title):
        formatted_title = title.replace(" ", "+")
        addr = self.addr + "works?query.title=" + formatted_title
        work_info = []
        headers = {
            'Content-Type' : 'application/json'
        }
        response = requests.get(
            url = addr,
            headers = headers
        )
        result = response.json()
        try:
            author_info = result['message']['items'][0]['author'][0]
            work_info.append({
                "type" : result['message']['items'][0]['type'],
                "authors" : f"{author_info['given']} {author_info['family']}",
                "doi" : result['message']['items'][0]['DOI'],
                "publisher" : result['message']['items'][0]['publisher']
            })
        except:
            pass
        return work_info
        
    def searchWorksByAuthor(self, author_name):
        formatted_author_name = author_name.replace(" ", "+")
        addr = self.addr + "works?query.author=" + formatted_author_name + "&rows=5"
        works_info = []
        headers = {
            'Content-Type' : 'application/json'
        }
        response = requests.get(
            url = addr,
            headers = headers
        )
        result = response.json()
        for work in result['message']['items']:
            try:
                title = work['title'][0]
                doi = work['DOI']
                works_info.append({
                    "title": title,
                    "doi": doi
                })
            except:
                continue
        return works_info
        
    def getPublisherBasicInfo(self, publisher_name):
        formatted_publisher_name = publisher_name.replace(" ", "+")
        addr = self.addr + "members?query=" + formatted_publisher_name
        publisher_info = []
        headers = {
            'Content-Type' : 'application/json'
        }
        response = requests.get(
            url = addr,
            headers = headers
        )
        result = response.json()
        try:
            publisher_info.append({
                "publisher_id" : result['message']['items'][0]['id'],
                "current_dois" : result['message']['items'][0]['counts']['current-dois'],
                "backfile_dois" : result['message']['items'][0]['counts']['backfile-dois'],
                "total_dois" : result['message']['items'][0]['counts']['total-dois'],
                "doi_prefix" : result['message']['items'][0]['prefixes'][0]
            })
        except:
            pass
        return publisher_info
        
    def getPublisherWorks(self, publisher_id):
        addr = self.addr + "members/" + publisher_id + "/works?rows=5"
        works_info = []
        headers = {
            'Content-Type' : 'application/json'
        }
        response = requests.get(
            url = addr,
            headers = headers
        )
        result = response.json()
        for work in result['message']['items']:
            try:
                author_info = work['author'][0]
                works_info.append({
                    "works_title" : work['title'][0],
                    "works_doi" : work['DOI'],
                    "works_author" : f"{author_info['given']} {author_info['family']}"
                })
            except:
                continue
        return works_info

        
