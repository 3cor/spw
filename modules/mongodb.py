import pymongo

def make_conn():
    client = pymongo.MongoClient(
        "mongodb+srv://corgi:264135@cluster0-stxg5.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('Practice')
    return db


def print_all(docs):
    for i, document in enumerate(docs):
        print('[{}]'.format(i + 1))
        for key, value in document.items():
            print('{}: {}'.format(key, value))


def ls(database):
    pass


if __name__ == '__main__':
    database = make_conn()
    ls(database)
