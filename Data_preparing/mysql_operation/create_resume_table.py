import pymysql

def create_table(t_n ,setting ,columns ):
    connect = pymysql.connect(**setting)
#    print(setting)
    cursor = connect.cursor()
#    print(" ".join(columns["ID"]))
    try:
        command = "CREATE TABLE IF NOT EXISTS {name}(".format(name = t_n)
        for column_name,datatype in columns.items():
           command = command +column_name +" "+" ".join(datatype)+" , "
        command = command.strip( ', ' ) 
        command += ");"
#        if __name__ == '__main__':
#            print(command)
        cursor.execute(command)
        connect.commit()
        print("New table created successfully!")
    #Exception : base class of non-fatal exception. Not include : SystemExit , KeyboardInterrupt , etc.

    except Exception as ex: 
        print(ex)
    finally:
        cursor.close()
        connect.close()