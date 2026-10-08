SELECT
    s.id,
    s.musteri_ad,
    s.adres,
    s.tel,
    s.siparis_tur,
    i.toplam_fiyat
FROM siparis AS s
LEFT JOIN ilaclama AS i
    ON s.id = i.s_id
WHERE s.siparis_tur = 'İlaçlama';

SELECT
    s.id,
    s.musteri_ad,
    s.adres,
    s.tel,
    s.siparis_tur,
    y.fiyat
FROM siparis AS s
LEFT JOIN yikama AS y
    ON s.id = y.s_id
WHERE s.siparis_tur = 'Yıkama';