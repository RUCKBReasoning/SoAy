from crossref_model import *
# TODO

if __name__ == "__main__":
    api = crossref()
    print(api.searchWorksByDoi(doi = "10.4103/0019-5545.82558"))
    print("=====================================")
    print(api.searchJournalBySubject(subject = "biology"))
    print("=====================================")
    print(api.searchWorksByTitle(title = "How to write a good abstract for a scientific paper or conference presentation"))
    print("=====================================")
    print(api.getAuthorWorks(author_name = "Richard Feynman"))
    print("=====================================")
    print(api. getPublisherBasicInfo(publisher_name = "Annals of Family Medicine"))
    print("=====================================")
    print(api.searchPublisher(publisher_id = "1"))
    print("=====================================")
