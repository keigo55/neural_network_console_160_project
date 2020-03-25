import pandas as pd
import numpy as np

df = pd.DataFrame(np.zeros((3,4),dtype = int))

print(df)

df.to_csv("test1.csv",header = None, index = False)
