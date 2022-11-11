import mylib as lib

VuKhi = "Kiem"
Tuoi = 100
tts = lib.TruongThuySon(VuKhi, Tuoi)
tts.info()

Lev = 200
tvk = lib.TruongVoKy(VuKhi, Tuoi, Lev)
tvk.info()
tvk.infoTruongVoKy()