import json
import requests
from openlibrary_model import *
import traceback

ol_api = openlibrary_soay()

def generate_result_from_process(process):
    global searchBook 
    global searchAuthor
    global searchSubject
    global getBook
    global getAuthorBasicInfo
    global getAuthorWorks
    searchBook = ol_api.searchBook
    searchAuthor = ol_api.searchAuthor
    searchSubject = ol_api.searchSubject
    getBook = ol_api.getBook
    getAuthorBasicInfo = ol_api.getAuthorBasicInfo
    getAuthorWorks = ol_api.getAuthorWorks
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
                {"role": "user", "content": "Here are some tool functions you can use. Each function returns a dict or a list of dict.\n-----\nsearchBook(book_info):\n    book_list = [{'book_key': str, 'title': str, 'author_name': str, 'year': }, {...}]\n    return book_list\n---\ngetBook(book_key):\n    info_dict = {'description': str, 'author_list': [{'author_key': str}, {...}], 'title': str, 'first_publish': str, 'subjects': list of str}\n    return info_dict\n---\nsearchAuthor(author_info):\n    author_list = [{'author_key': str, 'name': str, 'alternate_names': list of str}, {...}]\n    return author_list\n---\ngetAuthorBasicInfo(author_key):\n    info_dict = {'name': str, 'alternate_names': list of str, 'birth_date': str, 'work_count': int, 'top_work': str, 'top_subjects': list of str}\n    return info_dict\n---\ngetAuthorWorks(author_key, amount):\n    work_list = [{'book_key': str, 'title': str, 'subjects': list of str}, {...}]\n    return work_list\n---\nsearchSubject(subject):\n    work_list = [{'book_key': str, 'title': str}, {...}]\n    return work_list\n-----\nThe following example shows you how to use these tools in practical tasks. You are given a query. Break the query down into a combination of the python execution processes in order to solve it.\n---\nQuery: 列出所有与Computer Science有关的书籍\nCombination: searchBook\n--\nbook_list = searchBook(book_info = 'Computer Science')\nfinal_result = book_list\n---\nQuery: 介绍一下Harry Potter这部书\nCombination: searchBook->getBook\n--\nbook_list = searchBook(book_info = 'Harry Potter')\ntarget_book_key = book_list[0]['book_key']\ntarget_book = getBook(book_key = target_book_key)\nfinal_result = target_book['description']\n---\nQuery: The Lord of the Rings这部书的作者是谁\nCombination: searchBook->getBook->getAuthorBasicInfo\n--\nbook_list = searchBook(book_info = 'The Lord of the Rings')\ntarget_book_key = book_list[0]['book_key']\ntarget_book = getBook(book_key = target_book_key)\ntarget_author_key = target_book['author_list'][0]['author_key']\nauthor = getAuthorBasicInfo(author_key = target_author_key)\nfinal_result = author['name']\n---\nQuery: A Game of Thrones这部书是在哪一年出版的\nCombination: searchBook->getBook\n--\nbook_list = searchBook(book_info = 'A Game of Thrones')\ntarget_book_key = book_list[0]['book_key']\ntarget_book = getBook(book_key = target_book_key)\nfinal_result = target_book['first_publish']\n---\nQuery: Flatland是什么类型的书\nCombination: searchBook->getBook\n--\nbook_list = searchBook(book_info = 'Flatland')\ntarget_book_key = book_list[0]['book_key']\ntarget_book = getBook(book_key = target_book_key)\nfinal_result = target_book['subjects']\n---\nQuery: J. K. Rowling还用过哪些笔名\nCombination: searchAuthor\n--\nauthor_list = searchAuthor(author_info = 'J. K. Rowling')\ntarget_author = author_list[0]\nfinal_result = target_author['alternate_names']\n---\nQuery: 作家R. R. Martin是哪一年出生的\nCombination: searchAuthor->getAuthorBasicInfo\n--\nauthor_list = searchAuthor(author_info = 'R. R. Martin')\ntarget_author_key = author_list[0]['author_key']\ntarget_author = getAuthorBasicInfo(author_key = target_author_key)\nfinal_result = target_author['birth_date']\n---\nQuery: 作家Mazo de la Roche一生大约创作了多少部作品\nCombination: searchAuthor->getAuthorBasicInfo\n--\nauthor_list = searchAuthor(author_info = 'Mazo de la Roche')\ntarget_author_key = author_list[0]['author_key']\ntarget_author = getAuthorBasicInfo(author_key = target_author_key)\nfinal_result = target_author['work_count']\n---\nQuery: 作家J. K. Rowling有哪些出名的作品\nCombination: searchAuthor->getAuthorWorks\n--\nauthor_list = searchAuthor(author_info = 'J. K. Rowling')\ntarget_author_key = author_list[0]['author_key']\nwork_list = getAuthorWorks(author_key = target_author_key, amount = 5)\nfinal_result = [work['title'] for work in work_list]\n---\nQuery: 介绍一部Mazo de la Roche创作的作品\nCombination: searchAuthor->getAuthorWorks->getBook\n--\nauthor_list = searchAuthor(author_info = 'Mazo de la Roche')\ntarget_author_key = author_list[0]['author_key']\nwork_list = getAuthorWorks(author_key = target_author_key, amount = 1)\ntarget_work_key = work_list[0]['book_key']\ntarget_work = getBook(book_key = target_work_key)\nfinal_result = target_work\n---\nQuery: 列举一些科幻题材的代表作\nCombination: searchSubject\n--\nwork_list = searchSubject(subject = 'science fiction')\nfinal_result = work_list\n---\nQuery: 简要介绍一本自传类别的书籍\nCombination: searchSubject->getBook\n--\nwork_list = searchSubject(subject = 'autobiography')\ntarget_work_key = work_list[0]['book_key']\ntarget_work = getBook(book_key = target_work_key)\nfinal_result = target_work\n---\nQuery: "},
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
