from flask import Flask , request
from flask_restful import Resource , Api,reqparse
from datetime import datetime
import json ,time

app = Flask (__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('birthdate')

def age_cal(date):		#calculate age 
	if (date.month==datetime.now().month and date.day<=datetime.now().day) or (date.month<datetime.now().month):
		return datetime.now().year-date.year
	else:
		return datetime.now().year-date.year-1
		

class Hello(Resource):
	def get(self):
		args = parser.parse_args()
	 	birthdate = args['birthdate']
		dt_birthdate = datetime.strptime(birthdate, '%d-%m-%Y')
		bd = dt_birthdate					
		dt_birthdate = dt_birthdate.strftime('%d-%m-%Y')
		return {"birthdate":dt_birthdate,"age":age_cal(bd)}

api.add_resource(Hello,'/birthdate')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5555)

