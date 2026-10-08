INSERT INTO siparis(
    musteri_ad, adres, tel, siparis_tur, tarih, saat, durum, notlar, alinan_tarih
)
VALUES(
    'Muharrem Kalın', 'Kazım Dirik Mh. 230 Sk. No: 12 Hakan Apt Bornova', '0555 555 55 55', 'İlaçlama', '2026-06-28', '09:00:00', 'Tamamlandı', 'Evcil hayvan var.', CURRENT_TIMESTAMP
)

INSERT INTO ilaclama(
    s_id, daire_sayi, daire_basi_fiyat, toplam_fiyat
)
VALUES(
    3, 10, 400, 10 * 400
)