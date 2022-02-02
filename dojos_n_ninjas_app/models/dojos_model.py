from dojos_n_ninjas_app.config.mysqlconnection import connectToMySQL
from dojos_n_ninjas_app.models.ninjas_model import Ninja

class Dojo:
    def __init__(self, id, name, created_at, updated_at):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.ninjas = []
    
    def addNinja(self, ninja):
        self.ninjas.append(ninja)
    
    @classmethod
    def getDojos(cls):
        query = "SELECT * FROM dojos;"
        queryResult = connectToMySQL("dojos_n_ninjas_schema").query_db(query)
        dojosList = []
        for dojo in queryResult:
            dojosList.append(Dojo(dojo["id"], dojo["name"], dojo["created_at"], dojo["updated_at"]))
        return dojosList
    
    @classmethod
    def getDojosWithNinjas(cls):
        query = "SELECT d.id, d.name, d.created_at, d.updated_at, n.id AS n_id, n.first_name, n.last_name, n.age, n.dojo_id, n.created_at AS n_created_at, n.updated_at AS n_updated_at FROM dojos d LEFT JOIN ninjas n ON d.id = n.dojo_id;"
        queryResult = connectToMySQL("dojos_n_ninjas_schema").query_db(query)
        dojosWithNinjasList = []
        for row in queryResult:
            index = isDojoInList(row["id"], dojosWithNinjasList)
            if index == -1:
                dojoToAdd = Dojo(row["id"], row["name"], row["created_at"], row["updated_at"])
                dojoToAdd.addNinja(Ninja(row["n_id"], row["first_name"], row["last_name"], row["age"], row["dojo_id"], row["n_created_at"], row["n_updated_at"]))
                dojosWithNinjasList.append(dojoToAdd)
            else:
                dojosWithNinjasList[index].addNinja(Ninja(row["n_id"], row["first_name"], row["last_name"], row["age"], row["dojo_id"], row["n_created_at"], row["n_updated_at"]))
        return dojosWithNinjasList
    
    @classmethod
    def getDojoWithNinjas(cls, dojo):
        query = "SELECT d.id, d.name, d.created_at, d.updated_at, n.id AS n_id, n.first_name, n.last_name, n.age, n.dojo_id, n.created_at AS n_created_at, n.updated_at AS n_updated_at FROM dojos d LEFT JOIN ninjas n ON d.id = n.dojo_id WHERE d.id = %(id)s;"
        queryResult = connectToMySQL("dojos_n_ninjas_schema").query_db(query, dojo)
        dojoWithNinjas = Dojo(queryResult[0]["id"], queryResult[0]["name"], queryResult[0]["created_at"], queryResult[0]["updated_at"])
        for row in queryResult:
            dojoWithNinjas.addNinja(Ninja(row["n_id"], row["first_name"], row["last_name"], row["age"], row["dojo_id"], row["n_created_at"], row["n_updated_at"]))
        return dojoWithNinjas
    
    @classmethod
    def addDojo(cls, newDojo):
        query = "INSERT INTO dojos(name) VALUES(%(name)s);"
        queryResult = connectToMySQL("dojos_n_ninjas_schema").query_db(query, newDojo)
        return queryResult

def isDojoInList(dojoId, listOfDojos):
    for i in range(len(listOfDojos)):
        if listOfDojos[i].id == dojoId:
            return i
    return -1