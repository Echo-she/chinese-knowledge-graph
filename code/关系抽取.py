# coding=utf-8

import jiagu
import pandas as pd
import re

result = []
df = pd.read_csv('data.csv')
print(df.columns)

for i in range(df.shape[0]):
    temp = df.iloc[i, -1]

    # new = re.findall(r'[\u4e00-\u9fa5a-zA-Z0-9]', temp)
    # knowledge = jiagu.knowledge(''.join(new))

    knowledge = jiagu.knowledge(temp)
    result += knowledge

print(result)
