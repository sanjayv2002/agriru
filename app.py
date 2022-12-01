from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import cross_origin
import numpy as np
import plotly
import json

import pickle
import tools

npk =[]
nut =[]
out="rice"
app = Flask(__name__, template_folder="templates")
print("Model Loaded")

@app.route("/home",methods=['GET'])
@cross_origin()
def home():
	return render_template("home.html")
@app.route("/",methods=['GET', 'POST'])
@cross_origin()
def predict():
	global npk
	global nut
	global out
	if request.method == "POST":

		# statw
		state_no = int(request.form['state'])
		state = tools.state_id(state_no)
		#print("state= ",state)
		# city
		city = str(request.form['city'])
		# nitrogen ratio
		N = float(request.form['N'])
		# potassium ratio
		K = float(request.form['K'])
		# phospours ratio
		P = float(request.form['P'])
        # ph
		ph = float(request.form['ph'])
		
		npk = [N,P,K,ph]
		#print(npk)
		nut = [calcium,magnesium ,sulphur,zinc,iron,boron,magnese]
		unit =[ca_unit,mg_unit,s_unit,zn_unit,fe_unit,b_unit,mn_unit]
		#print(npk,nut,unit)
		nut = tools.convert(nut,unit)
		#print(nut)
		#append temp,humidity,rainfall in input_lst
		loc=tools.loc_att(state,city)
		input_lst=[npk[0],npk[1],npk[2],loc[0],loc[1],npk[3],loc[2]]
		input_lst = np.array(input_lst).reshape(1,-1)
		pred = model.predict(input_lst)
		out = pred[0]
		#print(out)
		

		return render_template("{}.html".format(out))
	
		


	return render_template("predict.html")

if __name__=='__main__':
	app.run(debug=True)