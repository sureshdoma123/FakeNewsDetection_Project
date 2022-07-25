import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from flask import Flask, render_template, request, url_for

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index123.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/pred',methods=["GET","POST"])
def pred():
    if request.method=="POST":
        d=request.form['data']
        
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
        news_headline=d
        data=cv.transform([news_headline]).toarray()
        r=model.predict(data)
    
        return render_template('index123.html',data=r[0])



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)