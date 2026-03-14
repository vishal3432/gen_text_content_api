import pandas as pd 
import re
import nltk

nltk.download('stopwords')

def clean_text(text):
  text = text.lower()
  text = re.sub(r'http\S+', '', str(text))
  text = re.sub(r'[^a-zA-Z]', '', text)
  return text

def load_dataset():
  df = pd.read_csv("../dataset/blog_dataset.csv")
  df["text"] = df["title"] + "" + df["subtitle"].fillna("")
  df["text"] = df["text"].apply(clean_text)
  return df["text"].tolist()