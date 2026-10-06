# AI Geliştirme Kaydı

- Kullanıcı tercihleri: Django, Conda `base`, SQLite, önce yerel hazırlık; marka adı Enes Turhan. Yeni Python ortamı oluşturulmaması istendi ve VS Code yorumlayıcısı mevcut `base` ortamına geçirildi.
- Tasarım referansı: `https://tarhannes.com.tr/`; geniş boşluk, güçlü başlık hiyerarşisi, kırmızı/bordo vurgu ve küçük koyu navigasyon öğeleri uygulandı.
- Uygulama: `requests_app` içinde hizmet talebi modeli, ModelForm doğrulaması, kayıt sonrası yönlendirme ve veritabanı hatası durumu ayrıştırıldı. Form başarı mesajı yalnızca veritabanı yazımı başarılı olduktan sonra eklenir.
- Yayın sınırı: Hosting hesabı ve uzak Git deposu erişimi olmadığı için canlı URL veya herkese açık kaynak URL’si oluşturulmadı. Dağıtım gereksinimleri README’de belirtildi.
- Doğrulama kaydı: `python manage.py check` temiz geçti, migration'lar SQLite'a uygulandı ve `python manage.py test requests_app.tests` üç testi başarıyla tamamladı. Mobil görünümde bulunan taşma düzeltildi; yerel tarayıcıda sayfa açılıp kontrol edildi.