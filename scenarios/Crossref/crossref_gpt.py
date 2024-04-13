import json
import requests
from crossref_model import *
import traceback

crossref_api = crossref()

def generate_result_from_process(process):
    global searchPublisherBySubject
    global searchWorksByTitle
    global searchWorksByAuthor
    global getWorksByDoi
    global getPublisherBasicInfo
    global getPublisherWorks
    searchPublisherBySubject = crossref_api.searchPublisherBySubject
    searchWorksByTitle = crossref_api.searchWorksByTitle
    searchWorksByAuthor = crossref_api.searchWorksByAuthor
    getWorksByDoi = crossref_api.getWorksByDoi
    getPublisherBasicInfo = crossref_api.getPublisherBasicInfo
    getPublisherWorks = crossref_api.getPublisherWorks
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
    
def parse_response(response):
    process = response['answer'].split('--')[1]
    formatted_process = process.replace('\\n', '\n')
    return formatted_process
    
    


if __name__ == "__main__": 
    url = 'http://43.138.89.88:9988/api/chatcompletion'
    query_count = 0
    while True:
        query_count += 1
        if query_count > 1:
            if input('是否继续？(y/n)') == 'n':
                break
        data = {
            "model" : "gpt-4",
            "messages" : [
                {"role": "user", "content": "Here are some tool functions you can use. Each function returns a dict or a list of dict.\n------\nsearchPublisherBySubject(subject):\n    publisher_list = [{'publisher': str, 'doi_count': int}, {...}]\n    return publisher_list\n---\nsearchWorksByTitle(work_title):\n    work_list = [{'type': str, 'authors': str, 'doi': str, 'publisher': str}]\n    return work_list\n---\nsearchWorksByAuthor(author_name):\n    work_list = [{'title': str, 'doi': str}, {...}]\n    return work_list\n---\ngetWorksByDoi(doi):\n    work_info = [{'author_name': str, 'work_title': str, 'publisher': str, 'type': str, 'reference_count': int}]\n    return work_info\n---\ngetPublisherBasicInfo(publisher_name):\n    publisher_basic_info = [{'publisher_id': int, 'current_dois': int, 'backfile_dois': int, 'total_dois': int, 'doi_prefix': str}]\n    return publisher_basic_info\n---\ngetPublisherWorks(publisher_id):\n    work_list = [{'works_title': str, 'works_doi': str, 'works_author': str}, {...}]\n    return work_list\n------\nThe following example shows you how to use these tools in practical tasks. You are given a query. Break the query down into a combination of the python execution processes in order to solve it.\n---\nQuery: Please list some publishers in the medical field.\nCombination: searchPublisherBySubject\n--\npublisher_list = searchPublisherBySubject(subject='medical')\nfinal_result = publisher_list\n---\nQuery: I'd like to learn about the field of computer science. Can you give me a list of publishers that I can look for?\nCombination: searchPublisherBySubject\n--\npublisher_list = searchPublisherBySubject(subject='computer science')\nfinal_result = publisher_list\n---\nQuery: I want to seacher an article with DOI 10.4103/0019-5545.82558, please give me the information of this article.\nCombination: getWorksByDoi\n--\nwork_info = getWorksByDoi(doi='10.4103/0019-5545.82558')\nfinal_result = work_info\n---\nQuery: Please give me some publishers' id of crossref about the field of computer sicence.\nCombination: searchPublisherBySubject -> getPublisherBasicInfo\n--\npublisher_list = searchPublisherBySubject(subject='computer science')\npublisher = [publisher_list[i]['publisher'] for i in range(len(publisher_list))]\npublisher_id_list = []\nfor i in range(len(publisher)):\n    id = getPublisherBasicInfo(publisher_name=publisher[i])\n    if id == []:\n        continue\n    publisher_id_list.append({\n        'publisher_name' : publisher[i],\n        'publisher_id' : id[0]['publisher_id']\n    })\nfinal_result = publisher_id_list\n---\nQuery: Please obtain the current DOI numbers issued by some publishers in the field of biology from your database.\nCombination: searchPublisherBySubject -> getPublisherBasicInfo\n--\npublisher_list = searchPublisherBySubject(subject='biology')\npublisher = [publisher_list[i]['publisher'] for i in range(len(publisher_list))]\npublisher_doi_list = []\nfor i in range(len(publisher)):\n    doi_count = getPublisherBasicInfo(publisher_name=publisher[i])\n    if doi_count == []:\n        continue\n    publisher_doi_list.append({\n        'publisher_name' : publisher[i],\n        'doi_count' : doi_count[0]['current_dois']\n    })\nfinal_result = publisher_doi_list\n---\nQuery: Please obtain the backfile DOI numbers issued by some publishers in the field of medicine from your database.\nCombination: searchPublisherBySubject -> getPublisherBasicInfo\n--\npublisher_list = searchPublisherBySubject(subject='biology')\npublisher = [publisher_list[i]['publisher'] for i in range(len(publisher_list))]\npublisher_doi_list = []\nfor i in range(len(publisher)):\n    doi_count = getPublisherBasicInfo(publisher_name=publisher[i])\n    if doi_count == []:\n        continue\n    publisher_doi_list.append({\n        'publisher_name' : publisher[i],\n        'doi_count' : doi_count[0]['backfile_dois']\n    })\nfinal_result = publisher_doi_list\n---\nQuery: I want to know the total DOI numbers of some publishers in the field of computer science from your database.\nCombination: searchPublisherBySubject -> getPublisherBasicInfo\n--\npublisher_list = searchPublisherBySubject(subject='biology')\npublisher = [publisher_list[i]['publisher'] for i in range(len(publisher_list))]\npublisher_doi_list = []\nfor i in range(len(publisher)):\n    doi_count = getPublisherBasicInfo(publisher_name=publisher[i])\n    if doi_count == []:\n        continue\n    publisher_doi_list.append({\n        'publisher_name' : publisher[i],\n        'doi_count' : doi_count[0]['total_dois']\n    })\nfinal_result = publisher_doi_list\n---\nQuery: I want to know the DOI prefix of some publishers in the field of computer science from your database.\nCombination: searchPublisherBySubject -> getPublisherBasicInfo\n--\npublisher_list = searchPublisherBySubject(subject='biology')\npublisher = [publisher_list[i]['publisher'] for i in range(len(publisher_list))]\npublisher_doi_list = []\nfor i in range(len(publisher)):\n    doi_count = getPublisherBasicInfo(publisher_name=publisher[i])\n    if doi_count == []:\n        continue\n    publisher_doi_list.append({\n        'publisher_name' : publisher[i],\n        'doi_count' : doi_count[0]['doi_prefix']\n    })\nfinal_result = publisher_doi_list\n---\nQuery: Can you list some articles in the field of mathematics?\nCombination: searchPublisherBySubject -> getPublisherBasicInfo -> getPublisherWorks\n--\npublisher_list = searchPublisherBySubject(subject='mathematics')\npublisher = [publisher_list[i]['publisher'] for i in range(len(publisher_list))]\npublisher_id = []\nfor i in range(len(publisher)):\n    id = getPublisherBasicInfo(publisher_name=publisher[i])\n    if id == []:\n        continue\n    publisher_id.append({\n        'publisher_name' : publisher[i], \n        'id' : id[0]['publisher_id']\n    })\n    break\narticle_list = []\narticle = getPublisherWorks(publisher_id=publisher_id[0]['id'])\nfor i in range(len(article)):\n    article_list.append({\n        'article' : article[i]['works_title']\n    })\nfinal_result = article_list\n---\nQuery: Can you list some articles‘ DOI numbers in the field of mathematics?\nCombination: searchPublisherBySubject -> getPublisherBasicInfo -> getPublisherWorks\n--\npublisher_list = searchPublisherBySubject(subject='mathematics')\npublisher = [publisher_list[i]['publisher'] for i in range(len(publisher_list))]\npublisher_id = []\nfor i in range(len(publisher)):\n    id = getPublisherBasicInfo(publisher_name=publisher[i])\n    if id == []:\n        continue\n    publisher_id.append({\n        'publisher_name' : publisher[i], \n        'id' : id[0]['publisher_id']\n    })\n    break\narticle_list = []\narticle = getPublisherWorks(publisher_id=publisher_id[0]['id'])\nfor i in range(len(article)):\n    article_list.append({\n        'doi' : article[i]['works_doi']\n    })\nfinal_result = article_list\n---\nQuery: Can you list some articles and their authors in the field of mathematics?\nCombination: searchPublisherBySubject -> getPublisherBasicInfo -> getPublisherWorks\n--\npublisher_list = searchPublisherBySubject(subject='mathematics')\npublisher = [publisher_list[i]['publisher'] for i in range(len(publisher_list))]\npublisher_id = []\nfor i in range(len(publisher)):\n    id = getPublisherBasicInfo(publisher_name=publisher[i])\n    if id == []:\n        continue\n    publisher_id.append({\n        'publisher_name' : publisher[i], \n        'id' : id[0]['publisher_id']\n    })\n    break\narticle_list = []\narticle = getPublisherWorks(publisher_id=publisher_id[0]['id'])\nfor i in range(len(article)):\n    article_list.append({\n        'artical' : article[i]['works_title'],\n        'author' : artical[i]['works_author']\n    })\nfinal_result = article_list\n---\nQuery: I want to know the type of work THE ORIGINALITY OF DISSERTATION THESIS.\nCombination: searchWorksByTitle\n--\ntype = searchWorksByTitle(title='THE ORIGINALITY OF DISSERTATION THESIS')[0]['type']\nfinal_result = type\n---\nQuery: I want to know the author of work Magnetic susceptibility of solid solutions based on the higher silicide of nickel.\nCombination: searchWorksByTitle\n--\nauthor = searchWorksByTitle(title='Magnetic susceptibility of solid solutions based on the higher silicide of nickel')[0]['authors']\nfinal_result = author\n---\nQuery: I want to know the DOI number of work Economic Development and Gender.\nCombination: searchWorksByTitle\n--\ndoi = searchWorksByAuthor(title='Economic Development and Gender')[0]['doi']\nfinal_result = doi\n---\nQuery: I want to know the publisher of work Bangladesh-Myanmar [Report Number 6-24].\nCombination: searchWorksByTitle\n--\npublisher = searchWorksByTitle('Bangladesh-Myanmar [Report Number 6-24]')[0]['publisher']\nfinal_result = publisher\n---\nQuery: I want to know the reference count of work Inhibition of Leukotriene D4 Mediated Release of Prostacyclin Using Antisense DNA\nCombination: searchWorksByTitle -> getWorksByDoi\n--\nwork_doi = searchWorksByTitle(title='Inhibition of Leukotriene D4 Mediated Release of Prostacyclin Using Antisense DNA')[0]['doi']\nreference_count = getWorksByDoi(doi=work_doi)[0]['reference_count']\nfinal_result = reference_count\n---\n"},
            ]
        }

        print('请输入问题: ')
        query = input()
        data['messages'][0]['content'] = data['messages'][0]['content'] + query
    
        json_data = json.dumps(data)

        headers = {
            'Content-Type': 'application/json'
        }
    
        response = requests.post(url, data=json_data, headers=headers)
    
        response_json = response.json()
    
        process = parse_response(response_json)
    
        print(response_json['answer'].replace('\\n', '\n'))
    
    
        lines = []
        # while True:
        #     line = input()
        #     if line == 'eoc':
        #         break
        #     lines.append(line)
        lines = process.split('\n')
    
        code = '\n'.join(lines)
        #print("输入的代码是：{}".format(code))
        result = generate_result_from_process(process = code)
        print('代码执行结果:\n {}'.format(result))
