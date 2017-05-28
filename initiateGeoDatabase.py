import csv
from pymongo import MongoClient

documentCounter=0

# Load city-zipcode-location csv to memory
print("Loading CSV file...")
with open('data/zipcode-database-Primary.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    city_list = list(reader)
print("successfully loaded "+ str(len(city_list))+" rows from CSV file.\n")

print("Connecting to MongoDB...")
# MongoDB connection
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.gTerminal
db.cities.drop()
citiesCollection = db.cities

print("Inserting records... DB:gTerminal  Collection:cities")
# For each row
for index in range(len(city_list)):
    if(index==0):
        header=city_list[index]
    else:
        if(len(city_list[index])>1):
            document={}
            for hid in range(len(header)):
                if city_list[index][hid]:
                    document[header[hid]]=city_list[index][hid]
            # print("Inserting: "str(document))
            citiesCollection.insert_one(document)
            documentCounter=documentCounter+1
            if documentCounter%10000==0:
                print("Have loaded " + str(documentCounter) +" records...")

print("Total inserted records:" + str(documentCounter))
