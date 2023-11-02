import nltk
#nltk.download('punkt')
import pandas as pd
import unicodedata
def clean_data_df(df,columns):
    def utf8_ignore(x):
        return x.encode('utf-8', 'ignore').decode('utf-8')
    def to_halfwidth(x):
        return "".join(unicodedata.normalize('NFKC',letter) for letter in x)
    def clean_data(text,f):
        tokens = nltk.word_tokenize(text)
        new_text  = list(map(f, tokens))
        return new_text
    for column_name in columns:
        df[column_name] = df[column_name].apply(lambda text : " ".join(clean_data(text,utf8_ignore)))
        df[column_name] = df[column_name].apply(lambda text : " ".join(clean_data(text,to_halfwidth)))
    return df
if __name__ == '__main__':
    import csv_datatype
    df_all = pd.read_csv(csv_datatype.data_path)
    df = df_all.loc[df_all["ID"] == 14413257]
    text = clean_data_df(df,["Resume_str"])
    print(text["Resume_str"])
    
#    file = open('check.txt', 'w' , encoding='UTF-8')
#    text = text.to_numpy
#    file.write(text[0])
#    file.close()
    
    



   