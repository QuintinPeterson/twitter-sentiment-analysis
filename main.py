import pandas as pd

# load dataset
df = pd.read_csv('data/training.1600000.processed.noemoticon.csv.zip', encoding='latin-1', header=None)
df = df[[0, 5]]
df.columns = ['polarity', 'text']
print(df.head())

df = df[df.polarity != 2]