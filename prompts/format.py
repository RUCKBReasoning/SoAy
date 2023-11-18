import jsonlines
docs = []
# index_candidates = ['route', 'searhPerson',
# 'searchPerson -> getCoauthors',
# 'searchPerson -> getPersonPubs',
# 'searchPerson -> getPersonBasicInfo',
# 'searchPerson -> getCoauthors -> searchPerson',
# 'searchPerson -> getCoauthors -> getPersonInterest',
# 'searchPerson -> getCoauthors -> getCoauthors',
# 'searchPerson -> getPersonPubs -> getPublication',
# 'searchPublication -> getPublication',
# 'searchPublication -> getPublication -> getPersonInterest',
# 'searchPublication -> getPublication -> getCoauthors',
# 'searchPublication -> getPublication -> getPersonPubs',
# 'searchPublication -> getPublication -> getPersonBasicInfo',
# 'searchPublication -> getPublication -> searchPerson]'
# ]

# for i in range(len(index_candidates)):
while True:
    index = input('index: ')
    # index = index_candidates[i]
    # print('index: {}'.format(index_candidates[i]))
    # flag = input('insert? [y for YES and n for NO, o for OVER]:')
    # if flag == 'n':
    #     continue
    # if flag == 'o':
    #     break
    if index == 'o':
        break
    result = ''
    while True:
        txt = input()
        if txt == 'c':
            break
        result = result + '\n' + txt
    # result = result.replace('\'', '\\\'')
    doc = {'index' : index, 'prompt' : result}
    docs.append(doc)
    print(f"saved\n{doc}")

with jsonlines.open('prompt_jsonl/prompt_qg.jsonl', 'a') as f:
# with open('prompt_0516.jsonl', 'a') as f:
    for doc in docs:
        f.write(doc)
    f.close()
# print(len(result))
print('已存储！！')