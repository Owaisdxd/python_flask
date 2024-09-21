#pip intall flask
"""
All the page are settedup in HTML and only linkings of the pages and logic is being implemented in this file 
"""
from flask import Flask

app=Flask(__name__)
app.config['MYSQL_HOST']='HOSTNAME'                            #Please provide the hostname(can be ip) 
app.config['MYSQL_USER']='USERNAME'                            #Please provide the database username db
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
    if request.method=="POST":                                #defining method wheather we request ("GET") or give ("POST") data
        fname_data=request.form['fname']                      #fname will be first name
        lname_data=request.form['lname']                      #lname will be last name
        design_data=request.form['design']                    #design will be designation
        course_data=request.form['course']                    #course will be course name
        cdate_data=data.today()                               #time when we are adding the data
        sql="INSERT INTO 'data base name' (fname,lname,design,course,datetime) VALUES (%s,%s,%s,%s,%s)"  #writing the query to sql database to insert the data
        val=(fname_data,lname_data,design_data,course_data,cdate_data)                                   #values that will be added
        cursor=mysql.connection.cursor()                      #creating the cursor
        cursor.execute(sql,val)                               #executing the cursor
        mysql.connection.commit()                             #saving the data 
        cursor.close()                                        #closing datanbase 
        return render_template("success.html")                #Getting to the success page
        

@app.route("/trainer_filter",methods=["POST","GET"])         #Adding Searching capabilities as per the course  
def trainer_filter():
    if request.method=="POST":
        course_name=request.form['course']                   #course is defined in the html file 
        if course_name=='All':                               #All is used to show all the data 
            sql = f"select * from trainer_details"           
            cursor = mysql.connection.cursor()
            cursor.execute(sql)
            row = cursor.fetchall()
        else:                                               #It will show only those asked by user 
            sql=f"select * from trainer_details where course='{course_name}'"
            cursor=mysql.connection.cursor()
            cursor.execute(sql)
            row = cursor.fetchall()
        return render_template("sample.html",output_data=row)
@app.route("/database",methods=["POST","GET"])
def database():
    cursor=mysql.connection.cursor()
    sql="select * from trainer_details"
    cursor.execute(sql)
    row=cursor.fetchall()
    return render_template("sample.html",output_data=row)
@app.route("/database",methods=["POST","GET"])                #we are defining the method here to interact with database 
def database():                                               
    cursor=mysql.connection.cursor()                           #creating the cursor 
    sql="select * from trainer_details"                        #writing the query to sql database to insert the data
    cursor.execute(sql)                                        #executing the query
    row=cursor.fetchall()                                      #fetching data
    return render_template("trainer_details_fetch.html",output_data=row)  #trainer_details_fetch.html is the html page where database values will be displayed
if __name__ == "__main__":  #if you want to run using ide
    app.run(debug=True,host='192.168.0.225',port=9000)

# if you want to run using terminal  no need of if __name__ run this on terminal flask run by specifeing the host and port if needed
#debug=True will change value the real time you do not need to rerun the file
#port is provided if you want to run this on specific port
