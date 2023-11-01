import pymysql
def create_db(db_name , setting):
    setting.pop("db")
    connect = pymysql.connect(**setting)
    cursor = connect.cursor()
    try:
        command1 = "CREATE SCHEMA `{name}` DEFAULT CHARACTER SET utf8mb4;".format(name = db_name)
#        print(command1)
        cursor.execute(command1)
        connect.commit()
        print("New db created successfully!")
        command2 = "SHOW DATABASES"
        cursor.execute(command2)
        connect.commit()
    #Exception : base class of non-fatal exception. Not include : SystemExit , KeyboardInterrupt , etc.
    except Exception as ex: 
        print(ex)
    finally:
        cursor.close()
        connect.close()