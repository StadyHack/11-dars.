menu = ['Somsa', 'tovuq', 'sho`rva', 'kaklet', 'osh', 'manti', 'Norin', 'Lavash', 'Free']
zakas = ['manti', 'spagetti', 'qarsildoq', 'beshbarmoq', 'issiq', 'free', 'Tuxumbarak', 'osh']

klon = []

for royxatt in menu:
    rt = royxatt.lower()
    klon.append(rt)

for royxat in zakas:
    if royxat.lower() in klon:
        print(f"Sizning buyurtmangiz qabul qilindi \n {royxat} eng qisqa mudatta yetkiziladi ")
    else:
        print(f"Kechirasiz {royxat} bizning menu da mavjud emas")