import pymongo
from collections import Counter
client = pymongo.MongoClient("mongodb://vektorelpython24:djKwpQpazjUiiUDT@cluster0-shard-00-00.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-01.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-02.3fkyr.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
veritabaniYeni = client["deneme"]
collectionYeni = veritabaniYeni["koleksiyon"]

sorgu = {"isim":"İbrahim"}
x = collectionYeni.find(sorgu,{"_id":0,"isim":1})
guncelle = {"$set":{"isim":"ibrahim"}}
x=collectionYeni.update_many(sorgu,guncelle)
print(x.modified_count)
sorgu = {"isim":"ibrahim"}
x = collectionYeni.find(sorgu,{"_id":0,"isim":1})
print(*x)
