-- ==========================================================
-- Fikri Usta Sipariş Sistemi - Veritabanı Tablo Şeması (SQLite)
-- ==========================================================

CREATE TABLE IF NOT EXISTS musteri (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,
    tel TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS siparis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    musteri_id INTEGER NOT NULL,
    adres TEXT,
    tel TEXT,
    siparis_tur TEXT NOT NULL,
    tarih DATE,
    saat TEXT,
    durum TEXT DEFAULT 'BEKLİYOR',
    notlar TEXT,
    alinan_tarih DATETIME DEFAULT CURRENT_TIMESTAMP,
    tamamlanan_tarih DATETIME,

    FOREIGN KEY (musteri_id) REFERENCES musteri(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS yikama (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    siparis_id INTEGER NOT NULL,
    takim_sayi INTEGER DEFAULT 0,
    yatak_sayi INTEGER DEFAULT 0,
    sandalye_sayi INTEGER DEFAULT 0,
    fiyat REAL,

    FOREIGN KEY (siparis_id) REFERENCES siparis(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ilaclama (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    siparis_id INTEGER NOT NULL,
    daire_sayi INTEGER DEFAULT 1,
    daire_basi_fiyat REAL,
    toplam_fiyat REAL,

    FOREIGN KEY (siparis_id) REFERENCES siparis(id) ON DELETE CASCADE
);