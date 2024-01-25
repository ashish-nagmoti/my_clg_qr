from flask import Flask, render_template, request
import random
app = Flask(__name__)
name = None
roll = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global name, roll
    
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        return render_template('que.html')
    
    return render_template('index.html')

num1 = random.randint(1,4)
num2 = random.randint(1,4)
num3 = random.randint(1,4)
num4 = random.randint(1,4)
num5 = random.randint(1,4)
per= random.randint(60,100)
mark= random.randint(200,600)
@app.route("/web", methods=['GET', 'POST'])
def web():
    if request.method == 'POST':
        return render_template("web.html", name=name, roll=roll,x1=num1,x2=num2,x3=num3,x4=num4,x5=num5,per=per,marks=mark)    
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
