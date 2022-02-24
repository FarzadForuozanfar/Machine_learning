import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(121)

N = 500
std = 0.8
bananas = pd.DataFrame({
    'length': np.random.normal(8, std, N),
    'width': np.random.normal(4, std, N),
    'class': np.zeros(N, dtype='int')}
)
apples = pd.DataFrame({
    'length': np.random.normal(6, std, N),
    'width': np.random.normal(6, std, N),
    'class': np.ones(N, dtype='int')}
)
fruits = pd.concat([bananas, apples])
plt.scatter(x=apples['length'], y=apples['width'],color = 'r', label='apples')
plt.scatter(x=bananas['length'], y=bananas['width'],color = 'orange', label='bananas')
plt.legend()
plt.xlabel('Length')
plt.ylabel('Width')
plt.show()



