from flask import Flask,request,render_template
import psycopg2 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# Purl = os.environ['POSTGRES_URL']
# Puser = os.environ['POSTGRES_USER']
# Ppw = os.environ['POSTGRES_PW']
# Pdb = os.environ['POSTGRES_DB']

DB_URL = 'postgresql+psycopg2://postgres:1007@localhost:5432/postgres'
# print(DB_URL)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
print('success')
print(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)
app= app


try: 
    conn = psycopg2.connect(database="postgres", user="postgres",  
    password="1007", host="localhost")
    print("connected")
except:
    print ("I am unable to connect to the database")
mycursor =conn.cursor()
