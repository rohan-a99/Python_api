import shutil
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
        project1 = data["project"]
        project=str(project1.replace(" ",""))
        
        filepath = "../giturl_details/" + project+ "_giturl.txt"

        #dir_list = os.listdir(filepath)

        if Path(filepath).exists():
            content = open(filepath, "r")
            check_url=content.read()
            
            # filepathjar = 'sh '  + "publish.sh "+project + " " + check_url

            if(check_url == fileurl):
                resp={"status":False}

            else:
                # os.popen(filepathjar)
                
                f = open(filepath, "w")
                f.write(fileurl)
                f.close()
                print("git url updated")
                resp={"status":True}

        else:
            # filepathjar = 'sh '  + "publish.sh "+project + " " + fileurl
            # os.popen(filepathjar)
            # print("git url updated")
            f = open(filepath, "w+")
            f.write(fileurl)
            f.close()
            print("giturl updated")
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
    project_name2 = request.form["project"]
    target_date = request.form["target_date"]

    project_name=str(project_name2.replace(" ",""))
    filepathjar = 'sh '  + "simple.sh "+project_name
    try:
        filepath =  "../workspaces/" + project_name +"/.version"
        
        
        if Path(filepath).exists(): 
            fileurl.save(os.path.join(app.root_path,"/workspaces/"+project_name+"/libs", secure_filename("com.simplifyQA.Agent.jar")))
            os.popen(filepathjar)
            resp={"status":"jar file got updated"}
        else:
            fileurl.save(os.path.join(app.root_path,"/workspaces/"+project_name+"/libs", secure_filename("com.simplifyQA.Agent.jar")))
            
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

    project1 =data["project"]
    target_date = data["target_date"]
    project=str(project1.replace(" ",""))

    try:
        filepath ="../workspaces/" + project+ "/.version" 
        
        
        if Path(filepath).exists(): 
            content = open(filepath, "r")
            check_url=content.read()
            

            if(check_url == target_date):
                resp={"status":False}

            else:
                # f = open(filepath, "w")
                # f.write(target_date)
                # f.close()
                #fileurl.save(os.path.join(app.root_path,project_name, secure_filename("com.simplifyQA.Agent.jar")))
                resp={"status":True}

        else:
            # f = open(filepath, "w+")
            # f.write(target_date)
            # f.close()
            #fileurl.save(os.path.join(app.root_path,project_name, secure_filename("com.simplifyQA.Agent.jar")))
            resp={"status":True}
        
        return resp
    
    
    
    except Exception as e:
        print(e)
        response = {
                    "status":"false"
                }
        return response


@app.route('/versioncopy', methods=['POST'])
def versionco():
    print("got jar check api request")

    data = request.get_json()

    project1 =data["project"]
    target_date = data["target_date"]
    project=str(project1.replace(" ",""))

    try:
        filepath ="../workspaces/" + project+ "/.version" 
        
        
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



@app.route('/project', methods=['POST'])
def project():
    print("checking if project directory present")

    try:
        project_type=""
        data =request.get_json()
        url = data["url"]
        project1 = data["project"]
        id = data["id"]

        project=str(project1.replace(" ",""))

        if "github" in url:
            project_type="github"
        if "gitlab" in url:
            project_type="gitlab"
        if "bitbucket" in url:
            project_type="bigbucket"
	

        build = "chmod +x build.sh\nrm -rf target/classes\ncd / \ncd bash-files\n./build.sh " +project + "\ncd "
        load  = "chmod +x load.sh\ncd / \ncd bash-files\n./dependencies.sh "+ project + "\ncd"
        
        filepath = r"../workspaces/"
        filepath2 = r"../workspaces/" + project  


        isFile = Path(filepath2).is_dir()


        if isFile:
            # f = open(filepath+"/build.sh", "w")
            # f.write(build)
            # f.close()
            print("Directory already present")
            response = {
                    "codeeditor_url":"http:127.0.0.1:7000/#/workspaces/"+project,
                    "status":"File Already present"
                }
            return response


        else:

            if "github" in url:
                shutil.copytree("../CodeEditor_github", filepath2)
                
            if "gitlab" in url:
                shutil.copytree("../CodeEditor_gitlab", filepath2)
            
            if "bitbucket" in url:
                shutil.copytree("../CodeEditor_bitbucket", filepath2)
            
            
            #shutil.move(filepath+"CodeEditor",filepath2)

            f = open(filepath2+"/build.sh", "w")
            f.write(build)
            f.close()

            f = open(filepath2+"/load.sh", "w")
            f.write(load)
            f.close()
            
            command = "sh "+"project_creation.sh " + project + " " + url

            os.popen(command) 

            print("project created and pulled successfully...")


            response = {
                    "codeeditor_url":"http:127.0.0.1:7000/#/workspaces/"+project,
                    "status":"Directory created"
                }

            return response
            
            

        
    
    except Exception as e:
        print(e)
        response = {
                    "status":False
                }
        return response


@app.route('/giturlchange', methods=['POST'])
def gitchange():
    print("checking if project directory present")

    try:
        project_type=""
        data =request.get_json()
        url = data["url"]
        project1 = data["project"]
        id = data["id"]

        project=str(project1.replace(" ",""))

        if "github" in url:
            project_type="github"
        if "gitlab" in url:
            project_type="gitlab"
        if "bitbucket" in url:
            project_type="bigbucket"
	

        build = "chmod +x build.sh\nrm -rf target/classes\ncd / \ncd bash-files\n./build.sh " +project + "\ncd "
        load  = "chmod +x load.sh\ncd / \ncd bash-files\n./dependencies.sh "+ project + "\ncd"
        
        filepath = r"../workspaces/"
        filepath2 = r"../workspaces/" + project  


        isFile = Path(filepath2).is_dir()


        if isFile:
            # f = open(filepath+"/build.sh", "w")
            # f.write(build)
            # f.close()
            print("Directory already present")
            response = {
                    "codeeditor_url":"http:127.0.0.1:7000/#/workspaces/"+project,
                    "status":"File Already present"
                }
            return response


        else:

            if "github" in url:
                shutil.copytree("../CodeEditor_github", filepath2)
                
            if "gitlab" in url:
                shutil.copytree("../CodeEditor_gitlab", filepath2)
            
            if "bitbucket" in url:
                shutil.copytree("../CodeEditor_bitbucket", filepath2)
            
            
            #shutil.move(filepath+"CodeEditor",filepath2)

            f = open(filepath2+"/build.sh", "w")
            f.write(build)
            f.close()

            f = open(filepath2+"/load.sh", "w")
            f.write(load)
            f.close()
            
            command = "sh "+"project_creation.sh " + project + " " + url

            os.popen(command) 

            print("project created and pulled successfully...")


            response = {
                    "codeeditor_url":"http:127.0.0.1:7000/#/workspaces/"+project,
                    "status":"Directory created"
                }

            return response
            
            

        
    
    except Exception as e:
        print(e)
        response = {
                    "status":False
                }
        return response

if __name__ == "__main__":
    #nos = []
    app.run(host ='0.0.0.0', port = 19010,debug=True)
