from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):  
    ID = db.Column(db.Integer, primary_key=True) 
    Station_Name = db.Column(db.String(500), nullable=False)
    Line = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Station {self.Station_Name}, Line {self.Line}>"



@app.route("/")
def main():
    
    stations = Data.query.all()
    return render_template("index.html", stations=stations)

@app.route("/cost",methods=["POST","GET"])
def cost_cal():

    if request.method=="POST":
        selected_source = request.form.get('source')
        selected_destination = request.form.get('destination')




# Run the app
if __name__ == "__main__":
    app.run(debug=True)
