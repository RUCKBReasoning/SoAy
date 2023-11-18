import matplotlib.pyplot as plt

file_1 = open('result_1.txt', 'r')
result_1 = file_1.read()
list_1 = result_1.split('\n')
y_1 = [0, 0, 0]
for each in list_1:
    if each == 'ChatGPT raw result':
        y_1[0] = y_1[0] + 1
    if each == 'SoAy':
        y_1[1] = y_1[1] + 1
    if each == '人工标注回答':
        y_1[2] = y_1[2] + 1

file_2 = open('result_2.txt', 'r')
result_2 = file_2.read()
list_2 = result_2.split('\n')
y_2 = [0, 0, 0]
for each in list_2:
    if each == 'ChatGPT raw result':
        y_2[0] = y_2[0] + 1
    if each == 'SoAy':
        y_2[1] = y_2[1] + 1
    if each == '人工标注回答':
        y_2[2] = y_2[2] + 1

file_3 = open('result_3.txt', 'r')
result_3 = file_3.read()
list_3 = result_3.split('\n')
y_3 = [0, 0, 0]
for each in list_3:
    if each == 'ChatGPT raw result':
        y_3[0] = y_3[0] + 1
    if each == 'SoAy':
        y_3[1] = y_3[1] + 1
    if each == '人工标注回答':
        y_3[2] = y_3[2] + 1

# 数据
# x = ['ChatGPT raw result', 'SoAy', '人工标注回答']
x_1 = [-0.2, 0.8, 1.8]
x_2 = [0.0, 1.0, 2.0]
x_3 = [0.2, 1.2, 2.2]
values = y_1
# x = [i for i in range(3)]
plt.figure()

# 创建折线图
plt.bar(x_1, y_1, width=0.1, label='ChatGPT raw result')
plt.bar(x_2, y_2, width=0.1, label='SoAy')
plt.bar(x_3, y_3, width=0.1, label='Human Annotation')

# 设置标题和标签
plt.title('Bar Chart')
plt.xlabel('Method')
plt.ylabel('Vote')

plt.legend()

# 显示图表
plt.show()