from pymongo import MongoClient
import Connection
import json

class DB:
    def __init__(self):
        self.collection = MongoClient().local.connections

    def REMOVEALL(self):
        self.collection.delete_many({})

    def remove(self, connection, field):
        if("ip" in field):
            self.collection.delete_many({"ip": connection.ip})
        elif("hostname" in field):
            self.collection.delete_many({"hostname": connection.hostname})
        else:
            return False
        return True

    def insert(self, connection):
        data = json.dumps(connection.socket, -1)
        self.collection.insert_one({
            "ip": connection.ip,
            "hostname": connection.hostname,
            "uniq": str(connection.unique)
        })

    def getAllConnectionsPrint(self):
        darr = []
        docs = self.collection.find()
        for doc in docs:
            darr.append(doc)
        return darr

    def getCollection(self):
        return self.collection