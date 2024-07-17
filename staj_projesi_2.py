import tkinter as tk  # Tkinter kütüphanesini tk olarak içe aktar
from tkinter import messagebox  # Tkinter'den messagebox modülünü içe aktar

# Öğe sınıfı tanımlaması
class Item:
    def __init__(self, ad, miktar, fiyat):
        """
        Bir öğe nesnesi oluşturur.

        Args:
            ad (str): Öğenin adı.
            miktar (int): Öğenin miktarı.
            fiyat (float): Öğenin birim fiyatı.
        """
        # Öğe adının boş olmamasını kontrol et
        if not ad:
            messagebox.showerror("Hata", "Öğe adı boş olamaz.")
            raise ValueError("Öğe adı boş olamaz.")
        # Öğe miktarının negatif olmamasını kontrol et
        if miktar < 0:
            messagebox.showerror("Hata", "Öğe miktarı negatif olamaz.")
            raise ValueError("Öğe miktarı negatif olamaz.")
        # Öğe fiyatının negatif olmamasını kontrol et
        if fiyat < 0:
            messagebox.showerror("Hata", "Öğe fiyatı negatif olamaz.")
            raise ValueError("Öğe fiyatı negatif olamaz.")

        self.ad = ad  # Öğenin adı
        self.miktar = miktar  # Öğenin miktarı
        self.fiyat = fiyat  # Öğenin birim fiyatı

    def __str__(self):
        """
        Öğe nesnesinin metin temsilini döndürür.

        Returns:
            str: Öğenin adı, miktarı ve fiyatıyla biçimlenmiş metin.
        """
        return f"{self.ad} - Miktar: {self.miktar}, Fiyat: {self.fiyat}"


# Envanter sınıfı tanımlaması
class Envanter:
    def __init__(self):
        """
        Envanter nesnesi oluşturur ve özelliklerini başlatır.

        Attributes:
            ogeler (dict): Öğelerin adını anahtar olarak tutan sözlük.
            onceki_toplam_deger (float): Envanterin son güncellenmiş toplam değeri.
        """
        self.ogeler = {}  # Öğelerin depolanacağı sözlük
        self.onceki_toplam_deger = 0  # Önceki toplam değer için başlangıç değeri

    def oge_ekle(self, ad, miktar, fiyat):
        """
        Envantere yeni bir öğe ekler veya varsa miktarını günceller.

        Args:
            ad (str): Öğenin adı.
            miktar (int): Öğenin eklenecek veya güncellenecek miktarı.
            fiyat (float): Öğenin birim fiyatı.
        """
        self.onceki_toplam_deger = self.toplam_deger()  # Önceki toplam değeri güncelle
        if ad in self.ogeler:
            self.ogeler[ad].miktar += miktar  # Eğer öğe zaten varsa miktarı güncelle
        else:
            self.ogeler[ad] = Item(ad, miktar, fiyat)  # Yeni öğe ekle

    def oge_guncelle(self, ad, miktar, fiyat):
        """
        Var olan bir öğenin miktarını ve fiyatını günceller.

        Args:
            ad (str): Güncellenecek öğenin adı.
            miktar (int): Yeni miktar.
            fiyat (float): Yeni fiyat.
        """
        self.onceki_toplam_deger = self.toplam_deger()  # Önceki toplam değeri güncelle
        if ad in self.ogeler:
            self.ogeler[ad].miktar = miktar  # Öğenin miktarını güncelle
            self.ogeler[ad].fiyat = fiyat  # Öğenin fiyatını güncelle
        else:
            print(f"Öğe '{ad}' envanterde bulunamadı.")  # Hata durumunda mesaj yazdır

    def oge_sil(self, ad):
        """
        Var olan bir öğeyi envanterden siler.

        Args:
            ad (str): Silinecek öğenin adı.
        """
        self.onceki_toplam_deger = self.toplam_deger()  # Önceki toplam değeri güncelle
        if ad in self.ogeler:
            del self.ogeler[ad]  # Öğeyi sil
        else:
            print(f"Öğe '{ad}' envanterde bulunamadı.")  # Hata durumunda mesaj yazdır

    def ogeleri_listele(self):
        """
        Envanterde bulunan tüm öğeleri ekrana yazdırır.
        """
        for oge in self.ogeler.values():
            print(oge)

    def oge_ara(self, ad):
        """
        Verilen adla bir öğeyi arar ve bulursa nesnesini döndürür.

        Args:
            ad (str): Aranacak öğenin adı.

        Returns:
            Item or None: Bulunan öğe nesnesi veya None (eğer bulunamazsa).
        """
        return self.ogeler.get(ad, None)  # İsimle öğe ara, bulunamazsa None döndür

    def toplam_deger(self):
        """
        Envanterin toplam değerini hesaplar.

        Returns:
            float: Envanterdeki tüm öğelerin toplam değeri.
        """
        return sum(oge.miktar * oge.fiyat for oge in self.ogeler.values())

    def detayli_toplam_deger(self):
        """
        Envanterin detaylı toplam değerini hesaplar ve her bir öğe için ayrıntılı bilgi döndürür.

        Returns:
            tuple: (detaylar, toplam_deger)
                detaylar (list): Her bir öğe için biçimlenmiş detaylı bilgiler listesi.
                toplam_deger (float): Envanterdeki tüm öğelerin toplam değeri.
        """
        detaylar = []
        toplam_deger = 0
        for oge in self.ogeler.values():
            oge_toplam = oge.miktar * oge.fiyat
            detaylar.append(f"{oge.ad} - Miktar: {oge.miktar}, Toplam Fiyat: {oge_toplam:.2f} TL")
            toplam_deger += oge_toplam
        return detaylar, toplam_deger


