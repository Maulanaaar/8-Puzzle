import random

def acak_papan():
    angka = list(range(1, 9)) + [0]
    random.shuffle(angka)
    return [angka[i:i+3] for i in range(0, len(angka), 3)]

def tampilkan_papan():
    print("\nPapan:")
    for row in grid:
        print(' '.join([str(x) if x != 0 else ' ' for x in row]))
    print()

def cek_berurutan():
    angka = [num for row in grid for num in row]
    return angka == list(range(1, 9)) + [0]

def temukan_kosong():
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return i, j

def gerakkan_angka(i, j):
    kosong_i, kosong_j = temukan_kosong()
    if abs(kosong_i - i) + abs(kosong_j - j) == 1:  # Mengecek apakah angka di sebelah ruang kosong
        grid[kosong_i][kosong_j], grid[i][j] = grid[i][j], grid[kosong_i][kosong_j]
        tampilkan_papan()
        if cek_berurutan():
            print("Selamat, Kamu Menang!")
            return True
    return False

def mulai_ulang():
    global grid
    grid = acak_papan()
    tampilkan_papan()

# Inisialisasi permainan
grid = acak_papan()
tampilkan_papan()

# Permainan berlangsung
while True:
    if cek_berurutan():
        print("Selamat, Kamu Menang!")
        break
    
    # Input perintah pemain
    try:
        move = input("Masukkan posisi angka yang ingin digerakkan (1-8) atau 'x' untuk keluar: ")
        if move == 'x':
            print("Permainan Selesai.")
            break

        move = int(move)
        found = False
        for i in range(3):
            for j in range(3):
                if grid[i][j] == move:
                    if gerakkan_angka(i, j):
                        found = True
                    break
            if found:
                break
        else:
            print("Angka tidak ditemukan atau tidak dapat digerakkan!")
    except ValueError:
        print("Input tidak valid, masukkan angka dari 1 sampai 8 atau 'x' untuk keluar.")