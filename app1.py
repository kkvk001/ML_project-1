## integrate HTML with Flask
## HTTP verb GET And POST

from flask import Flask,redirect,url_for,render_template

app=Flask(__name__)

@app.route("/youtube/")
def welcome():
    return render_template("index.html")



@app.route('/success/<int:score>')
def success(score):
    return 'the person has passed and the marks is' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'the person has fail and the marks is' + str(score)

##result checker
@app.route('/results/<int:marks>')
def result(marks):
    result=''
    if marks<50:
        result='fail'
    else:
        result='pass'
    return redirect(url_for(result,score=marks))


if __name__=="__main__":
    app.run(debug=True)
