# Envanter Yönetim Sistemi

## İçindekiler
1. [Giriş](#giriş)
2. [Amaç](#amaç)
3. [Özellikler](#özellikler)
4. [Gereksinimler](#gereksinimler)
5. [Proje Özeti-Sınıflar ve Metodlar](#sınıflar-ve-metodlar)
   - [Item Sınıfı](#item-sınıfı)
   - [Envanter Sınıfı](#envanter-sınıfı)
   - [EnvanterGUI Sınıfı](#envantergui-sınıfı)
6. [Kodu Çalıştırma Talimatları](#kodu-çalıştırma-talimatları)
   - [Kullanım Görselleri](#kullanım-görselleri)
7. [Sonuç](#sonuç)

## Giriş

Bu proje, Python'un Tkinter kütüphanesini kullanarak bir grafik arayüz ile envanter yönetim sistemi oluşturmayı amaçlamaktadır. Bu sistem, kullanıcıların envanterlerini kolayca yönetmelerine olanak tanır.

## Amaç

Bu projenin amacı, kullanıcıların öğeleri envantere ekleyebilmeleri, güncelleyebilmeleri, silebilmeleri, listeleyebilmeleri ve toplam envanter değerini görebilmelerini sağlayan bir envanter yönetim sistemi geliştirmektir.

## Özellikler

- **Öğe Ekleme:** Envantere yeni bir öğe ekleyin.
- **Öğe Güncelleme:** Mevcut bir öğenin miktarını ve fiyatını güncelleyin.
- **Öğe Silme:** Envanterden bir öğeyi silin.
- **Öğeleri Listeleme:** Envanterde bulunan tüm öğeleri listeleyin.
- **Öğe Arama:** Envanterde bir öğe arayın.
- **Toplam Değeri Görüntüleme:** Envanterdeki tüm öğelerin toplam değerini hesaplayın ve görüntüleyin.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki gereksinimlere ihtiyacınız var:

- Python 3.x
- Tkinter (Python ile birlikte gelir)

## Proje Özeti - Sınıflar ve Metodlar

### Item Sınıfı

Bu sınıf, envanterdeki öğelerin temel yapı taşını oluşturur. Her öğe bir isim, miktar ve fiyat değerine sahiptir.

#### `__init__` Metodu

```python
class Item:
    def __init__(self, ad, miktar, fiyat):
        """
        Bir öğe nesnesi oluşturur.
        Args:
            ad (str): Öğenin adı.
            miktar (int): Öğenin miktarı.
            fiyat (float): Öğenin birim fiyatı.
        """
        if not ad:
            messagebox.showerror("Hata", "Öğe adı boş olamaz.")
            raise ValueError("Öğe adı boş olamaz.")
        if miktar < 0:
            messagebox.showerror("Hata", "Öğe miktarı negatif olamaz.")
            raise ValueError("Öğe miktarı negatif olamaz.")
        if fiyat < 0:
            messagebox.showerror("Hata", "Öğe fiyatı negatif olamaz.")
            raise ValueError("Öğe fiyatı negatif olamaz.")

        self.ad = ad
        self.miktar = miktar
        self.fiyat = fiyat
```

Bu metod, bir öğe nesnesi oluşturur ve öğe adının boş, miktarının ve fiyatının negatif olmamasını kontrol eder.

#### `__str__` Metodu

```python
def __str__(self):
    return f"{self.ad} - Miktar: {self.miktar}, Fiyat: {self.fiyat}"
```

Bu metod, öğenin adını, miktarını ve fiyatını metin olarak döndürür.

### Envanter Sınıfı

Bu sınıf, öğelerin yönetimini sağlar ve envanterin toplam değerini hesaplar.

#### `__init__` Metodu

```python
class Envanter:
    def __init__(self):
        self.ogeler = {}
        self.onceki_toplam_deger = 0
```

Bu metod, envanter nesnesi oluşturur ve öğeleri saklamak için bir sözlük ve önceki toplam değeri saklamak için bir değişken tanımlar.

#### `oge_ekle` Metodu

```python
def oge_ekle(self, ad, miktar, fiyat):
    self.onceki_toplam_deger = self.toplam_deger()
    if ad in self.ogeler:
        self.ogeler[ad].miktar += miktar
    else:
        self.ogeler[ad] = Item(ad, miktar, fiyat)
```

Bu metod, envantere yeni bir öğe ekler veya varsa miktarını günceller.

#### `oge_guncelle` Metodu

```python
def oge_guncelle(self, ad, miktar, fiyat):
    self.onceki_toplam_deger = self.toplam_deger()
    if ad in self.ogeler:
        self.ogeler[ad].miktar = miktar
        self.ogeler[ad].fiyat = fiyat
    else:
        print(f"Öğe '{ad}' envanterde bulunamadı.")
```

Bu metod, mevcut bir öğenin miktarını ve fiyatını günceller.

#### `oge_sil` Metodu

```python
def oge_sil(self, ad):
    self.onceki_toplam_deger = self.toplam_deger()
    if ad in self.ogeler:
        del self.ogeler[ad]
    else:
        print(f"Öğe '{ad}' envanterde bulunamadı.")
```

Bu metod, var olan bir öğeyi envanterden siler.

#### `ogeleri_listele` Metodu

```python
def ogeleri_listele(self):
    for oge in self.ogeler.values():
        print(oge)
```

Bu metod, envanterde bulunan tüm öğeleri ekrana yazdırır.

#### `oge_ara` Metodu

```python
def oge_ara(self, ad):
    return self.ogeler.get(ad, None)
```

Bu metod, verilen adla bir öğeyi arar ve bulursa nesnesini döndürür.

#### `toplam_deger` Metodu

```python
def toplam_deger(self):
    return sum(oge.miktar * oge.fiyat for oge in self.ogeler.values())
```

Bu metod, envanterin toplam değerini hesaplar.

#### `detayli_toplam_deger` Metodu

```python
def detayli_toplam_deger(self):
    detaylar = []
    toplam_deger = 0
    for oge in self.ogeler.values():
        oge_toplam = oge.miktar * oge.fiyat
        detaylar.append(f"{oge.ad} - Miktar: {oge.miktar}, Toplam Fiyat: {oge_toplam:.2f} TL")
        toplam_deger += oge_toplam
    return detaylar, toplam_deger
```

Bu metod, envanterin detaylı toplam değerini hesaplar ve her bir öğe için ayrıntılı bilgi döndürür.

### EnvanterGUI Sınıfı

Bu sınıf, Tkinter kullanarak grafik arayüzü sağlar ve kullanıcı etkileşimlerini yönetir.

#### `__init__` Metodu

```python
class EnvanterGUI:
    def __init__(self, root):
        self.envanter = Envanter()
        self.root = root
        self.root.title("Envanter Yönetim Sistemi")

        label_font = ("Helvetica", 12, "bold")
        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 12)

        self.ad_etiket = tk.Label(root, text="Öğe Adı", font=label_font)
        self.ad_etiket.grid(row=0, column=0, padx=10, pady=5)
        self.ad_giris = tk.Entry(root, font=entry_font)
        self.ad_giris.grid(row=0, column=1, padx=10, pady=5)

        self.miktar_etiket = tk.Label(root, text="Miktar", font=label_font)
        self.miktar_etiket.grid(row=1, column=0, padx=10, pady=5)
        self.miktar_giris = tk.Entry(root, font=entry_font)
        self.miktar_giris.grid(row=1, column=1, padx=10, pady=5)

        self.fiyat_etiket = tk.Label(root, text="Fiyat", font=label_font)
        self.fiyat_etiket.grid(row=2, column=0, padx=10, pady=5)
        self.fiyat_giris = tk.Entry(root, font=entry_font)
        self.fiyat_giris.grid(row=2, column=1, padx=10, pady=5)

        button_style = {"font": button_font, "bg": "#4CAF50", "fg": "white", "padx": 10, "pady": 5}

        self.ekle_buton = tk.Button(root, text="Öğe Ekle", command=self.oge_ekle, **button_style)
        self.ekle_buton.grid(row=3, column=0, padx=10, pady=5)

        self.guncelle_buton = tk.Button(root, text="Öğe Güncelle", command=self.oge_guncelle, **button_style)
        self.guncelle_buton.grid(row=3, column=1, padx=10, pady=5)

        self.sil_buton = tk.Button(root, text="Öğe Sil", command=self.oge_sil, bg="red", fg="white", font=button_font,
                                   padx=10, pady=5)
        self.sil_buton.grid(row=3, column=2, padx=10, pady=5)

        self.listele_buton = tk.Button(root, text="Öğeleri Listele", command=self.ogeleri_listele, **button_style)
        self.listele_buton.grid(row=4, columnspan=3, padx=10, pady=5)

        self.ara_buton = tk.Button(root, text="Öğe Ara", command=self.oge_ara, **button_style)
        self.ara_buton.grid(row=5, columnspan=3, padx=10, pady=5)

        self.toplam_deger_buton = tk.Button(root, text="Toplam Değer", command=self.toplam_degeri_goster,
                                            **button_style)
        self.toplam_deger_buton.grid(row=6, columnspan=3, padx=10, pady=5)

        self.bitir_buton = tk.Button(root, text="İşlemi Bitir", command=self.islemi_bitir, **button_style)
        self.bitir_buton.grid(row=7, columnspan=3, padx=10, pady=5)
```

Bu metod, kullanıcı arayüzünü oluşturur ve tüm bileşenleri yerleştirir.

#### Arayüz İşlevleri

```python
def oge_ekle(self):
    ad = self.ad_giris.get()
    try:
        miktar = int(self.miktar_giris.get())
        fiyat = float(self.fiyat_giris.get())
        self.envanter.oge_ekle(ad, miktar, fiyat)
        messagebox.showinfo("Başarılı", "Öğe eklendi.")
    except ValueError as e:
        messagebox.showerror("Hata", str(e))

def oge_guncelle(self):
    ad = self.ad_giris.get()
    try:
        miktar = int(self.miktar_giris.get())
        fiyat = float(self.fiyat_giris.get())
        self.envanter.oge_guncelle(ad, miktar, fiyat)
        messagebox.showinfo("Başarılı", "Öğe güncellendi.")
    except ValueError as e:
        messagebox.showerror("Hata", str(e))

def oge_sil(self):
    ad = self.ad_giris.get()
    self.envanter.oge_sil(ad)
    messagebox.showinfo("Başarılı", "Öğe silindi.")

def ogeleri_listele(self):
    ogeler = self.envanter.ogeleri_listele()
    if not ogeler:
        messagebox.showinfo("Envanter Boş", "Envanterde öğe yok.")
    else:
        liste = "\n".join(str(oge) for oge in self.envanter.ogeler.values())
        messagebox.showinfo("Envanter Listesi", liste)

def oge_ara(self):
    ad = self.ad_giris.get()
    oge = self.envanter.oge_ara(ad)
    if oge:
        messagebox.showinfo("Öğe Bulundu", str(oge))
    else:
        messagebox.showwarning("Öğe Bulunamadı", "Öğe envanterde yok.")

def toplam_degeri_goster(self):
    detaylar, toplam_deger = self.envanter.detayli_toplam_deger()
    detayli_mesaj = "\n".join(detaylar)
    messagebox.showinfo("Toplam Envanter Değeri", f"{detayli_mesaj}\n\nToplam Değer: {toplam_deger:.2f} TL")

def islemi_bitir(self):
    self.root.quit()
```

Bu işlevler, GUI bileşenlerinin davranışlarını tanımlar ve kullanıcı etkileşimlerini yönetir.


## **Kodu Çalıştırma Talimatları**<br/>
Bu proje geliştirme sürecinde Google Colab kullanılmıştır. Kodu çalıştırma talimatları da bu doğrultuda açıklanmıştır.<br/>
Google Colab ile kodları çalıştırmak için aşağıdaki adımları izleyebilirsiniz:<br/>
1. **Google Colab'e Git:**
   - Google Colab'e gitmek için [Google Colab](https://colab.research.google.com/) sayfasını ziyaret edin.<br/>
   - Yeni bir notebook oluşturun.
2. **Google Drive'ı Bağlama:**
   - Google Drive'ınızı Colab'e bağlamak için aşağıdaki kodu yeni bir hücreye yapıştırın ve çalıştırın. Bu işlem, CSV dosyanıza erişmenizi sağlayacaktır.<br/>
     `python`<br/>
     `from google.colab import drive`<br/>
     `drive.mount('/content/drive')`<br/>
3. **CSV Dosyasının Yolunu Belirleme:**
   - CSV dosyanızın Google Drive'da nerede olduğunu belirleyin ve dosya yolunu not edin. Örneğin, `'/content/drive/MyDrive/Adsız klasör/dataset.csv'`.   
4. **Kodları Yapıştırma ve Çalıştırma:**
   - Yukarıda yer alan işlem kodlarını Google Colab'deki hücrelere sırayla yapıştırın ve her hücreyi çalıştırın.<br/>
Bu adımları izleyerek Google Colab üzerinde projenizi çalıştırabilir ve analizlerinizi gerçekleştirebilirsiniz.

### Kullanım Görselleri
#### Öğe Ekleme
Ürün sayısı ve ürün miktarı negatifken işlem yapılmaz. ürn adı girilmemişken işlem gerçekleştirilmez. <br/>
**ürün adı girilmemişken**
![ürün adı girilmemişken](https://github.com/Zeynep981/staj-projesi2/blob/main/images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-07-17%20135003.png)
**ürün miktarı negatifken**
![ürün miktarı negatifken](https://github.com/Zeynep981/staj-projesi2/blob/main/images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-07-17%20134808.png)
**ürün başarıyla eklenince**
![ürün başarıyla eklenince](https://github.com/Zeynep981/staj-projesi2/blob/main/images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-07-17%20133945.png)
#### Öğe Güncelleme
Var olan ürünün miktarı veya fiyatını değiştirmek için yapılır.<br/>
![öğe güncelle](https://github.com/Zeynep981/staj-projesi2/blob/main/images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-07-17%20134043.png)
#### Öğe Listeleme
Var olan öğelerin miktar ve fiyatlarını görmek için yapılır.
![öğe listeleme](https://github.com/Zeynep981/staj-projesi2/blob/main/images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-07-17%20134043.png)
#### Öğe Silme
Silinmek istenen öğenin adı girilerek yapılır. var olmayan bir öğe silinemez.
![öğe silme](https://github.com/Zeynep981/staj-projesi2/blob/main/images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-07-17%20134322.png)
#### Öğe Arama
Var olan bir öğe adı girilerek aranır.
![öğe arama](https://github.com/Zeynep981/staj-projesi2/blob/main/images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-07-17%20134322.png)
Silinen ya da var olmayan bir öğe bulunamaz.
![öğe bulunamadı](https://github.com/Zeynep981/staj-projesi2/blob/main/images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202024-07-17%20134409.png)
#### Toplam Değer
Toplam değeri detaylı bir şekilde görmekiçin yapılır
## Sonuç

Bu proje, kullanıcıların envanterlerini yönetmelerine yardımcı olan basit bir envanter yönetim sistemi sunar. Kullanıcı dostu arayüzü sayesinde öğe ekleme, güncelleme, silme ve listeleme gibi işlemler kolayca gerçekleştirilebilir. Tkinter ile oluşturulan grafik arayüz, kullanıcıların bu işlemleri hızlı ve verimli bir şekilde yapmalarına olanak tanır.
