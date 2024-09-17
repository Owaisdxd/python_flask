#pip intall flask

from flask import Flask

app=Flask(__name__)
app.config['MYSQL_HOST']='HOSTNAME'                            #Please provide the hostname
app.config['MYSQL_HOST']='USERNAME'                            #Please provide the database username
app.config['MYSQL_PASSWORD']='DATABASE PASSWD'                 #Please provide the database username password
app.config['MYSQL_DB']='DATABASE NAME'                         #Please provide the database name
mysql=MySQL(app)                                               #Connecting the database to website
home="Welcome To My Web Page"
@app.route("/")                                                #you can use route instead of get it will work the same
def home_one():
    return home

contact="Phone Numer\tPhone Number,\nEmail myemail@mail.com"  #
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

@app.route("/tariner_create",methods=["POST","GET"])
def trainer_create():
    if request.method=="POST":
        fname_data=request.form['fname']
        lname_data=request.form['lname']
        design_data=request.form['design']
        course_data=request.form['course']
        cdate_data=data.today()
    







if __name__ == "__main__":  #if you want to run using ide
    app.run(debug=True,host='192.168.0.225',port=9000)

# if you want to run using terminal  no need of if __name__ run this on terminal flask run by specifeing the host and port if needed
#debug=True will change value the real time you do not need to rerun the file
#port is provided if you want to run this on specific port
