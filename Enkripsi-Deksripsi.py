import string

text = string.printable

#pilih opsi 1, masukan dulu isi pesan di enkripsi dan sandinya bebas nanti bila sudah diisi, masukan output pesan dan masukan sandi yang di enkrripsi tadi ke opsi 2 atau deksripsi
def enkripsi(isi):
    global text

    key = int(input("Masukan Sandi : "))
    cipher = ""
    for i in isi:
        if i in text:
            k = text.find(i)
            k = (k + key) % 100
            cipher = cipher+text[k]
        else:
            cipher = cipher + i

    return cipher
#

def deksripsi(cipher):
    global text
    key = int(input('Masukan Sandi : '))

    isi = ''
    for i in cipher:
        if i in text:
            k = text.find(i)
            k = (k - key) % 100
            isi = isi+text[k]
        else:
            isi = isi + i

    return isi


if __name__ == "__main__":
    mode = int(input("1. Enkripsi Pesan\n2. Deksripsi Pesan\nPilih Opsi :"))

    if mode == 1:
        isi = input("Masukan Isi Pesan :")
        print(enkripsi(isi))
    elif mode == 2:
        cipher = input("Masukan Isi Pesan : ")
        print(deksripsi(cipher))
    else:
        print("MASUKAN PILIHAN ANDA!!")
