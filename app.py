from flask import Flask, render_template, request
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__)

#FLASK app that manages birthdays. IT stores only:  
#- a persons name, 
#- their birthday.  

@app.route('/Birthdays',methods = ['GET'])
def Birthdays():
#Connects to the DB
   con = sqlite3.connect("C:/Users/Admin/Desktop/SQLiteStudio/BirthdayList.db")
   cur = con.cursor()
   
#GETing  to /birthdays will list all birthdays in the system 
#curl -X GET localhost:5000/Birthdays ~
   if request.method == 'GET':
        Cur1 = cur.execute("SELECT ID, Name, Birthday FROM BirthdayList")   
        
#Put the result to a Var that can be used by the return      
   msg2 = {'list':Cur1.fetchall()}  
   
#Outputs the result    
   return msg2         
  
@app.route('/Birthday',methods = ['POST', 'PUT'])
def Birthday():
#Set the Vars
   Name2 = request.values.get('Name')
   Birthday2 = request.values.get('Birthday')
#Connects to the DB
   con = sqlite3.connect("C:/Users/Admin/Desktop/SQLiteStudio/BirthdayList.db")
   cur = con.cursor()
   
#POSTing to /birthday will post a new birthday , and create an entry   
#curl -X POST localhost:5000/Birthday -d "Name=Graham&Birthday=20210107" ~
   if request.method == 'POST':
        cur.execute("INSERT INTO BirthdayList (Birthday, Name) VALUES (?, ?)",(Name2,Birthday2))
        con.commit()
#Put the result to a Var that can be used by the return       
   msg2 = "Birthday Added"
   
#Outputs the result    
   return msg2 
 
@app.route('/Birthday/<Number>',methods = ['PUT', 'GET'])
def SelectBirthday(Number):
#Connects to the DB
   con = sqlite3.connect("C:/Users/Admin/Desktop/SQLiteStudio/BirthdayList.db")
   cur = con.cursor()
   
#an entry that can be viewed at /birthday/:number: (like /birthday/0001 for the first entry) 
#curl -X GET http://localhost:5000/Birthday/2  ~
   if request.method == 'GET':
        Cur1 = cur.execute("select ID, Name, Birthday from BirthdayList where ID = ?",(Number))
#Put the result to a Var that can be used by the return          
        msg2 = {'list':Cur1.fetchall()}  
        
#PUTing to /birthday/:number: will update details on that birthday 
#curl -X PUT localhost:5000/Birthday/2 -d "Name=Graham&Birthday=20210107" ~       
   if request.method == 'PUT': 
       Name2 = request.values.get('Name')
       Birthday2 = request.values.get('Birthday')
       cur.execute("UPDATE BirthdayList SET Birthday = ?, Name = ? WHERE ID = ?",(Birthday2, Name2, Number))
       con.commit()
#Put the result to a Var that can be used by the return  
       msg2 = "Record updated"
  
#Outputs the result    
   return msg2    
         
if __name__ == '__main__':
   app.run(debug = True)