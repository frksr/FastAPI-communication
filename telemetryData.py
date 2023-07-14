


# GET /api/giris
teamLogin = {
        "kadi" : "takimkadi",
        "sifre" : "takimsifresi"
    }

# GET /api/serverTime
serverTime = {
        "saat": 6,
        "dakika": 9,
        "saniye": 2,
        "milisaniye": 617
    }

# // POST api/telemetryData
telemetryData = {
    "takim_numarasi": 1,
    "IHA_enlem": 43.576546,
    "IHA_boylam": 22.385421,
    "IHA_irtifa": 100,
    "IHA_dikilme": 5,
    "IHA_yonelme": 256,
    "IHA_yatis": 0,
    "IHA_hiz": 223,
    "IHA_batarya": 20,
    "IHA_otonom": 0,
    "IHA_kilitlenme": 1,
    "Hedef_merkez_X": 315,
    "Hedef_merkez_Y": 220,
    "Hedef_genislik": 12,
    "Hedef_yukseklik": 46,
    "GPSSaati": {
            "saat": 19,
            "dakika": 1,
            "saniye": 23,
            "milisaniye": 507
        }
}

# telemetryData response
responseTelemetryData = {
    
        "sunucuSaati": {
                "saat": 6,
                "dakika": 53,
                "saniye": 42,
                "milisaniye": 500
            },
        "konumBilgileri": [
            {
                "takim_numarasi": 1,
                "iha_enlem": 12.236945,
                "iha_boylam": 26.945331,
                "iha_irtifa": 25,
                "iha_dikilme": 5,
                "iha_yonelme": 256,
                "iha_yatis": 0,
                "zaman_farki": 93
            },
            {
                "takim_numarasi": 2,
                "iha_enlem": 41.265854,
                "iha_boylam": 25.697435,
                "iha_irtifa": 55,
                "iha_dikilme": 5,
                "iha_yonelme": 256,
                "iha_yatis": 0,
                "zaman_farki": 74
            },
            {
                "takim_numarasi": 3,
                "iha_enlem": 41.598546,
                "iha_boylam": 26.974315,
                "iha_irtifa": 65,
                "iha_dikilme": 5,
                "iha_yonelme": 12,
                "iha_yatis": 4,
                "zaman_farki": 43
            }
        ]
    }

# POST /api/tracking
trackingData = {
    
        "kilitlenmeBaslangicZamani": {
        "saat": 19,
        "dakika": 1,
        "saniye": 23,
        "milisaniye": 507
        },
        "kilitlenmeBitisZamani": {
        "saat": 19,
        "dakika": 1,
        "saniye": 45,
        "milisaniye": 236
        },
        "otonom_kilitlenme": 0
    }


# POST /api/kamikazeInfo
kamikazeData = {
    
        "kamikazeBaslangicZamani": {
        "saat": 19,
        "dakika": 1,
        "saniye": 23,
        "milisaniye": 507
        },
        "kamikazeBitisZamani": {
        "saat": 19,
        "dakika": 1,
        "saniye": 28,
        "milisaniye": 236
        },
        "qrMetni ": "teknofest2022"
    }

# GET /api/qrCoordinate:
qrData = {
    
        "qrEnlem": 41.123456,
        "qrBoylam": 26.654987
    }