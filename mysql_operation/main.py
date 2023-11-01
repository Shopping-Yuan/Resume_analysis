import settings
import csv_datatype
import create_new_resumw_db
import create_resume_table
import add_data_from_csv
import get_resume_data
import copy
import time
create_new_resumw_db.create_db(settings.database_name,copy.deepcopy(settings.DATABASES['default']))
time.sleep(1)
create_resume_table.create_table(csv_datatype.table_name,copy.deepcopy(settings.DATABASES['default']),copy.deepcopy(csv_datatype.data))
add_data_from_csv.add_data(csv_datatype.table_name,csv_datatype.data_path,
                           copy.deepcopy(csv_datatype.data),copy.deepcopy(settings.DATABASES['default']))
df = get_resume_data.get_data(csv_datatype.table_name,copy.deepcopy(settings.DATABASES['default']))
print(df.shape,df.columns)