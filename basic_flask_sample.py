#pip intall flask

from flask import Flask

app=Flask(__name__)

home="Welcome To My Web Page"
@app.route("/")          #you can use route instead of get it will work the same
def home_one():
    return home

contact="Phone Numer\tPhone Number,\nEmail myemail@mail.com"
@app.get("/cont")
def contact_me():
    return contact

ser="How may I help you"
@app.get("/serve")
def service():
    return ser

@app.route("/trainer")   
def trainer():
    return render_template("trainer_details.html") 
    #render_template is used to direct the html file 
    #HTML file should be in a directory/folder called template







if __name__ == "__main__":  #if you want to run using ide
    app.run(debug=True,host='192.168.0.225',port=9000)

# if you want to run using terminal  no need of if __name__ run this on terminal flask run by specifeing the host and port if needed
#debug=True will change value the real time you do not need to rerun the file
#port is provided if you want to run this on specific port
