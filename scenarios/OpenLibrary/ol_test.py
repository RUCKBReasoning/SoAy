from openlibrary_model import *
# todo

if __name__ == '__main__':
    api = openlibrary_soay()    
    print(api.searchBook(book_info = 'computer science')[0])
    print("=====================================")
    print(api.getBook(book_key = '/works/OL27448W')['title'])
    print("=====================================")
    print(api.searchAuthor(author_info = 'Tolkien')[0])
    print("=====================================")
    print(api.getAuthorBasicInfo(author_key = 'OL23919A')['name'])
    print("=====================================")
    print(api.getAuthorWorks(author_key = 'OL23919A', amount=10)[0]['title'])
    print("=====================================")
    print(api.searchSubject(subject = 'computer science')[0])
    