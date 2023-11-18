import matplotlib.pyplot as plt

file_1 = open('result_1.txt', 'r')
result_1 = file_1.read()
list_1 = result_1.split('\n')

file_2 = open('result_2.txt', 'r')
result_2 = file_2.read()
list_2 = result_2.split('\n')

file_3 = open('result_3.txt', 'r')
result_3 = file_3.read()
list_3 = result_3.split('\n')

file_4 = open('result_4.txt', 'r')
result_4 = file_4.read()
list_4 = result_4.split('\n')

file_5 = open('result_5.txt', 'r')
result_5 = file_5.read()
list_5 = result_5.split('\n')

file_6 = open('result_6.txt', 'r')
result_6 = file_6.read()
list_6 = result_6.split('\n')

file_7 = open('result_7.txt', 'r')
result_7 = file_7.read()
list_7 = result_7.split('\n')

file_8 = open('result_8.txt', 'r')
result_8 = file_8.read()
list_8 = result_8.split('\n')

file_9 = open('result_9.txt', 'r')
result_9 = file_9.read()
list_9 = result_9.split('\n')

file_10 = open('result_10.txt', 'r')
result_10 = file_10.read()
list_10 = result_10.split('\n')

result_candidate = [list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10]
result = [0, 0, 0]

mv_result = []
for i in range(len(list_1)):
    # if i == 2 or i == 3 or i == 6:
    #     continue
    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0
    
    for j in range(10):
        if result_candidate[j][i] == 'ChatGPT raw result':
            cnt_0 += 1
        if result_candidate[j][i] == 'SoAy':
            cnt_1 += 1
        if result_candidate[j][i] == '人工标注回答':
            cnt_2 += 1

    sl = [cnt_0, cnt_1, cnt_2]
    sl.sort(reverse=True)

    if cnt_1 == sl[0]:
        result[1] = result[1] + 1
        mv_result.append(0)

    elif cnt_0 == sl[0]: 
        result[0] = result[0] + 1
        mv_result.append(-1)

    elif cnt_2 == sl[0]:
        mv_result.append(-1)
        result[2] = result[2] + 1
     
    # if cnt_0 >= 2:
    #     result[0] = result[0] + 1
    # if cnt_1 >= 2:
    #     result[1] = result[1] + 1
    # if cnt_2 >= 2:
    #     result[2] = result[2] + 1

print('mv_result : {}'.format(mv_result))

# 数据
x = ['ChatGPT raw result', 'SoAy', 'Human']
print('result:{}'.format(result))
# x = [i for i in range(3)]
plt.figure()

# 创建折线图
plt.bar(x, result, width=0.5)

# 设置标题和标签
plt.title('Majority Voting')
plt.xlabel('Method')
plt.ylabel('Vote')

# 显示图表
plt.show()