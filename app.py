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
		print('this works')
		# district
		dis = str(request.form.get('dis'))
		city = str(request.form.get('city'))
		# nitrogen ratio
		N = float(request.form.get('N'))
		# potassium ratio
		K = float(request.form.get('K'))
		# phospours ratio
		P = float(request.form.get('P'))
        # ph
		ph = float(request.form.get('ph'))
		print(dis, N, K, P, ph)
		npk = [N,P,K,ph]
		#print(nut)
		#append temp,humidity,rainfall in input_lst
		#loc=tools.loc_att(dis)
		#input_lst=[npk[0],npk[1],npk[2],loc[0],loc[1],npk[3],loc[2]]
		#input_lst = np.array(input_lst).reshape(1,-1)
		#pred = model.predict(input_lst)
		#pyout = pred[0]
		#print(out)
		

		return render_template("predict.html".format(out))
	
		


	return render_template("predict.html")

@app.route("/crop",methods=['GET'])
@cross_origin()
def crop():
	apple = 'apple_pic'
	return render_template("crop.html", name = apple)

if __name__=='__main__':
	app.run(debug=True)