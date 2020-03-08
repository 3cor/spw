import pymongo

def connect():
    client = pymongo.MongoClient(
        "mongodb+srv://corgi:TIZnBqHEHh0VTtWI@cluster0-7jdrj.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('spw')
    return db


def print_all(docs):
    for i, document in enumerate(docs):
        print('[{}]'.format(i + 1))
        for key, value in document.items():
            print('{}: {}'.format(key, value))


def find(db):
    docs = db.users.find()
    print_all(docs)

if __name__ == '__main__':
    database = connect()
    find(database)
