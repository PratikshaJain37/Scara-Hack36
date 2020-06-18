"""
Created on Fri Nov  8 23:23:22 2019

@author: Pratiksha
"""

# app.py for Scara Web App

from flask import Flask, render_template, request
from data import Articles
import cv2
from pyzbar import pyzbar

app = Flask(__name__)

Articles = Articles()
S = []

@app.route('/')
def index():
	return render_template('home.html')
	
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/articles')
def articles():
	return render_template('articles.html', articles = Articles)

   
@app.route("/submit", methods=['GET', 'POST'])
def submit():

	if request.method == 'POST':
		f = request.files['file']  
		f.save(f.filename)  
		image = cv2.imread(f.filename)
		barcodes = pyzbar.decode(image)
		data = ""
		for barcode in barcodes:
		# extract the bounding box location of the barcode and draw the
		# bounding box surrounding the barcode on the image
			(x, y, w, h) = barcode.rect
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

		# the barcode data is a bytes object so if we want to draw it on
		# our output image we need to convert it to a string first
			data = barcode.data.decode("utf-8")

			for i in range(len(Articles)):
				if data==Articles[i]['id']:
					S.append([Articles[i]['title'],Articles[i]['mrp']])
			
			
					
			
			
			
			
	return render_template('bill.html', data=S) 
				  

				   
				   
				   
if __name__ == '__main__':
	app.run(debug = True)
