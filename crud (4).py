from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:45358' % (username, password))
        # where xxxxx is your port number
        self.database = self.client['AAC']

    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary  
            return True          
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, data):
        if data is not None:

            #returns cursor
            #x = self.database.animals.find(data)
            x = self.database.animals.find(data, {"_id":False})
            #print(x)

            #returns result (old method)
            #cur = self.database.animals.find_one(data)
            #print(cur)

            return x
        else:
            raise Exception("Nothing to read, because data parameter is empty")

    def update(self, query, newValue):
        if query is not None: # make sure query is in db
            
            self.database.animals.update_one(query, newValue) # read the data
             
        else:
            raise Exception("Nothing to update, because query parameter is empty")

    def delete(self, data):
        if data is not None:
            self.database.animals.delete_one(data) # delete the data
            #print(x)
            return True
        else:
            raise Exception("Nothing to delete, because data parameter is empty")