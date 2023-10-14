import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data)
print(df)
df.head(3)
print(df['score'])
df = df.dropna()
df.iloc[:,0:2]
k = {'name': ['Suresh'], 'score': [15.5], 'attempts': [1], 'qualify': ['yes']}
new_data = pd.DataFrame(k)
new_data2 = pd.concat([new_data,df],ignore_index=True)
print(new_data2)
new_data3 = new_data2.drop('attempts',axis=1)
print(new_data3)
def fun(num):
    if num>10: 
        return 1
    else: 
        return 0
new_data3.iloc[:,1:2]
new_data3['score'].apply(fun)
new_data3['success'] = new_data3['score'].apply(fun)
new_data3.to_csv(r'C:\Users\nabil\OneDrive\Desktop\GoMycode\data.csv')
#new_data3.to_excel(r'\C:\Users\nabil\OneDrive\Desktop\GoMycode\data.csv', index=False)