# Fikri Usta Sipariş Sistemi

Fikri Usta Sipariş Sistemi, koltuk yıkama ve ilaçlama hizmeti veren işletmeler için geliştirilen bir **sipariş ve müşteri yönetim sistemi**dir.

Projenin backend tarafı **Python, FastAPI ve SQLite** kullanılarak geliştirilmiştir.

## 🚀 Özellikler

### Sipariş Yönetimi

* Yeni sipariş oluşturma
* Sipariş detaylarını görüntüleme
* Sipariş güncelleme
* Sipariş silme
* Sipariş durumunu güncelleme
* Sipariş tamamlanma tarihini takip etme
* Yıkama siparişlerine ait detayları yönetme
* İlaçlama siparişlerine ait detayları yönetme

### Müşteri Yönetimi

* Yeni müşteri oluşturma
* Müşteri bilgilerini görüntüleme
* Müşteri bilgilerini güncelleme
* Müşteri silme
* Ad veya telefon numarası ile müşteri arama
* Müşterinin sipariş geçmişini görüntüleme
* Aynı telefon numarasına sahip mükerrer müşteri oluşturulmasını engelleme

### Takvim

* Haftalık siparişleri görüntüleme
* Günlük siparişleri görüntüleme
* Bugünkü siparişleri görüntüleme
* Belirli tarih aralığındaki siparişleri görüntüleme
* Sipariş türüne göre takvim verilerini kullanma

### Dashboard

Dashboard üzerinden:

* Bugünkü toplam sipariş
* Bekleyen sipariş sayısı
* Onaylanan sipariş sayısı
* Yola çıkılan sipariş sayısı
* İşlemde olan sipariş sayısı
* Tamamlanan sipariş sayısı
* İptal edilen sipariş sayısı
* Haftalık toplam sipariş

görüntülenebilir.

## 🛠️ Kullanılan Teknolojiler

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **Pydantic**
* **SQLite**
* **Uvicorn**
* **Swagger / OpenAPI**

## 📁 Proje Yapısı

```text
FikriUstaSiparis/
│
├── app/
│   ├── core/
│   │   ├── config.py
│   │   ├── exception_handler.py
│   │   └── logger.py
│   │
│   ├── enums/
│   │   ├── siparis_durumu.py
│   │   └── siparis_turu.py
│   │
│   ├── models/
│   │   ├── ilaclama.py
│   │   ├── musteri.py
│   │   ├── siparis.py
│   │   └── yikama.py
│   │
│   ├── repositories/
│   │   ├── ilaclama_repository.py
│   │   ├── musteri_repository.py
│   │   ├── siparis_repository.py
│   │   └── yikama_repository.py
│   │
│   ├── routes/
│   │   ├── dashboard.py
│   │   ├── health.py
│   │   ├── musteri.py
│   │   ├── siparis.py
│   │   └── takvim.py
│   │
│   ├── schemas/
│   │   ├── durum.py
│   │   ├── ilaclama.py
│   │   ├── musteri.py
│   │   ├── musteri_siparis.py
│   │   ├── siparis.py
│   │   ├── siparis_detay.py
│   │   ├── takvim.py
│   │   └── yikama.py
│   │
│   ├── services/
│   │   ├── dashboard_service.py
│   │   ├── musteri_service.py
│   │   ├── siparis_service.py
│   │   └── takvim_service.py
│   │
│   ├── database.py
│   └── main.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Kurulum

### 1. Projeyi klonla

```bash
git clone <repository-url>
cd FikriUstaSiparis
```

### 2. Sanal ortam oluştur

Windows:

```bash
python -m venv venv
```

### 3. Sanal ortamı aktif et

Windows CMD:

```bash
venv\Scripts\activate
```

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Gerekli paketleri yükle

```bash
pip install -r requirements.txt
```

## ▶️ Uygulamayı Çalıştırma

Proje ana klasöründeyken:

```bash
uvicorn app.main:app --reload
```

Uygulama çalıştıktan sonra:

```text
http://127.0.0.1:8000
```

adresinden API'ye erişilebilir.

## 📚 API Dokümantasyonu

FastAPI'nin otomatik oluşturduğu Swagger arayüzü:

```text
http://127.0.0.1:8000/docs
```

Alternatif OpenAPI arayüzü:

```text
http://127.0.0.1:8000/redoc
```

## 🔌 Temel API Grupları

### Sipariş

```text
POST   /siparis
GET    /siparis
GET    /siparis/{siparis_id}
PUT    /siparis/{siparis_id}
DELETE /siparis/{siparis_id}
PATCH  /siparis/{siparis_id}/durum
```

### Müşteri

```text
POST   /musteri
GET    /musteri
GET    /musteri/ara
GET    /musteri/{musteri_id}
GET    /musteri/{musteri_id}/siparisler
PUT    /musteri/{musteri_id}
DELETE /musteri/{musteri_id}
```

### Takvim

```text
GET /takvim/haftalik
GET /takvim/gunluk
GET /takvim/bugun
GET /takvim/aralik
```

### Dashboard

```text
GET /dashboard
```

### Health Check

```text
GET /health
```

## 📌 Sipariş Durumları

Sistem aşağıdaki sipariş durumlarını desteklemektedir:

```text
BEKLİYOR
ONAYLANDI
YOLA_CIKILDI
ISLEMDE
TAMAMLANDI
IPTAL
```

## 🗄️ Veritabanı

Projenin mevcut sürümünde **SQLite** kullanılmaktadır.

Veritabanı dosyaları `.gitignore` içerisinde tutulduğu için GitHub repository'sine gönderilmez.

## 🔮 Gelecek Geliştirmeler

Planlanan geliştirmeler:

* React tabanlı Admin Panel
* Mobil uyumlu kullanıcı arayüzü
* Haftalık takvim arayüzü
* Sipariş detay popup'ı
* Müşteri yönetim ekranı
* Dashboard arayüzü
* Telefon üzerinden müşteriyi doğrudan arama
* Sipariş fiyatlandırma sistemi
* Manuel özel fiyat teklifi oluşturma
* Backend ve frontend entegrasyonu

## 👨‍💻 Geliştirici

**Fikri Usta Sipariş Sistemi**

Backend geliştirme: Python / FastAPI

---

> Bu proje, gerçek bir işletmenin günlük sipariş ve müşteri yönetimi süreçlerini dijitalleştirmek amacıyla geliştirilmektedir.
