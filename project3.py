from pypdf import PdfReader
import pandas
import argparse
import re
import spacy
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from joblib import load
import pickle
import joblib
from sklearn.feature_extraction.text import CountVectorizer


def load_file(doc_name):
    d=pandas.DataFrame()
    l_city=[]
    l_txt=[]
    
    reader=PdfReader(doc_name)
    fname=doc_name
    key=fname[:-4]
    txt=""
    l_city.append(key)
    for page in reader.pages:
        txt+=page.extract_text()
    l_txt.append(txt)
            
        
    d['city']=l_city
    d['txt']=l_txt   
    return d
def process_clean(d):
    # https://github.com/dipanjanS/text-analytics-with-python/blob/master/New-Second-Edition/Ch05%20-%20Text%20Classification/text_normalizer.py
    # https://www.analyticsvidhya.com/blog/2021/08/a-friendly-guide-to-nlp-text-pre-processing-with-python-example/
    format = r'[,;0-9)#@*.\"\':(\t\n]' 
    format1 = r'\[\]'
    d['text_cleaned']=d['txt'].str.lower()
    d['text_cleaned'] = d['text_cleaned'].replace(format,' ',regex=True)
    d['text_cleaned'] = d['text_cleaned'].replace(format1,' ',regex=True)
    d['text_cleaned']=d['text_cleaned'].replace("[Cc]ity"," ",regex=True)
    d['text_cleaned']=d['text_cleaned'].replace("smart"," ",regex=True)
    d['text_cleaned']=d['text_cleaned'].replace("page"," ",regex=True)
    d['text_cleaned']=d['text_cleaned'].apply(lambda s:lemm_text(s))
    d['text_cleaned']=d['text_cleaned'].apply(lambda s:stemming(s))
    d['text_cleaned']=d['text_cleaned'].apply(lambda s:delete_stopwords(s))
    return d
def lemm_text(txt):
    nlp=spacy.load('en_core_web_sm')
    txt = nlp(txt)
    txt = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in txt])
    return txt

def stemming(text):
    ps = nltk.porter.PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text
    
def delete_stopwords(text, is_lower_case=False):
    nltk.download('stopwords')
    stop_words=nltk.corpus.stopwords.words('english')
    t = ToktokTokenizer()
    tokens = t.tokenize(text)
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stop_words]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument("--document",type=str,required=True,help="City document")
    args=p.parse_args()
    doc_name=args.document
    d=load_file(doc_name)
    d=process_clean(d)
    model=joblib.load('model_km1.pkl')
    #model=pickle.load(open('models.pkl','rb'))
    #CV_model=CountVectorizer(ngram_range=(3,5))
    CV_model=joblib.load('vec.pkl')
    train=CV_model.transform(d['text_cleaned'])
    label=model.predict(train)
    d['cluster ID']=label
    name=doc_name[:-4]
    res="["+name+']'+' cluster id: '+str(label[0])
    #f=open('smartcity_predict.tsv','a+')
    d.to_csv('smartcity_predict.tsv',mode='a',sep="\t")
    #d.to_csv('smart.csv',sep=",")
    print(res)
    
    
    # ref=https://stackoverflow.com/questions/57438375/valueerror-x-has-29-features-per-sample-expecting-84
    #ref: https://docs.python.org/3/library/argparse.html
     #https://www.geeksforgeeks.org/how-to-append-pandas-dataframe-to-existing-csv-file/
    
