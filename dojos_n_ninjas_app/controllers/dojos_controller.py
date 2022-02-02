from flask import redirect, render_template, request, flash, session
from dojos_n_ninjas_app import app
from dojos_n_ninjas_app.models.dojos_model import Dojo

@app.route('/', methods=["GET"])
def home():
    return redirect('/dojos')

@app.route('/dojos', methods=["GET", "POST"])
def handleDojos():
    if request.method == "GET":
        dojosList = Dojo.getDojos()
        return render_template("dojo.html", dojos=dojosList)

@app.route('/dojo/add', methods=["POST"])
def addDojoNew():
    newDojo = {
        "name" : request.form["name"],
    }
    result = Dojo.addDojo(newDojo)
    if type(result) is not int:
        flash("There was a problem registering the new dojo, please try again", "adddojonew")
    return redirect('/dojos')

@app.route('/dojo/<id>', methods=["GET"])
def showDojo(id):
    dojo = {
        "id" : int(id)
    }
    dojoWithNinjasList = Dojo.getDojoWithNinjas(dojo)
    print(dojoWithNinjasList)
    print(type(dojoWithNinjasList))
    return render_template("dojoshow.html", dojoWithNinjas=dojoWithNinjasList)