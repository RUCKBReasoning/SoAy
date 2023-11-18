result_list = []
for i in range(1, 11):
    with open('result_{}.txt'.format(i), 'r') as f:
        content = f.read()
        result = content.split('\n')
        # print(result)
        num_result = []
        for each in result:
            if each == 'SoAy':
                num_result.append(1)
            else:
                num_result.append(0)
        result_list.append(num_result)
print(len(result_list[0]))