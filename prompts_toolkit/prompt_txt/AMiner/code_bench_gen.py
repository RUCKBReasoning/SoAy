def searchPerson(**kwargs):
    if 'name' in kwargs:
        ...
    if 'interest' in kwargs:
        ...
    if 'organization' in kwargs:
        ...
    personList = []
    ...
    personList.append(
        {
            'person_id' : ...,
            'name' : ...,
            'interests' : ...,
            'num_citation' : ...,
            'num_pubs': ...,
            'organization' : ...
        }
    )
    return personList

def searchPublication(publication_info):
    pubList = []
    ...
    pubList.append({
        'pub_id' : ...,
        'title' : ...,
        'year' : ...
    })
    return pubList

def getPublication(pub_id):
    ...
    info_dict = {}
    for key in ['abstract', 'author_list', 'num_citation', 'year', 'pdf_link', 'venue']:
        try:
            info_dict[key] = ...
        except:
            info_dict[key] = ''

    return info_dict

def getPersonInterest(person_id):
    ...
    interest_list = ...#list of interests strings
    return interest_list

def getCoauthors(person_id):
    ...
    coauthorsList = ...#list of person_id strings
    return coauthorsList

def getPersonPubs(person_id):
    pubList = []
    ...
    pubList.append({
        'authors_name_list' : ...,
        'pub_id' : ...,
        'title' : ...,
        'num_citation' : ...,
        'year' : ...
    })
    return pubList

def getPersonBasicInfo(person_id):
    ...
    info_dict = {}
    for key in ['person_id', 'name', 'gender', 'organization', 'position', 'bio', 'education_experience', 'email']:
        try:
            info_dict[key] = ...
        except:
            info_dict[key] = ''
    return info_dict