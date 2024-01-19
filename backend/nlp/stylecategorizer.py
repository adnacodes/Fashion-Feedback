import spacy
import pandas as pd
import numpy as np
import os
from typing import Set, List, Tuple
from spacy.tokens import DocBin

path = os.getcwd()
parent = os.path.dirname(path)


nlp = spacy.load("en_core_web_sm")
textcat = nlp.add_pipe("textcat")

df = pd.read_csv(parent + "/data/styles.csv")

print(df.head())
#Formats data/prepares for training: 
def make_docs(data: List[Tuple[str, str]], target_file: str, cats: Set[str]):
    docs = DocBin()
    for doc, label in nlp.pipe(data, as_tuples = True):
        for cat in cats: 
            doc.cats[cat] = 1 if cat == label else 0
  
        docs.add(doc)
    docs.to_disk(target_file)
    return (docs)

class StyleCategorizer:
    def __init__(self):
        self.cats = np.unique(df['masterCategory'])
        self.textcat = nlp.get_pipe("textcat")

s = StyleCategorizer()
print(s.cats)



