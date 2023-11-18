import matplotlib.pyplot as plt

file_1 = open('result_1.txt', 'r')
result_1 = file_1.read()
list_1 = result_1.split('\n')
y_1 = []
for each in list_1:
    if each == 'ChatGPT raw result':
        y_1.append(1)
    if each == 'SoAy':
        y_1.append(2)
    if each == '人工标注回答':
        y_1.append(3)

file_2 = open('result_2.txt', 'r')
result_2 = file_2.read()
list_2 = result_2.split('\n')
y_2 = []
for each in list_2:
    if each == 'ChatGPT raw result':
        y_2.append(1)
    if each == 'SoAy':
        y_2.append(2)
    if each == '人工标注回答':
        y_2.append(3)

file_3 = open('result_3.txt', 'r')
result_3 = file_3.read()
list_3 = result_3.split('\n')
y_3 = []
for each in list_3:
    if each == 'ChatGPT raw result':
        y_3.append(1)
    if each == 'SoAy':
        y_3.append(2)
    if each == '人工标注回答':
        y_3.append(3)

# 数据
x = [i for i in range(54)]
plt.figure()

# 创建折线图
plt.plot(x, list_1)
plt.plot(x, list_2)
plt.plot(x, list_3)

# 设置标题和标签
plt.title('Line Chart')
plt.xlabel('Question id')
plt.ylabel('Vote')

# 显示图表
plt.show()