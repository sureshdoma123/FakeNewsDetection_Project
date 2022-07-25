import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
data=pd.read_csv("news.csv")
#print(data.head())
x=np.array(data['title'])
y=np.array(data['label'])
cv=CountVectorizer()
x=cv.fit_transform(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=MultinomialNB()
model.fit(x_train,y_train)
#print(model.score(x_test,y_test)*100)
news_headline="CA Exams 2021:Supreme Court asks ICAI to extend opt-out option for july exams, final order tomorrow"
data=cv.transform([news_headline]).toarray()
print(model.predict(data))