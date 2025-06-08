from pymongo import MongoClient

def ambil_data_dari_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['transaction_db']
    transaksi = db['data_transaction']

    hasil = []
    for doc in transaksi.find():
        doc["sumber"] = "MongoDB"
        hasil.append(doc)

    return hasil