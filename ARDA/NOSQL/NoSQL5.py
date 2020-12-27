import pymongo
from collections import Counter
client = pymongo.MongoClient("mongodb://vektorelpython24:djKwpQpazjUiiUDT@cluster0-shard-00-00.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-01.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-02.3fkyr.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
veritabaniYeni = client["deneme"]
collectionYeni = veritabaniYeni["koleksiyon"]

# sorgu = {"isim":"ibrahim"}
# print("sonuc1",collectionYeni.find(sorgu).count())
# x = collectionYeni.delete_one(sorgu)
# print("sonuc2",collectionYeni.find(sorgu).count())
# print("sonuc3",x.deleted_count)

# sorgu = {"isim":"Deneme1"}
# x=collectionYeni.find(sorgu)
# x = collectionYeni.delete_many(sorgu)
# print(x.deleted_count)

# sorgu = {}
# x=collectionYeni.find(sorgu)
# x = collectionYeni.delete_many(sorgu)
# print(x.deleted_count)


