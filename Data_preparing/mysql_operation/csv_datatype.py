#from sqlalchemy.dialects.mysql import VARCHAR , MEDIUMTEXT

data_path  = 'mysql_operation\Resume.csv'
table_name = "all_resumes"
data = {"ID":("VARCHAR(10)","NOT NULL","UNIQUE"),
        "Resume_str":("MEDIUMTEXT","NOT NULL"),
        "Resume_html":("MEDIUMTEXT","NOT NULL"),
        "Category":("VARCHAR(100)","NOT NULL")
        }
'''
data_for_sqlalchemy ={
        'ID': VARCHAR(10),
        'Resume_str': MEDIUMTEXT(charset="utf8mb4"),
        'Resume_html': MEDIUMTEXT(charset="utf8mb4"),
        'Category': VARCHAR(100)
    }
print(type(data_for_sqlalchemy["ID"]))
'''