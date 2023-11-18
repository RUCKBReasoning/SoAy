import matplotlib.pyplot as plt
result_2 = [9, 27, 15]
result_1 = [9, 30, 15]
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