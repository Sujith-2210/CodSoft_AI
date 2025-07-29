import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

tv=TfidfVectorizer()

m=pd.read_csv("https://raw.githubusercontent.com/bapujik/dataSets/main/movie_dataset.csv")

f=["keywords","cast","genres","director"]

for fe in f:
  m[fe]=m[fe].fillna(" ")

df1=m["genres"]+" "+m["director"]+" "+m["cast"]+" "+m["keywords"]

m["combined_features"]=df1

tr=tv.fit_transform(m["combined_features"])

tr.toarray()

s1=cosine_similarity(tr)

m1=input("Enter movie name: ")

i=m[m.title==m1].values[0][0]

sm=list(enumerate(s1[i]))

ss=sorted(sm,key=lambda x:x[1],reverse=True)

sm1=ss[0:]

for i in range(0,10):
  mi=sm1[i][0]
  print(m["title"].loc[mi])
