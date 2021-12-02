import sys
import os
from flask import Flask, jsonify, request,Response
from pathlib import Path
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory, Blueprint
from werkzeug.utils import secure_filename
import subprocess



#fom = Blueprint('image_rec_forms', __name__)
app = Flask(__name__)



APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = '/Users/admin/Desktop/Code Editor Docker/demo'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/git', methods=['POST'])
def giturl():
    print("getting git url for remote add")

    try:
        
        data =request.get_json()


        fileurl =data["url"]
        project = data["project"]

        filepath = "../workspaces/"+ project+ "/giturl.txt"

        #dir_list = os.listdir(filepath)

        if Path(filepath).exists():
            content = open(filepath, "r")
            check_url=content.read()
            

            if(check_url == fileurl):
                resp={"status":False}

            else:
                f = open(filepath, "w")
                f.write(fileurl)
                f.close()
                resp={"status":True}

        else:
            f = open(filepath, "w+")
            f.write(fileurl)
            f.close()
            resp={"status":True}
        
        return resp
    
    
    except Exception as e:
        print(e)
        response = {
                    "status":False
                }
        return response

@app.route('/jarversion', methods=['POST'])
def jarcheck():
    print("got jar check api request")

    fileurl =request.files["demo"]
    project_name = request.form["project"]
    target_date = request.form["target_date"]

    filepathjar = 'sh '  + "simple.sh "+project_name
    try:
        filepath = "../workspaces/"+ project_name+ "/.versioncheck"
        
        
        if Path(filepath).exists(): 
            fileurl.save(os.path.join(app.root_path,"../workspaces/"+project_name+"/libs", secure_filename("com.simplifyQA.Agent.jar")))
            os.popen(filepathjar)
            
            resp={"status":"jar file got updated"}
        else:
            fileurl.save(os.path.join(app.root_path,"../workspaces/"+project_name+"/libs", secure_filename("com.simplifyQA.Agent.jar")))
            
            os.popen(filepathjar)
            resp={"status":"jar file got updated"}
        
        return resp
    
    
    
    except Exception as e:
        print(e)
        response = {
                    "status":"false"
                }
        return response


@app.route('/versionmatch', methods=['POST'])
def version():
    print("got jar check api request")

    data = request.get_json()

    project =data["project"]
    target_date = data["target_date"]

    try:
        filepath = filepath = "../workspaces/"+ project+ "/.version" 
        
        
        if Path(filepath).exists(): 
            content = open(filepath, "r")
            check_url=content.read()
            

            if(check_url == target_date):
                resp={"status":False}

            else:
                f = open(filepath, "w")
                f.write(target_date)
                f.close()
                #fileurl.save(os.path.join(app.root_path,project_name, secure_filename("com.simplifyQA.Agent.jar")))
                resp={"status":True}

        else:
            f = open(filepath, "w+")
            f.write(target_date)
            f.close()
            #fileurl.save(os.path.join(app.root_path,project_name, secure_filename("com.simplifyQA.Agent.jar")))
            resp={"status":True}
        
        return resp
    
    
    
    except Exception as e:
        print(e)
        response = {
                    "status":"false"
                }
        return response



if __name__ == "__main__":
    #nos = []
    app.run(host ='0.0.0.0', port = 19010,debug=True)
