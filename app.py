from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)
print(os.getenv("PORT"))
port = int(os.getenv("PORT", 5000))

f=open('assign1.json',"r+")
data =json.load(f)

@app.route('/')
def home():
   return render_template('home.html')



@app.route('/list',methods=['POST','GET'])
def list():
    value = str(request.form['values'])
    val1 = str(request.form['value1'])
    print(value)
    array1=[]
    if(value=="name"):
        for i in data:
            array2=[]
            if(i==val1):
                array2.append(i)
                array2.append(data[i]['Picture'])
                array1.append(array2)
            else:
                pass
        print(array1)
        return render_template("list1.html",rows = array1)
    elif(value=="state"):
        
        for i in data:
            array2=[]
            if(data[i]['State']==val1):
                array2.append(i)
                array2.append(data[i]['State'])
                array2.append(data[i]['Salary'])
                array2.append(data[i]['Grade'])
                array2.append(data[i]['Room'])
                array2.append(data[i]['Telnum'])
                array2.append(data[i]['Picture'])
                array2.append(data[i]['Keywords'])
                array1.append(array2)

    elif(value=="room"):
        
        for i in data:
            array2=[]
            if(data[i]['Room']==int(val1)):
                array2.append(i)
                array2.append(data[i]['State'])
                array2.append(data[i]['Salary'])
                array2.append(data[i]['Grade'])
                array2.append(data[i]['Room'])
                array2.append(data[i]['Telnum'])
                array2.append(data[i]['Picture'])
                array2.append(data[i]['Keywords'])
                array1.append(array2)
    print (array1)
    return render_template("list.html",rows = array1)

@app.route('/list1',methods=['POST','GET'])
def list1():
    valuenum = str(request.form['valuesNum'])
    valuenum1 = int(request.form['valuenum1'])
    valuenum2 = int(request.form['valuenum2'])
    print(valuenum)
    array1=[]
    if(valuenum=="grade"):
        for i in data:
            array2=[]
            print(type(data[i]['Grade']),type(int(valuenum2)))
            if(data[i]['Grade']!="" and data[i]['Grade']<int(valuenum2) and data[i]['Grade']>int(valuenum1)):
                array2.append(i)
                array2.append(data[i]['State'])
                array2.append(data[i]['Salary'])
                array2.append(data[i]['Grade'])
                array2.append(data[i]['Room'])
                array2.append(data[i]['Telnum'])
                array2.append(data[i]['Picture'])
                array2.append(data[i]['Keywords'])
                array1.append(array2)

        return render_template("list.html",rows = array1)
    elif(valuenum=="salary"):
        for i in data:
            array2=[]
            if(data[i]['Salary']!="" and data[i]['Salary']<int(valuenum2) and data[i]['Salary']>int(valuenum1)):
                array2.append(data[i]['Picture'])

                array1.append(array2)
    return render_template("list2.html",rows = array1)


@app.route('/deleterecord', methods=['POST','GET'])
def deleterecord():
    value = request.form['valuesDEL']
    val1 = request.form['valueDEL']
    if(value=="nameDEL"):
        #querry = "DELETE FROM people where Name='"+val1+"' "
        for i in data.copy():
            if(i==val1):
                del data[i]
    if(value=="stateDEL"):
        for i in data:
            if(data[i]['State']==val1):
                del data[i]
    if(value=="roomDEL"):
        for i in data:
            if(data[i]['Room']==val1):
                del data[i]
    array1=[]
    for i in data.copy():
        array2=[]
        array2.append(i)
        array2.append(data[i]['State'])
        array2.append(data[i]['Salary'])
        array2.append(data[i]['Grade'])
        array2.append(data[i]['Room'])
        array2.append(data[i]['Telnum'])
        array2.append(data[i]['Picture'])
        array2.append(data[i]['Keywords'])
        array1.append(array2)
    return render_template('list.html',rows=array1)


@app.route('/update',methods=['POST','GET'])
def update():
    value1 = str(request.form['valueADD1'])
    value2 = str(request.form['valueADD2'])
    value3 = str(request.form['valuesADD2'])
    if(value3=="stateADD2"):
        for i in data:
            if(i==value1):
                data[i]['State']=value2
    if(value3=="keywordADD2"):
        
        for i in data:
            if(i==value1):
                data[i]['Keywords']=value2
    if(value3=="roomADD2"):
        for i in data:
            if(i==value1):
                data[i]['Room']=int(value2)
    if(value3=="gradeADD2"):
       
        for i in data:
            if(i==value1):
                data[i]['Grade']=int(value2)
    if(value3=="imageADD2"):
        
        for i in data:
            if(i==value1):
                data[i]['Picture']=value2
   
    array1=[]
    for i in data.copy():
        array2=[]
        array2.append(i)
        array2.append(data[i]['State'])
        array2.append(data[i]['Salary'])
        array2.append(data[i]['Grade'])
        array2.append(data[i]['Room'])
        array2.append(data[i]['Telnum'])
        array2.append(data[i]['Picture'])
        array2.append(data[i]['Keywords'])
        array1.append(array2)	
    return render_template('list.html',rows=array1)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)