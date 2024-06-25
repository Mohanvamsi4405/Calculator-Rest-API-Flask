from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def test():
    return render_template("index.html")

@app.route('/math',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        op=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if(op=='add'):
            sum=num1+num2
            result='The Sum of '+str(num1) +' and '+str(num2) +' is '+str(sum)

    

        elif(op=='subtract'):
            sub=num1-num2
            result='The Subtraction of '+str(num1) +' and '+str(num2) +' is '+str(sub)

        elif(op=='multiply'):
            mul=int(num1*num2)
            result='The Mutiplication of '+str(num1) +' and '+str(num2) +' is '+str(mul)
    
    
        elif(op=='divide'):
            div=num1/num2
            result='The Divison of '+str(num1) +' and '+str(num2) +' is '+str(div)
    
    
        elif(op=='modulo'):
            mod=num1%num2
            result='The Modulo of '+str(num1) +' and '+str(num2) +' is '+str(mod)

        
        return render_template('results.html',result=result)
















@app.route('/postman_data',methods=['POST'])
def math_operation1():
    if(request.method=='POST'):
        op=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        if(op=='add'):
            sum=num1+num2
            result='The Sum of '+str(num1) +' and '+str(num2) +' is '+str(sum)

        elif(op=='subtract'):
            sub=num1-num2
            result='The Subtraction of '+str(num1) +' and '+str(num2) +' is '+str(sub)

        elif(op=='multiply'):
            mul=int(num1*num2)
            result='The Mutiplication of '+str(num1) +' and '+str(num2) +' is '+str(mul)
    
    
        elif(op=='divide'):
            div=num1/num2
            result='The Divison of '+str(num1) +' and '+str(num2) +' is '+str(div)
    
    
        elif(op=='modulo'):
            mod=num1%num2
            result='The Modulo of '+str(num1) +' and '+str(num2) +' is '+str(mod)

        
        return jsonify(result)
if __name__=="__main__":
    app.run(host="0.0.0.0")





























# @app.route("/hello_world1")
# def hello_world():
#     return "<h1>Hello, World1 Mohan</h1>"

# @app.route("/hello_world2")
# def hello_world2():
#     return "<h1>Hello, World2 Vamsi</h1>"

# @app.route("/hello_world3")
# def hello_world3():
#     return "<h1>Hello, World3 Chitrada Mohan Vamsi</h1>"
# @app.route("/test")
# def test():
#     return "This is My test function"

# @app.route("/test1")
# def test1():
#     return "This is My test function"

# @app.route("/test2")
# def test2():
#     a=10+5
#     return "This is My test function {}".format(a)

# @app.route("/userinput")
# def test3():
#     data=request.args.get("x")

#     return "The input x value is {}".format(data)









