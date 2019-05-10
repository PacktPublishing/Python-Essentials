class Defaults:
    mongo_uri = "mongodb://localhost:27017"
    some_param = "xyz"

class Dev(Defaults):
    mongo_uri = "mongodb://sandbox:27017"

class QA(Defaults):
    mongo_uri = "mongodb://username:password@qa02:27017/?authMechanism=PLAIN&amp;authSource=$external"