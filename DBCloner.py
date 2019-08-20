import pymysql
from time import sleep
from termcolor import colored, cprint

def PrintStatus(string, colour):
    print ('[ ',end="")
    cprint(string, colour, end="")
    print (' ] ',end="")

def Build():
    print ('Building ... \ ', end = "\r")
    sleep(0.25)
    print ("Building ... |", end="\r")
    sleep(0.25)
    print ("Building ... /", end="\r")
    sleep(0.25)
    print ("Building ... -", end="\r")
    sleep(0.25)
    print ("Building ... |", end="\r")
    sleep(0.25)
    print ('Building ... \ ', end = "\r")
    sleep(0.25)
    print ("Building ... |", end="\r")
    sleep(0.25)
    print ("Building ... /", end="\r")
    sleep(0.25)
    print ("Building ... -", end="\r")
    sleep(0.25)

print ('''

  / ____|_   _|   /\     
 | (___   | |    /  \    
  \___ \  | |   / /\ \   
  ____) |_| |_ / ____ \  
 |_____/|_____/_/    \_\ 
                         
''')

print ('DB Cloning Script:')
sleep (0.5)
print ('REQUIRES PYMYSQL')
sleep (0.5)
print ('------------')
sleep (0.5)

while True:
    PrintStatus('*','red')
    host = input('(locahost: 127.0.0.1) input Host IP address: ')
    PrintStatus('*','red')
    user = input('user: ')
    PrintStatus('*','red')
    passwd = input ('passwd: ')
    PrintStatus('*','red')
    db = input('Target DB: ')
    PrintStatus('*','red')
    unicode = input('unicode y/n:')
    if unicode.lower()[:1] == 'y':
        unicode = True
    else:
        unicode = False
    PrintStatus('*','red')
    charset = input('(DEF: utf8) Charset: ')
    while True:
        try:
            PrintStatus('*','red')
            port = int(input('(DEF: 3306) port: '))
        except:
            pass
        else:
            break
    sleep(1)
    print ('----------')
    PrintStatus('*','red')
    NEW_DB = input('New DB Name (leave blank for Queries): ')

    try:
        PrintStatus('PENDING', 'yellow')
        print('Connection to Mysql Server...')
        conn = pymysql.connect(host = host, user = user, passwd = passwd, db = db,use_unicode=unicode, charset=charset, port=port)
    except:
        sleep(0.5)
        print ("",end='\r')
        PrintStatus ('REFUSED', 'red')
        print('Connection to Mysql Server...')
        print ('Check the following Details: ')
        print ('---------------------------- ')
        PrintStatus('HOST','yellow')
        print(host)
        PrintStatus('USER','yellow')
        print(user)
        PrintStatus('PASSWD','yellow')
        print(passwd)
        PrintStatus('DB','yellow')
        print(db)
        PrintStatus('UNICODE','yellow')
        print(unicode)
        PrintStatus('CHARSET','yellow')
        print(charset)
        PrintStatus('PORT','yellow')
        print(port)
        sleep(0.25)
        print ('Please retry')
        print('---------------------')
    else:
        sleep(0.5)
        print("",end='\r')
        PrintStatus('ACCEPTED', 'green')
        print('Mysql Connection')
        break

cursor = conn.cursor()

Query = 'SHOW TABLES'
cursor.execute(Query)
Tables01 = cursor.fetchall()
Tables = []
for i in Tables01:
    Tables.append(i[0])

Columns = []
for i in Tables:
    Query = 'SHOW COLUMNS FROM {}'.format(i)
    cursor.execute(Query)
    x = cursor.fetchall()
    Columns_Temp = []
    for a in x:
        Columns_Temp.append([a[0],a[1]])
    Columns.append(Columns_Temp)
    
#QUERY01 = "CREATE DATABASE '{}".format(NEW_DB)
Queries = []
for i in range (len(Columns)):
    Query = "CREATE TABLE {}(".format(Tables[i])
    for x in range (len(Columns[i])):
        Query = Query + Columns[i][x][0] + " " + Columns[i][x][1] + ", "
    Queries.append(Query[:len(Query)-2] + ")")

if NEW_DB == "":
    for Query in Queries:
        print(Query)
else:
    PrintStatus('*','red')
    Confirmation = input("Are you sure you want to build the DB: '{}'. y/n: ".format(NEW_DB))
    if Confirmation.lower()[:1] == 'y':
        Query = "CREATE DATABASE {}".format(NEW_DB)
        cursor.execute(Query)
        Query = "USE {}".format(NEW_DB)
        cursor.execute(Query)
        for Query in range (len(Queries)):
            Percent = Query*100/len(Queries)
            Build()
            print ('Building: {}%'.format(str(Query*100/len(Queries))[:4]))
            cursor.execute(Queries[Query])
            sleep(0.5)
        conn.commit()
        print ('Building: 100%')
PrintStatus('Thank you for using this script // SyberProjects','green')           
    
