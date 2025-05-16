from flask import Flask, render_template, request, redirect, flash, send_from_directory
from flask_mysqldb import MySQL

app = Flask(__name__,
    static_folder="",  
    template_folder=""  
)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 's@chand'
app.config['MYSQL_DB'] = 'project'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog-single')
def blog_single():
    return render_template('blog-single.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portfolio-details')
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/success')
def success():
    return render_template('success.html')


@app.route("/css/<path:filename>")
def serve_css(filename):
    return send_from_directory("css", filename)

@app.route("/js/<path:filename>")
def serve_js(filename):
    return send_from_directory("js", filename)

@app.route("/img/<path:filename>")
def serve_images(filename):
    return send_from_directory("img", filename)

@app.route("/fonts/<path:filename>")
def serve_fonts(filename):
    return send_from_directory("fonts", filename)

@app.route("/mail/<path:filename>")
def serve_mail_files(filename):
    return send_from_directory("mail", filename)



@app.route('/testing', methods=['GET', 'POST'])
def appointment():
    if request.method == "POST":
        details = request.form
        print(details)
        Name = details['name']
        Email = details['email']
        Phone = details['phone']
        Dept = details['department']
        Doc = details['doctor']
        App_date = details['date']
        Desc = details['message']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO appointments(name, email_id, phone, department, doctor, appointment_date, description) VALUES (%s, %s, %s, %s, %s, %s, %s)", (Name, Email, Phone, Dept, Doc, App_date, Desc))
        mysql.connection.commit()
        cur.close() 

        return redirect('/testing')
        
    return render_template('testing.html')
    


if __name__ == '__main__':
    app.run()