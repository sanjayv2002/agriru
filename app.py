from flask import Flask,render_template,url_for,request,jsonify, redirect
from flask_cors import cross_origin
import numpy as np
import pandas as pd 
import plotly
import json

import pickle
import tools


npk =[]
nut =[]
out="rice"
app = Flask(__name__, template_folder="templates")
model = pickle.load(open("./model.pkl", "rb"))

#tr = pickle.load(open('./transformer.pkl','rb'))
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
		soil_test = str(request.form.get('res'))
		if soil_test == '1':

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
		elif soil_test == '0':
		
			dis = str(request.form.get('dis'))
			city = str(request.form.get('city'))
			base = pd.read_csv(r'./resources/raw/base.csv')
			npk = base[base['district'] == dis.upper()]

			npk = [npk.n, npk.p, npk.k, npk.ph]


		#print(nut)
		#append temp,humidity,rainfall in input_lst
		loc=tools.loc_att(city, dis)
		input_lst=[npk[0],npk[1],npk[2],loc[0],loc[1],npk[3],loc[2]]
		
		print(input_lst)
		input_lst = np.array(input_lst).reshape(1,-1)
		pred = model.predict(input_lst)
		out = pred[0]
		#print(out)
		

		return redirect("/crop")
	
		


	return render_template("predict.html")

@app.route("/crop",methods=['GET'])
@cross_origin()
def crop():
	if out:
		apple ='{}_pic'.format(out.lower())
		namey = out.lower()
	else:
		apple = 'rice_pic'
		namey = 'rice'

	dict_info = {
		'apple_pic':'Apples grow best on a well-drained, loam soils having a depth of 45 cm. The soil should be free from hard substrata and water-logged conditions',
		'banana_pic':' Soil for banana should have good drainage, adequate fertility and moisture. Deep, rich loamy soil ',
		'grapes_pic':' Vine roots grow in the top 3 to 4 feet of soil, so they need a planting area with at least a few feet of soil on top of rock or hardpan. They also prefer soils with good drainage ',
		'jute_pic':'The new gray alluvial soil of good depth, receiving salt from annual floods, is best for jute.',
		'maize_pic':'Maize can be grown in all types of soil.<br> But for good growth and productivity of maize, loam and medium to heavy soil having adequate amount of bacteria and proper drainage is suitable.',
		'mango_pic':'''Mango grows well on wide variety of soils, such as lateritic,
            alluvial, sandy loam and sandy.The loamy, alluvial, well-drained, aerated and deep soils (2-2.5 m) rich
            in organic matter ideal for mango cultivation. The water table should be
            around 3 m and soils with high water table are unsuitable for mango.''',
		'orange_pic':'Orange trees prefer light to medium textured soils, with good drainage and free from stagnant water. Orange fruits do not grow well in the ground where there was before another citrus field.',
		'papaya_pic':'Deep, well drained sandy loam soil is ideal for cultivation of papaya.',
		'rice_pic':' Rice crop needs a hot and humid climate. It is best suited to regions which have high humidity, prolonged sunshine and an assured supply of water.'
	}

	print(apple)
	return render_template("crop.html", name = apple, namey = namey,content = dict_info[apple])

if __name__=='__main__':
	app.run(debug=True)