from flask import *  
import os 
import easygui
from pathlib import Path 

app = Flask(__name__) #creating the Flask class object   

@app.route('/')    
@app.route('/home')
def home():  
    return render_template("home.html") 


@app.route('/login')    
def login():  
    return render_template("login.html")

@app.route('/register')
def register():  
    return render_template("register.html")
 

@app.route('/upload')  
def upload():  
    return render_template("upload.html")

@app.route('/record')  
def record():  
    return render_template("record.html")

@app.route('/result') 
def result():
	return render_template("result.html") 

@app.route('/about') 
def about():
	return render_template("about.html") 

@app.route('/record_upload_success', methods = ['POST'])  
def record_upload_success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.filename = f.filename+'.avi'  
        f.save('./uploaded_file/'+f.filename)
        os.system('.\\OpenFace_2.2.0_win_x64\\FeatureExtraction.exe -f "./uploaded_file/'+f.filename+'" -aus -mloc "model/main_ceclm_general.txt"')
        filename=Path(f.filename).stem
        os.system('python second.1.py -f .\\processed\\'+filename+'.csv')
        return "Wait and then Go check Result"  


@app.route('/upload_success', methods = ['POST'])  
def upload_success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save('./uploaded_file/'+f.filename)
        os.system('.\\OpenFace_2.2.0_win_x64\\FeatureExtraction.exe -f "./uploaded_file/'+f.filename+'" -aus -mloc "model/main_ceclm_general.txt"')
        filename=Path(f.filename).stem
        os.system('python second.1.py -f .\\processed\\'+filename+'.csv')
        return render_template("upload_success.html", name = f.filename)  

if __name__ =='__main__':  
    app.run(host='0.0.0.0', debug=True)  