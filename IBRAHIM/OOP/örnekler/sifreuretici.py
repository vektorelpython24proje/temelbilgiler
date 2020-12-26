# xsifre=input("Şifre Giriniz: ")
# class SifreUretimi():
#     def __init__(self,var1,var2):
#         self.var1=var1
#         self.var2=var2
#         self.xsifre=xsifre

#     def ContMechanism(self,sifre):
#         k=bharf = kharf = nchar = num = False
#         ncharList=(""" -_,;.:!'^+%&/()=?><#$½{[]}|*\æß@€~¨`""")
#         if len(sifre)>=8:
#             for item in sifre:
#                 if item.isupper():
#                     bharf=True
#                 elif item.islower():
#                     kharf=True
#                 elif item.isnum():
#                     num=True
#                 elif item in ncharList:
#                     nchar=True
#             if k:
#                 print("Duru sifre1")
#             else:
#                 print("Bidaha Yaz")


# obj1=SifreUretimi.ContMechanism(xsifre)
# obj1(xsifre)