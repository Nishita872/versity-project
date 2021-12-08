from flask import Flask ,render_template,request,redirect, url_for, session
import mysql.connector

import re
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def login():  
    return render_template("index.html")


@app.route('/result',methods=['POST',"GET"])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="students"




        
        
        
    )
    mycursor=mydb.cursor()
    def login_validation():
        user_id=request.form.get("user_id")
        password=request.form.get("password")
        mycursor=mydb.cursor()
        mycursor.execute('SELECT * FROM info WHERE user_id = % s AND password = % s', (user_id, password ))
    # cursor.execute("""SELECT * FROM studentinfo WHERE user_id LIKE'{}' and password LIKE'{}'""" .format(user_id,password))
        users= mycursor.fetchall()
   

        if users is not None:
       
          if users['user_id']==user_id and users['password']==password:
              return render_template("s_profile.html")
            
    
       
        else:
            return "unsucces"  
   
    # cursor.execute("""SELECT * FROM studentinfo WHERE user_id LIKE'{}' and password LIKE'{}'""" .format(user_id,password))
    

    # k
    
    # if request.method=="POST":
    #     signup=request.form
    #     user_id=signup["user_id"]
    #     password=signup["password"]
    #     mycursor.execute("SELECT * FROM info where user_id='" +user_id+"' and password='"+password+"'")
    #     r=mycursor.fetchall()
    #     count=mycursor.rowcount
    #     if count==1:
    #         return "succes"
    #     elif count>1:
    #         return 'flse'

    #     else:
    #         return "not true"   


    # mydb.commit()
    # mycursor.close()

  
if __name__ =='__main__':  
   app.run(debug = True)      


  
