#database
username = "root"
host = 'localhost'
port = 3306  # default MySQL port
database_name = "resume_database"
password = "tim11111"

DATABASES = {
    'default': {
    "host" : host,
    "port" : port,
    "user" : username,
    "db": database_name,
    "password" : password,
    "charset" : "utf8mb4"
    }
}