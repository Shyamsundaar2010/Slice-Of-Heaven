from flask import Flask
from datetime import datetime
from flask import render_template,request,redirect,url_for,jsonify,session
import re
import sys
from config import app,db,mycursor
from flask.wrappers import Request
from models import login_details
#change

global unqmail 
global orderid
global totalvar
unqmail = ''
#app = Flask(__name__)

@app.route('/')
def home1():
   unqmail=''
   return render_template('signup.html')


@app.route('/home')
def home():
   return render_template('index.html')
if __name__ == '__main__':
       app.run()
       



@app.route("/menu",methods = ['POST','GET'])
def order():
        if request.method== 'GET':
              return render_template("menu.html")
        elif request.method== 'POST':
               p1 = int(request.form.get('p1'))
               p2 = int(request.form.get('p2'))
               p3 = int(request.form.get('p3'))
               p4 = int(request.form.get('p4'))
               p5 = int(request.form.get('s1'))
               p6 = int(request.form.get('s2'))
               p7 = int(request.form.get('s3'))
               iprice1=12.50
               iprice2 = 15.50
               iprice3 = 16.50
               iprice4 = 20.00
               iprice5 = 8.50
               iprice6 = 9.50
               iprice7 = 10.50
               total =iprice1*p1+iprice2*p2+iprice3*p3+iprice4*p4+iprice5*p5+iprice6*p6+iprice7*p7
               global totalvar
               totalvar = total
               db.session.execute("insert into order_table(uid,price) values((select u_id from user_table where email = '{}'),'{}')".format(unqmail,total))
               db.session.commit()
               res = db.session.execute("select oid from order_table where uid = (select u_id from user_table where email = '{}') order by oid desc limit 1".format(unqmail))
               res = res.fetchall()
               tempvar =str(res[0]) 
               tempvar = tempvar.strip('(')
               tempvar = tempvar.strip(')')
               tempvar = tempvar.strip(',')
               tempvar = int(tempvar)
               global orderid 
               orderid = tempvar
               
               if p1>0:
                      db.session.execute("insert into order_item values('{}',(select nameitem from menu_table where menuid = 1),'{}')".format(tempvar,p1))
                      db.session.commit()
               if p2>0:
                      db.session.execute("insert into order_item values('{}',(select nameitem from menu_table where menuid = 2),'{}')".format(tempvar,p2))
                      db.session.commit()
               if p3>0:
                      db.session.execute("insert into order_item values('{}',(select nameitem from menu_table where menuid = 3),'{}')".format(tempvar,p3))
                      db.session.commit()
               if p4>0:
                      db.session.execute("insert into order_item values('{}',(select nameitem from menu_table where menuid = 4),'{}')".format(tempvar,p4))
                      db.session.commit()
               if p5>0:
                      db.session.execute("insert into order_item values('{}',(select nameitem from menu_table where menuid = 5),'{}')".format(tempvar,p5))
                      db.session.commit()
               if p6>0:
                      db.session.execute("insert into order_item values('{}',(select nameitem from menu_table where menuid = 6),'{}')".format(tempvar,p6))
                      db.session.commit()
               if p7>0:
                      db.session.execute("insert into order_item values('{}',(select nameitem from menu_table where menuid = 7),'{}')".format(tempvar,p7))
                      db.session.commit()   
       
               return redirect(url_for('bill'))
               

@app.route("/signup",methods = ['POST','GET'] )
def about():
       if request.method== 'GET':
              return render_template("signup.html")
       elif request.method== 'POST':
              p1 = request.form.get('fname')
              p2 = request.form.get('lname')
              p3 = request.form.get('email')
              p4 = request.form.get('gen')
              p5 = request.form.get('addr')
              p6 = request.form.get('number')
              p7 = request.form.get('pswd')
              #obj1 = user_table(p1,p2,p3,p4,p5,p6)
              #db.session.add(obj1)
              #print(obj1,p1,p2,p3,p4,p5,p6,p7)
              db.session.execute("insert into user_table(f_name,l_name,email,gender,address,create_date,mobile_number) values('{}','{}','{}','{}','{}',current_date,'{}')".format(p1,p2,p3,p4,p5,p6))
              db.session.commit()
              #obj2 = login_details(p3,p7)
              #db.session.add(obj2)
              unqmail =p3
              db.session.execute("insert into login_details values('{}','{}')".format(p3,p7))
              db.session.commit()
              return redirect(url_for('home1'))
              #return render_template('/menu')
@app.route("/loginuser",methods = ['POST','GET'] )
def userlogin():
       error = None
       if request.method== 'GET':
              return render_template("signup.html")
       elif request.method== 'POST':
              p1 =request.form.get('email')
              p2 = request.form.get('pswd')
              global unqmail
              unqmail = p1
              res = db.session.execute("select user_mail from login_details where user_mail = '{}' and user_password = '{}'".format(p1,p2))
              res = res.fetchall()[0][0]
              #print(res,p1)
              if res!=p1:
                     error = "INVALID PASSWORD"
                     return render_template("signup.html",error=error)
              else:
                  return redirect(url_for('home'))   

@app.route("/cart",methods = ['POST','GET'])    
def cartout():
       if request.method == 'GET':
              return render_template("cart.html")
       elif request.method =='POST':
              session['data'] = request.json
              data = session.get('data', None)
              print("session items: " ,data)
       return redirect(url_for('home')) 

# @app.route("/bill")
# def bill():
#      return render_template("bill.html")

@app.route('/bill')
def bill():
    mycursor.execute("SELECT * FROM order_item where orderid = '{}'".format(orderid))
    data = mycursor.fetchall()
    return render_template('bill.html', data=data,total=totalvar)

@app.route('/deleteorder')
def deleteorder():
       db.session.execute("delete from order_item where orderid ='{}'".format(orderid))
       return redirect(url_for('order')) 

