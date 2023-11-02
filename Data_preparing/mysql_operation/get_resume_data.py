import pymysql
import pandas as pd
def get_data(t_n,settings):
    connect = pymysql.connect(**settings)
    cursor = connect.cursor()
    try:
        command = "SELECT * FROM {name};".format(name = t_n)
        cursor.execute(command)
        now_data = cursor.fetchall()
        sql_columns = []
        sql_columns_description = cursor.description
        for index , items in enumerate(sql_columns_description):
            sql_columns.append(items[0])
        print(sql_columns)
        return pd.DataFrame(now_data, columns = sql_columns)

    #Exception : base class of non-fatal exception. Not include : SystemExit , KeyboardInterrupt , etc.
    except Exception as ex: 
        print(ex)
    finally:
        cursor.close()
        connect.close()

if __name__ == '__main__':
    import settings,csv_datatype
    df = get_data(csv_datatype.table_name,settings.DATABASES['default'])
    print(df.shape)