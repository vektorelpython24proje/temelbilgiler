import pymongo

client = pymongo.MongoClient("mongodb://vektorelpython24:djKwpQpazjUiiUDT@cluster0-shard-00-00.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-01.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-02.3fkyr.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
veritabaniYeni = client["deneme"]

isim = input("İsminizi Giriniz:")
soyisim = input("Soyisminizi Giriniz")
numara = int(input("Numaranızı Giriniz"))
liste = ["isim","soyisim","numara"]
sozluk = {}
sozluk.update(zip(liste,[isim,soyisim,numara]))
collectionYeni = veritabaniYeni["koleksiyon"]
x = collectionYeni.insert_one(sozluk)
print("Kayıt",x.inserted_id," id sistemde yerini aldı")

sorgu = {"isim":{"$gt":"A"}}

x = collectionYeni.find({"isim":{"like":"%A%"}})

for item in x:
    print(item)