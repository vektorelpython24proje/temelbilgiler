import pymongo

client = pymongo.MongoClient("mongodb://vektorelpython24:djKwpQpazjUiiUDT@cluster0-shard-00-00.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-01.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-02.3fkyr.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
veritabaniYeni = client["deneme"]

isim =input("isim:")
soyisim=input("soyisim:")
no=input("numara")
liste=["isim","soyisim","numara"]
sozluk = {}
sozluk.update(*zip(liste,[isim,soyisim,numara]))
print(*zip(liste))
collectionYeni=veritabaniYeni["koleksiyon"]
x = collectionYeni.insert_one(sozluk)
print("kayıt",x.inserted_id," id gelmiş hoşgelmiş")

sorgu = {"isim":{"$gt":"A"}}
x = collectionYeni.find(sorgu)
print(*x)
sorguRex = {"isim":{"$regex":"^A"}}
x = collectionYeni.find(sorgu)
print(*x)