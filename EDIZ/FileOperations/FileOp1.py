from Tools import DosyaTool
bankaDefter = DosyaTool(r"EDIZ\ORNEKOOP\banka",alanlar=["Banka","Hesap","Tutar"])
bankaDefter.menu()

telefonDefter = DosyaTool(r"EDIZ\ORNEKOOP\defter",alanlar=["Adı","Soyadı","Tel"])
telefonDefter.menu()
