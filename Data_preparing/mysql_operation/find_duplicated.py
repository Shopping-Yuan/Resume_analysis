import pandas as pd
from . import settings,csv_datatype,get_resume_data
import copy
import nltk
#df = pd.read_csv("mysql_operation\Resume.csv")
#print(df.duplicated().agg("count"))
#df2 = pd.read_csv("Resume_check.csv",encoding="ISO-8859-1")
#print(df2.columns)
#df = get_resume_data.get_data(csv_datatype.table_name,copy.deepcopy(settings.DATABASES['default']))
#def utf8_ignore(x):
#        return x.encode('utf-8', 'ignore').decode('utf-8')
#print(df[df["ID"]=="16852973"]["Resume_str"])
#tokens = df[df["ID"]=="16852973"]["Resume_str"].apply(nltk.word_tokenize).to_list()
#print(tokens)