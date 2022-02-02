from flask import flash, redirect, render_template, request, session
from dojos_n_ninjas_app import app
from dojos_n_ninjas_app.models.dojos_model import Dojo
from dojos_n_ninjas_app.models.ninjas_model import Ninja

@app.route('/ninjas', methods=["GET", "POST"])
def handleNinjas():
    if request.method == "GET":
        dojosList = Dojo.getDojos()
        return render_template("ninja.html", dojos=dojosList)
    elif request.method == "POST":
        newNinja = {
            "first_name" : request.form["firstname"],
            "last_name" : request.form["lastname"],
            "age" : int(request.form["age"]),
            "dojo_id" : int(request.form["dojoid"]),
        }
        result = Ninja.addNinja(newNinja)
        if type(result) is int:
            return redirect('/dojo/' + str(newNinja["dojo_id"]))
        else:
            flash("There was a problem registering the new ninja, please try again", "addninjanew")
            return redirect('/ninjas')

# @app.route('/ninja/add', methods=["GET", "POST"])
# def 