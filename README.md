# Mülakat Örnek | Dijital Ürün ve Yazılım

Kişisel hizmet tanıtım sayfası ve hizmet talebi formu. Django ile sunulan form alanları hem tarayıcıda hem sunucuda doğrulanır; geçerli talepler SQLite veritabanına kaydedilir.

## Gereksinimler

- Python 3.12 veya üzeri
- Django 6.x (`base` ortamında kuruluysa yeniden kurmak gerekmez)

## Yerelde çalıştırma

Mevcut Conda `base` ortamı etkinleştirildikten sonra proje kökünde:

```bash
python manage.py migrate
python manage.py runserver
```

Sayfa `http://127.0.0.1:8000/` adresinde açılır. Alternatif olarak bağımlılıkları `python -m pip install -r requirements.txt` ile kurabilirsiniz.

Başvurular `db.sqlite3` içinde kalıcı olarak saklanır. Django yönetim arayüzü `/admin/` altında kullanılabilir; yönetici hesabı için `python manage.py createsuperuser` çalıştırın.

## Doğrulama ve form durumları

İsim, e-posta, hizmet ve açıklama alanları zorunludur. İsim en az 2, açıklama en az 20 karakter olmalıdır. E-posta ve hizmet seçimi Django tarafından doğrulanır; HTML kısıtları ve JavaScript gönderim davranışı istemci tarafındaki geri bildirimi sağlar. Başarı bildirimi yalnızca veritabanı kaydı tamamlandıktan sonra gösterilir. Veritabanı hatasında form hata bildirimi gösterir ve başarı mesajı üretilmez.

## Dağıtım notları

Bu teslim yerel çalışmaya hazırdır; Repo [link](https://github.com/rag0nn/interview) Yayın için hosting hesabı ve bir uzak depo hedefi gerekir. Üretimde `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0` ve `DJANGO_ALLOWED_HOSTS` ortam değişkenlerini tanımlayın; SQLite dosyası kalıcı disk üzerinde tutulmalıdır. Kalıcı dosya diski sunmayan platformlarda üretim veritabanı olarak PostgreSQL yapılandırın. Gerçek canlı URL ve herkese açık kaynak bağlantısı bu erişimler sağlanınca eklenmelidir.

## Proje notları

- [requirements.md](requirements.md): gereksinimler ve tamamlanma durumu
- [summary.md](summary.md): değişiklik özeti
- [summary_timeline.md](summary_timeline.md): değişiklik zaman çizelgesi
- [AI_LOG.md](AI_LOG.md): geliştirme ai logu
