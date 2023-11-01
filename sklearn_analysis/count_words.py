from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
#import torch
from mysql_operation import *
import copy
df =get_resume_data.get_data(csv_datatype.table_name,copy.deepcopy(settings.DATABASES['default']))
print(df.shape,df.columns)
df_1 = df[df['Category']=="HR"]
import unicodedata
s  = df_1["Resume_str"]
#print(s)
vectorizer = CountVectorizer(max_features=100)
vectorizer.fit(s)
feature_names = vectorizer.get_feature_names_out()
s_trans = vectorizer.transform(s)
print(feature_names)
import pandas as pd
s_df= pd.DataFrame(s_trans.toarray(),columns = feature_names)
df_feature_counts = s_df.agg("sum").sort_values(ascending=False)
print(df_feature_counts)

df_by_class = df.groupby('Category').agg(lambda x : " ".join(x))["Resume_str"]
print(df_by_class)

vectorizer_tfidf = TfidfVectorizer(max_features = 10)
s_tfidf = vectorizer_tfidf.fit_transform(df_by_class)
feature_names_tfidf = vectorizer_tfidf.get_feature_names_out()
df_feature_tfidf= pd.DataFrame(s_tfidf.toarray(),columns = feature_names_tfidf,index = list(df_by_class.index))
print(df_feature_tfidf)
