import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",password="156585",database="hotel")
mycus=mydb.cursor()
bno=int(input("Enter bill number"))
tpaid=int(input("Enter total amount paid"))
query="update bill set tpaid={} where bno={}".format(tpaid,bno)
mycus.execute(query)
mydb.commit()

