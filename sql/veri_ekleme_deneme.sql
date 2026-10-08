INSERT INTO siparis(
    musteri_ad, adres, tel, siparis_tur, tarih, saat, durum, notlar, alinan_tarih
) 

VALUES (
    'Ahmet Yılmaz', 'İstanbul, Türkiye', '555-123-4567', 'İlaçlama', '2024-06-01', '10:00:00', 'Tamamlandı', 'Evcil hayvan var.', '2024-05-24 10:00:00'
),
(
    'Ayşe Demir', 'Ankara, Türkiye', '555-987-6543', 'Yıkama', '2024-06-02', '14:00:00', 'Beklemede', 'Evde kimse yok.', '2024-04-02 14:00:00'
);

INSERT INTO yikama(
    s_id, yikama_tur, sandalye_sayi, fiyat, minderli
)
VALUES (
    2, 'Koltuk Yıkama', 3, 150, 1
);

INSERT INTO ilaclama(
    s_id, daire_sayi, daire_basi_fiyat, toplam_fiyat
)
VALUES (
    1, 2, 50, 100
);
