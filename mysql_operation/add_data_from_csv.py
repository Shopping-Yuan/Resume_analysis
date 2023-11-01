import pymysql
import pandas as pd
import sqlalchemy
from data_cleaning import clean_data_df
#from sqlalchemy.dialects.mysql import VARCHAR , MEDIUMTEXT
from sqlalchemy.dialects.mysql import *

def add_data(t_n,d_p,d_dic,setting):
    connect = pymysql.connect(**setting)
#    word = f'''mysql+pymysql://{setting[user]}:{setting["password"]]}@{setting["host"]}:
#                                      {setting["port"]}/{setting["db"]}?charset=utf8mb4'''
    word = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(
        user = setting["user"],password = setting["password"],host = setting["host"],
        port = setting["port"],db = setting["db"])
    print(word)
    engine = sqlalchemy.create_engine(word)
    data_for_sqlalchemy = {}
    columns_need_clean = []
    for columns, datatype in  d_dic.items():
#        print(columns,datatype[0])
        type_with_limit = datatype[0].strip(")").split("(")
#        print(type_with_limit)
        para = {}
        if len(type_with_limit)>1:
            para["length"] = int(type_with_limit[1])
        if "TEXT" in type_with_limit[0]:
            para["charset"]="utf8mb4"
            columns_need_clean.append(columns)
        data_class = getattr(sqlalchemy.dialects.mysql, type_with_limit[0])
#        print(data_class(**para))
        data_for_sqlalchemy[columns] = data_class(**para)

#    print(data_for_sqlalchemy)
    df = pd.read_csv(d_p,chunksize = 100,encoding = "utf-8")
    for chunk in df:
        try:
            chunk = clean_data_df(chunk,columns_need_clean)
            chunk.to_sql(t_n,con=engine, if_exists='append', index=False, dtype =data_for_sqlalchemy)
        except Exception as ex: 
#            pass
            print(ex)

    engine.dispose()
    connect.close()