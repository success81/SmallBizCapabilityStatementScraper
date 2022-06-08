#Libraries
import sys
import fitz
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def home():

	if request.method == 'POST':
		fname = request.form["myfile"]
	

	
	#fname = "/Users/dewaynewhitfield/Documents/Flask Companies/DoddiTech Capability Statement.pdf"



	
	
	doc = fitz.open(fname)  
	text = ''
	for page in doc:
	    text += page.get_text()

	#Converted Capability Statement
	complete_text = text


	#Tokenized complete text
	tokens = word_tokenize(complete_text)

	#Logic to pull NACICS
	NACICS = []
	num_check = ["0","1","2","3","4","5","6","7","8","9"]
	for x in tokens:
	    if len(x) == 6:
	        if x[0] in num_check and x[1] in num_check and x[2] in num_check and x[3] in num_check and x[4] in num_check and x[5] in num_check:
	            NACICS.append(x)
	        else:
	            pass

	#Putting Nacics on string
	codes = ""

	for x in NACICS:
	    codes += x
	    codes += " "

	#Combining all text and NACICS into one list
	output = []
	

	output.append(codes)
	output.append(complete_text)
	


	return render_template('after.html', data = output)
  	
if __name__ == "__main__":
    app.run(debug=True)



