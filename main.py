import pandas as pd

# load dataset
df = pd.read_csv('data/training.1600000.processed.noemoticon.csv.zip', encoding='latin-1', header=None)
df = df[[0, 5]]
df.columns = ['polarity', 'text']

df['polarity'] = df['polarity'].map({0: 0, 4: 1})

print(df['polarity'].value_counts())

def clean_text(text):
        return text.lower()

df['clean_text'] = df['text'].apply(clean_text)

print(df[['text', 'clean_text']].head())