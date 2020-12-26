# vektorelpython24

# djKwpQpazjUiiUDT

import pymongo
client = pymongo.MongoClient("mongodb://vektorelpython24:djKwpQpazjUiiUDT@cluster0-shard-00-00.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-01.3fkyr.gcp.mongodb.net:27017,cluster0-shard-00-02.3fkyr.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
veritabaniYeni = client["deneme"]
collectionYeni = veritabaniYeni["koleksiyon"]
liste =[{"isim":"İbrahim","soyisim":"EDIZ","adres":"KEÇİÖREN","tel":123},
{"isim":"Şakir","soyisim":"KAYADAN","adres":"GÖLBAŞI","tel":123},
{"isim":"Arda","soyisim":"GÖRE","adres":"YENİMAHALLE","tel":123},
{"isim":"ibrahim","soyisim":"koç","adres":"dünya","tel":123},
{"isim":"Sema","soyisim":"BULUT","adres":"GÖLBAŞI","tel":123},
{"isim":"FİKRİYE","soyisim":"İlik","adres":"SİLİFKE","tel":123}]
x = collectionYeni.insert_many(liste)
print(x.inserted_ids)

# veritabanim = client["sample_mflix"]
print(client.list_database_names())
print(veritabaniYeni.list_collection_names())