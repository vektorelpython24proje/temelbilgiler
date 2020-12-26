

import pymongo
client = pymongo.MongoClient("mongodb://vektorelpython24:djKwpQpazjUiiUDT@cluster0-shard-00-00.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-01.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-02.3fkyr.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
veritabaniYeni = client["deneme"]
# veritabaniYeni=client{"deneme"}
collectionYeni= veritabaniYeni["koleksiyon"]
sozluk={"isim":"ibrahim","soyisim":"koç","adres":"dünya"}
x = collectionYeni.insert_one(sozluk)
print(x.inserted_id
)
# veritabanim = client["sample_mflix"]
print(client.list_database_names())
print(veritabaniYeni.list_collection_names())