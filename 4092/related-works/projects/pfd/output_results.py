import pandas as pd

pd.set_option('display.max_rows', None, 'display.max_columns', None)

readFrame = pd.read_feather(path='./outputs.feather', )

print(readFrame)
