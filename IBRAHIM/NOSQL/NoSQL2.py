# # Find One

# import pymongo
# client = pymongo.MongoClient("mongodb://vektorelpython24:djKwpQpazjUiiUDT@cluster0-shard-00-00.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-01.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-02.3fkyr.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
# veritabaniYeni = client["deneme"]
# collectionYeni = veritabaniYeni["koleksiyon"]
# x = collectionYeni.find_one()
# print(x)


# # Find All

# import pymongo
# client = pymongo.MongoClient("mongodb://vektorelpython24:djKwpQpazjUiiUDT@cluster0-shard-00-00.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-01.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-02.3fkyr.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
# veritabaniYeni = client["deneme"]
# collectionYeni = veritabaniYeni["koleksiyon"]
# x = collectionYeni.find()
# for item in x:
#     print(item)
#istenilen için 1 tam tersi 0
# ŞART YAZIMI

import pymongo
client = pymongo.MongoClient("mongodb://vektorelpython24:djKwpQpazjUiiUDT@cluster0-shard-00-00.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-01.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-02.3fkyr.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
veritabaniYeni = client["deneme"]
collectionYeni = veritabaniYeni["koleksiyon"]
x = collectionYeni..find({},{"_id":0,"isim":1,"soyisim":1})

y = collectionYeni.find({},{"_id":0,"adres":0})
for item in x:
    print("1",item)
for item in y:
    print("2",item)


#sonuçları filtrelemek
sorgu = {"isim":"ibrahim","adres":"dünya"}
z = collectionYeni.find(sorgu)

for item in z:
    print("3",item)