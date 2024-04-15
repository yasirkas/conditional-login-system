print("*** Kullanıcı Giriş Sistemi ***\n")
print("KURALLAR:")
print("● Kullanıcı adınız en fazla 16 karakter uzunluğunda olmalı, sadece rakam ve büyük-küçük harflerden oluşmalıdır.")
print("● Şifreniz en az 8 en fazla 24 karakter uzunluğunda olmalı.")
print("● Şifreniz en az bir büyük harf, en az bir tane küçük karakter en az bir rakam ve en az bir de özel işaretlerden oluşmalıdır.\n")
print("-> Kayıt Olma Paneli <-")

kucukharf = "qwertyuıopğüasdfghjklşizxcvbnmöç"
buyukharf = "QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ"
sayi = "0123456789"
onay1 = 0
onay2 = 0
i = 0
f = 0
g = 0
h = 0
byk = 0
kck = 0
kharf = 0
bharf = 0

while True:
    kullaniciadi = input("\nKullanıcı adı giriniz:")
    sifre = input("Şifre giriniz:")

    if len(kullaniciadi) < 16:

        if kullaniciadi.isalnum():

            if kullaniciadi.isalpha():
                if kullaniciadi.islower():
                    print("Kullanıcı adınızda rakam ve büyük harf de olmalı!")
                    continue

                elif kullaniciadi.isupper():
                    print("Kullanıcı adınızda rakam ve küçük harf de olmalı!")
                    continue
                else:
                    print("Kullanıcı adınızda rakam da olmalı!")
                    continue

            elif kullaniciadi.isnumeric():
                print("Kullanıcı adınızda en az bir küçük ve en az bir büyük harf olmalı!")
                continue

            else:
                for x in kullaniciadi:
                    for y in x:
                        if y in buyukharf:
                            byk += 1

                for n in kullaniciadi:
                    for m in n:
                        if m in kucukharf:
                            kck += 1

                if kck < 1 and byk > 0:
                    print("Kullanıcı adınızda küçük harf de olmalı!")
                    continue
                elif kck > 0 and byk < 1:
                    print("Kullanıcı adınızda büyük harf de olmalı!")
                    continue
                elif kck > 0 and byk > 0:
                    print("Kullanıcı adı --> Onaylandı ✓")
                    onay1 = 1
                else:
                    print("Kullanıcı adınızda küçük ve büyük harf de olmalı!")
                    continue
        else:
            print("Kullanıcı adınızda özel karakter bulunamaz!")
            continue
    else:
        print("Kullanıcı adınızın uzunluğu 16 karakterden fazla!")
        continue

    if 8 <= len(sifre) <= 24:

        if sifre.isalnum():

            if sifre.isalpha():
                if sifre.islower():
                    print("Şifrenizde en az bir rakam, en az bir özel karakter ve en az bir de büyük harf olmalı!")
                    continue

                elif sifre.isupper():
                    print("Şifrenizde en az bir rakam, en az bir özel harakter ve en az bir de küçük harf olmalı!")
                    continue

                else:
                    print("Şifrenizde rakam ve özel karakter de olmalı!")
                    continue

            elif sifre.isnumeric():
                print("Şifrenizde en az bir küçük harf, en az bir büyük harf ve en az bir de özel karakter olmalı!")
                continue

            else:
                for t in sifre:
                    for g in t:
                        if g in buyukharf:
                            bharf += 1
                for u in sifre:
                    for v in u:
                        if v in kucukharf:
                            kharf += 1

                if kharf < 1 and bharf < 1:
                    print("Şifrenizde en az bir özel karakter, en az bir küçük harf ve en az bir büyük harf bulunmalıdır!")
                    continue
                elif kharf > 0 and bharf < 1:
                    print("Şifrenizde en az bir özel karakter ve en az bir büyük harf bulunmalıdır!")
                    continue
                elif kharf < 1 and bharf > 0:
                    print("Şifrenizde en az bir özel karakter ve en az bir küçük harf bulunmalıdır!")
                    continue
                else:
                    print("Şifrenizde en az bir özel karakter bulunmalıdır!")
                    continue

        else:
            for i in sifre:
                for a in i:
                    if a in buyukharf:
                        f += 1
            for i in sifre:
                for b in i:
                    if b in kucukharf:
                        g += 1
            for i in sifre:
                for c in i:
                    if c in sayi:
                        h += 1

            if f < 1 and g < 1 and h < 1:
                print("Şifrenizde en az bir küçük harf, en az bir büyük harf ve en az bir rakam bulunmalıdır!")
                continue
            elif f < 1 and g > 0 and h > 0:
                print("Şifrenizde en az bir büyük harf bulunmalıdır!")
                continue
            elif f < 1 and g < 1 and h > 0:
                print("Şifrenizde en az bir büyük harf ve en az bir küçük harf bulunmalıdır!")
                continue
            elif f < 1 and g > 0 and h < 1:
                print("Şifrenizde en az bir büyük harf ve en az bir rakam bulunmalıdır!")
                continue
            elif f > 0 and g < 1 and h < 1:
                print("Şifrenizde en az bir küçük harf ve en az bir rakam bulunmalıdır!")
                continue
            elif f > 0 and g > 0 and h < 1:
                print("Şifrenizde en az bir rakam bulunmalıdır!")
                continue
            elif f > 0 and g < 1 and h > 0:
                print("Şifrenizde en az bir küçük harf bulunmalıdır!")
                continue
            else:
                print("Şifre --> Onaylandı ✓")
                onay2 = 1
    else:
        print("Şifrenizin uzunluğu 8 ile 24 karakter arasında olmalı!")

    if onay1 == 1 and onay2 == 1:
        print("\n-> Giriş Yapma Paneli <-")
        while True:
            k1 = input("\nKullanıcı adınızı giriniz:")
            s1 = input("Şifrenizi giriniz:")

            if k1 == kullaniciadi and s1 != sifre:
                print("\nKullanıcı adınız doğru fakat şifreniz yanlış!")
                continue
            elif k1 != kullaniciadi and s1 == sifre:
                print("\nŞifreniz doğru fakat kullanıcı adınız yanlış!")
                continue
            elif k1 != kullaniciadi and s1 != sifre:
                print("\nHem kullanıcı adınız hem de şifreniz yanlış!")
                continue
            else:
                print("\n--> Sisteme başarıyla giriş yaptınız ✓")
                print(""" 
                  Hesap Makinesi                     
           ___________________________ 
          /              |-| |O| |X| / 
         /_________________________ / 
        /          Toplama --> +   / 
       /_________________________ / 
      /        Çıkarma --> -     / 
     /_________________________ / 
    /      Çarpma --> *        / 
   /_________________________ / 
  /    Bölme --> /           / 
 /_________________________ / 

Yapmak istediğiniz işlemi seçip ENTER tuşuna basınız.(Örneğin 
24 * 5 yazdıktan sonra ENTER tuşuna basın.) 
""")
                islem = input("İşleminizi giriniz:")
                sonuc = eval(islem)
                print(sonuc)
                break
        break