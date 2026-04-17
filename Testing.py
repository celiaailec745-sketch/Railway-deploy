#liste est modifiable (modifier les données)
a = [1,4,7]
a[0]=3
print(a)

#tuple immutable 'protéger les données)
a=(1,4,7)
print(a)

bp = [1,2,3,4,5,6,7,8,9,10]
b_pairs =[ b for b in bp if b % 2 == 0 ]
print(b_pairs)
b_impair = [b for b in bp if b % 2 == 1]
print(b_impair)


import pandas as pd
df = pd.DataFrame({'Nom':['A','B','C'], 'Age':[25,40,35]})
result = df[df['Age'] > 30]
print(result)

import tensorflow as tf
t = tf.constant([[1,2],[3,4]])
print(t.shape)  # (2,2)


