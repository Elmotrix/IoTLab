import pymongo;
from datetime import datetime

dbConString = "mongodb+srv://MyUser:9R5w7qEZPFFrZ7@mycluster.n4ynydx.mongodb.net/?retryWrites=true&w=majority";
client = pymongo.MongoClient(dbConString)
database = client["Lab2"]
collection = database["Temperature"]
def MongoPrint(value):
    now = datetime.now();
    datetimeformat = "%Y-%m-%d %H:%M:%S";
    MeasurementDateTime = now.strftime(datetimeformat);
    document = { "MeasurementValue": value, "MeasurementDateTime": MeasurementDateTime };
    x = collection.insert_one(document);