# Envanter için grafik arayüzü sınıfı tanımlaması
class EnvanterGUI:
    def __init__(self, root):
        """
        Envanter yönetim sistemi için grafik arayüzü oluşturur.

        Args:
            root (tk.Tk): Ana tkinter penceresi.
        """
        self.envanter = Envanter()  # Envanter nesnesi oluştur

        self.root = root
        self.root.title("Envanter Yönetim Sistemi")  # Başlık ayarı

        # Ortak yazı tipi ayarları
        label_font = ("Helvetica", 12, "bold")
        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 12)

        # Öğe adı etiketi ve giriş kutusu
        self.ad_etiket = tk.Label(root, text="Öğe Adı", font=label_font)
        self.ad_etiket.grid(row=0, column=0, padx=10, pady=5)
        self.ad_giris = tk.Entry(root, font=entry_font)
        self.ad_giris.grid(row=0, column=1, padx=10, pady=5)

        # Miktar etiketi ve giriş kutusu
        self.miktar_etiket = tk.Label(root, text="Miktar", font=label_font)
        self.miktar_etiket.grid(row=1, column=0, padx=10, pady=5)
        self.miktar_giris = tk.Entry(root, font=entry_font)
        self.miktar_giris.grid(row=1, column=1, padx=10, pady=5)

        # Fiyat etiketi ve giriş kutusu
        self.fiyat_etiket = tk.Label(root, text="Fiyat", font=label_font)
        self.fiyat_etiket.grid(row=2, column=0, padx=10, pady=5)
        self.fiyat_giris = tk.Entry(root, font=entry_font)
        self.fiyat_giris.grid(row=2, column=1, padx=10, pady=5)

        # Buton stil ayarları
        button_style = {"font": button_font, "bg": "#4CAF50", "fg": "white", "padx": 10, "pady": 5}

        # Öğe ekleme butonu
        self.ekle_buton = tk.Button(root, text="Öğe Ekle", command=self.oge_ekle, **button_style)
        self.ekle_buton.grid(row=3, column=0, padx=10, pady=5)

        # Öğe güncelleme butonu
        self.guncelle_buton = tk.Button(root, text="Öğe Güncelle", command=self.oge_guncelle, **button_style)
        self.guncelle_buton.grid(row=3, column=1, padx=10, pady=5)

        # Öğe silme butonu
        self.sil_buton = tk.Button(root, text="Öğe Sil", command=self.oge_sil, bg="red", fg="white", font=button_font,
                                   padx=10, pady=5)
        self.sil_buton.grid(row=3, column=2, padx=10, pady=5)

        # Öğeleri listeleme butonu
        self.listele_buton = tk.Button(root, text="Öğeleri Listele", command=self.ogeleri_listele, **button_style)
        self.listele_buton.grid(row=4, columnspan=3, padx=10, pady=5)

        # Öğe arama butonu
        self.ara_buton = tk.Button(root, text="Öğe Ara", command=self.oge_ara, **button_style)
        self.ara_buton.grid(row=5, columnspan=3, padx=10, pady=5)

        # Toplam değeri gösterme butonu
        self.toplam_deger_buton = tk.Button(root, text="Toplam Değer", command=self.toplam_degeri_goster,
                                            **button_style)
        self.toplam_deger_buton.grid(row=6, columnspan=3, padx=10, pady=5)

        # İşlemi bitirme butonu
        self.bitir_buton = tk.Button(root, text="İşlemi Bitir", command=self.islemi_bitir, **button_style)
        self.bitir_buton.grid(row=7, columnspan=3, padx=10, pady=5)

    def oge_ekle(self):
        """
        Kullanıcının girdiği bilgilerle bir öğe ekler ve sonucunu kullanıcıya gösterir.
        """
        ad = self.ad_giris.get()  # Öğe adını al
        miktar = int(self.miktar_giris.get())  # Öğe miktarını al
        fiyat = float(self.fiyat_giris.get())  # Öğe fiyatını al
        self.envanter.oge_ekle(ad, miktar, fiyat)  # Envantere öğe ekle
        yeni_toplam_deger = self.envanter.toplam_deger()  # Yeni toplam değeri al
        fark = yeni_toplam_deger - self.envanter.onceki_toplam_deger  # Değişimi hesapla
        # Kullanıcıya bilgi mesajı göster
        mesaj = f"Öğe başarıyla eklendi\nÖnceki Toplam Değer: {self.envanter.onceki_toplam_deger:.2f} TL\nYeni Toplam Değer: {yeni_toplam_deger:.2f} TL\nFark: {fark:.2f} TL"
        messagebox.showinfo("Başarılı", mesaj)

    def oge_guncelle(self):
        """
        Kullanıcının girdiği bilgilerle bir öğe günceller ve sonucunu kullanıcıya gösterir.
        """
        ad = self.ad_giris.get()  # Öğe adını al
        miktar = int(self.miktar_giris.get())  # Öğe miktarını al
        fiyat = float(self.fiyat_giris.get())  # Öğe fiyatını al
        self.envanter.oge_guncelle(ad, miktar, fiyat)  # Envanterdeki öğeyi güncelle
        yeni_toplam_deger = self.envanter.toplam_deger()  # Yeni toplam değeri al
        fark = yeni_toplam_deger - self.envanter.onceki_toplam_deger  # Değişimi hesapla
        # Kullanıcıya bilgi mesajı göster
        mesaj = f"Öğe başarıyla güncellendi\nÖnceki Toplam Değer: {self.envanter.onceki_toplam_deger:.2f} TL\nYeni Toplam Değer: {yeni_toplam_deger:.2f} TL\nFark: {fark:.2f} TL"
        messagebox.showinfo("Başarılı", mesaj)

    def oge_sil(self):
        """
        Kullanıcının girdiği bilgilerle bir öğe siler ve sonucunu kullanıcıya gösterir.
        """
        ad = self.ad_giris.get()  # Öğe adını al
        self.envanter.oge_sil(ad)  # Envanterden öğeyi sil
        yeni_toplam_deger = self.envanter.toplam_deger()  # Yeni toplam değeri al
        fark = yeni_toplam_deger - self.envanter.onceki_toplam_deger  # Değişimi hesapla
        # Kullanıcıya bilgi mesajı göster
        mesaj = f"Öğe başarıyla silindi\nÖnceki Toplam Değer: {self.envanter.onceki_toplam_deger:.2f} TL\nYeni Toplam Değer: {yeni_toplam_deger:.2f} TL\nFark: {fark:.2f} TL"
        messagebox.showinfo("Başarılı", mesaj)

    def ogeleri_listele(self):
        """
        Envanterde bulunan tüm öğeleri kullanıcıya gösterir.
        """
        ogeler = "\n".join(str(oge) for oge in self.envanter.ogeler.values())  # Öğeleri metin haline getir
        messagebox.showinfo("Envanter Listesi", ogeler)  # Kullanıcıya göster

    def oge_ara(self):
        """
        Kullanıcının girdiği öğe adını kullanarak bir öğe arar ve sonucunu kullanıcıya gösterir.
        """
        ad = self.ad_giris.get()  # Öğe adını al
        oge = self.envanter.oge_ara(ad)  # Öğeyi ara
        if oge:
            messagebox.showinfo("Öğe Bulundu", str(oge))  # Öğeyi kullanıcıya göster
        else:
            messagebox.showinfo("Hata", "Öğe bulunamadı")  # Hata mesajı göster

    def toplam_degeri_goster(self):
        """
        Envanterin detaylı toplam değerini hesaplar ve sonucunu kullanıcıya gösterir.
        """
        detaylar, toplam_deger = self.envanter.detayli_toplam_deger()  # Detayları ve toplam değeri al
        detaylar_str = "\n".join(detaylar)  # Detayları birleştir
        # Kullanıcıya detaylı toplam değeri göster
        messagebox.showinfo("Detaylı Toplam Değer", f"Toplam Değer: {toplam_deger:.2f} TL\n\n{detaylar_str}")

    def islemi_bitir(self):
        """
        Kullanıcının işlemi bitirme isteğini onaylar ve pencereyi kapatır.
        """
        cevap = messagebox.askyesno("İşlemi Bitir", "İşlemi tamamlamak istiyor musunuz?")  # Kullanıcıdan onay al
        if cevap:
            self.root.destroy()  # Pencereyi kapat


if __name__ == "__main__":
    root = tk.Tk()  # Ana tkinter penceresini oluştur
    gui = EnvanterGUI(root)  # Envanter GUI nesnesini oluştur
    root.mainloop()  # Ana döngüyü başlat
