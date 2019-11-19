#!C:/Users/leoviquez/AppData/Local/Programs/Python/Python37-32/python.exe
import cgi,psycopg2
print ("Content-type: text/html\n\r\n\r")
form = cgi.FieldStorage()
usuario = form.getvalue('usuario')
clave  = form.getvalue('clave')
try:
    connection = psycopg2.connect(user = "postgres",
                          password = "12345",
                                  host = "localhost",
                                  port = "5432",
                                  database = "test")
    cursor = connection.cursor()
    cursor.execute("select * from usuarios where usuario='{}' and clave=md5('{}');".format(usuario,clave))
    record = cursor.fetchone()
    if (record):
        print(true)
    else:
        print(false)
except (Exception, psycopg2.Error) as error :
    print (false)
finally:
    if(connection):
        cursor.close()
        connection.close()
