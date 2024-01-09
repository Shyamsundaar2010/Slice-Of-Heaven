from flask_sqlalchemy import SQLAlchemy
from config import app,db
from controller import *

if __name__ == '__main__':
#   res = db.session.execute('select * from student_details')
#   for r in res:
#       print(r)
  print(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])
  print(app.config['SQLALCHEMY_DATABASE_URI'])
  app.run(debug=True,host = '127.0.0.1',port='8000')