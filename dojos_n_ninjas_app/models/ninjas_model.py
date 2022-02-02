from dojos_n_ninjas_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, id, first_name, last_name, age, dojo_id, created_at, updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dojo_id = dojo_id
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def getNinjas(cls):
        query = "SELECT * FROM ninjas;"
        queryResult = connectToMySQL("dojos_n_ninjas_schema").query_db(query)
        ninjasList = []
        for ninja in queryResult:
            ninjasList.append(Ninja(ninja["id"], ninja["first_name"], ninja["last_name"], ninja["age"], ninja["dojo_id"], ninja["created_at"], ninja["updated_at"]))
        return ninjasList

    @classmethod
    def addNinja(cls, newNinja):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        queryResult = connectToMySQL("dojos_n_ninjas_schema").query_db(query, newNinja)
        return queryResult

    