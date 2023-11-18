import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 示例数据
# data = {
#     'A': [1, 2, 3, 4, 5],
#     'B': [2, 4, 6, 8, 10],
#     'C': [5, 4, 3, 2, 1],
#     'D': [10, 8, 6, 4, 2]
# }

result_dict = {}
for i in range(1, 11):
    # if i == 3 or i == 2 or i == 6:
    #     continue
    with open('result_{}.txt'.format(i), 'r') as f:
        content = f.read()
        result = content.split('\n')
        # print(result)
        num_result = []
        for each in result:
            if each == 'SoAy':
                num_result.append(0)
            elif each == 'ChatGPT raw result':
                num_result.append(1)
            else:
                num_result.append(-1)
        print(len(num_result))
        result_dict[str(i)] = num_result

# result_dict['mv'] = [0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, -1, -1, 0, 0, -1, 0, -1, -1, -1, -1, -1, 0, 0, -1, 0, -1, -1, 0, -1, -1, -1, -1, 0, 0, -1, -1, 0, -1, 0, 0, 0, -1, 0, 0, 0]
# print(len(result_dict['mv']))

# 创建DataFrame
df = pd.DataFrame(result_dict)

# 计算Spearman相关系数
corr_matrix = df.corr(method='spearman')

# 绘制热力图
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)

plt.savefig('spearman.pdf', dpi=500, format = 'pdf')

# 显示图形
plt.show()