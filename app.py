from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

def assignmentgrade(Testname):
    
    #Testname = input("Enter the Test name")
    file_path = f'/Users/pbritwum/Downloads/MattaEaglesApp/{Testname}.csv'
    
    data = pd.read_csv("/Users/pbritwum/Downloads/MattaEaglesApp/Introduction_To_Robotics62526 (2).csv")

    data = data.drop(index = [0,1])

    data['Score'] = data[Testname]

    colums_to_keep = ["Last Name","First Name",'Email Address','Score']

    data = data[colums_to_keep]

    data['Student Name'] = data["Last Name"] + ', ' + data["First Name"]

    data["Student Num"] = data['Email Address'].str.replace("@dallasisd.org","")

    columns_to_drop  = ["Last Name","First Name",'Email Address']

    data = data.drop(columns = columns_to_drop,axis =1)
    
    data.to_csv(file_path, index = False)
    
    return f'{Testname} has been saved to your folder'
   
   
@app.route('/')
def home():
    return render_template("index.html",)

@app.route('/run', methods=['POST'])
def run_assignmentgrade():
    Testname = request.form.get('Testname')
    
    try:
        result = assignmentgrade(Testname)
        return jsonify({"message": result, "status": "success"})
    except Exception as e:
        return jsonify({"message": str(e), "status": "error"})


if __name__ == "__main__":
    app.run(debug=True)
