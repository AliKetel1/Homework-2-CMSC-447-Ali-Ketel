from flask import Flask, render_template,request,redirect
from models import db,UserName

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MDOFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/newuser', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('newuser.html')
    
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_points = request.form['user_points']
        user_name = request.form['user_name']

        users = UserName(
            user_id = user_id,
            user_name = user_name,
            user_points = user_points
        )
        db.session.add(users)
        db.session.commit()
        return redirect('/')
     
@app.route('/', methods = ['GET'])
def PasteList():
    Users = UserName.query.all()
    return render_template('index.html',Users = Users)

app.run(debug=True)
    