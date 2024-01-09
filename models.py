from config import db 
# class user_table(db.Model):
#   userId = db.Column(db.String,primary_key=True)
#   Fname = db.Column(db.String(20))
#   Lname = db.Column(db.String(20))
#   email = db.Column(db.String(50))
#   gender = db.Column(db.String(1))
#   address = db.Column(db.String(120))
#   DOB= db.Column(db.String(10))
#   createDate = db.Column(db.String(10))
#   mobile_number = db.Column(db.String(10))
#   def __init__(self,u1,u2,u3,u4,u5,u6):
#       self.Fname =u1
#       self.Lname = u2
#       self.email= u3
#       self.gender=u4
#       self.address=u5
#       self.mobile_number=u6
      

class login_details(db.Model):
    user_mail = db.Column(db.String(30),primary_key=True)
    user_password = db.Column(db.Text)
    def __init__(self,l1,l2):
      self.user_mail = l1
      self.user_password = l2

