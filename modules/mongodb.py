import pymongo

def connect():
    client = pymongo.MongoClient(
        "mongodb+srv://admin:264135@cluster0-stxg5.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('spw')
    return db


def print_all(docs):
    for i, document in enumerate(docs):
        print('[{}]'.format(i + 1))
        for key, value in document.items():
            print('{}: {}'.format(key, value))

def findall(db, user):
    query = {'owner': str(user)}
    docs = db.data.find(query)
    # print_all(docs)
    return docs

def get_user(db, usr, pwd):
    query = {'$and' : [{'user': usr}, {'pass': pwd}]}

    docs = db.users.count_documents(query)
    return docs

def add_user(db, usr, pwd):
    mycol = db['users']
    payload = {
        'user': usr,
        'pass': pwd
    }
    return mycol.insert_one(payload)

def add_entry(db, user, entry):
    mycol = db['data']
    return mycol.insert_one(entry)

def edit_entry(db, user, row, entry):
    mycol = db['data']

    query = {'$and' : [{'owner': user}, {'name': row}]}

    update = { '$set': {
        'name': entry['name'],
        'user': entry['user'],
        'pass': entry['pass'],
        'url': entry['url']
        }}

    mycol.update_one(query, update)

def delete_entry(db, user, row):
    mycol = db['data']

    query = {'$and' : [{'owner': user}, {'name': row}]}

    mycol.delete_many(query)

def purge(db):
    query = {}
    result = db.users.delete_many(query)
    print('Purged collection!\nDeleted: {} rows'.format(result.deleted_count))

if __name__ == '__main__':
    database = connect()
    findall(database, 'test')
