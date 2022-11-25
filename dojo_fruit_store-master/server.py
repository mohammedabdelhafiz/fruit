from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    name = request.form['first_name']
    last = request.form ['last_name']
    num = request.form['student_id']
    strawberry = request.form['strawberry']
    apple = request.form['apple']
    raspberry = request.form['raspberry']
    result = int(strawberry) + int(apple) + int(raspberry)

    return render_template("checkout.html" , user= name , last = last , num = num , strawberry = strawberry , apple=apple, raspberry=raspberry , result=result )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    


# we made refresh on the page but nothing happened