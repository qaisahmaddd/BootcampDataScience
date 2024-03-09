'''
=================================================
Graded Challenge 1

Nama  : Ahmad Qais
Batch : RMT-026

Program ini dibuat untuk melakukan automatisasi transaksi belanja dengan empat fitur:
1. Menambah barang dan harga
2. Hapus barang
3. Cek barang yang ada di keranjang
4. Menghitung total belanjaan

Program ini memiliki dua kelas utama dengan beberapa fungsi di dalamnya

Mohon maaf nama file tidak bisa mengandung dash  " - " karena terkait dengan file _test.py 
=================================================
'''

class CartItem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class ShoppingCart:
    def __init__(self, cart):
        self.cart = cart

    def tambah_barang(self, nama_barang, harga):
        # create object CartItem
        c = CartItem(nama_barang, harga)

        # append data into cart
        self.cart.append(c)
        
        # print out info
        print(f'Barang "{nama_barang}" berhasil dimasukkan ke keranjang')
        return self.cart
    
    def hapus_barang(self, nama_barang):
        idx = -1

        for index, value in enumerate(self.cart):
            if value.nama == nama_barang:
                idx = index
                break # untuk membuat perulangan berhenti secara paksa

        # menghapus data dari list
        if idx != -1:
          self.cart.pop(idx)
          """
          Artinya :
              Jika nama pada object Cart == nama barang yang diinput oleh user, maka ...
              value dari idx adalah INDEX OBJECT TERSEBUT

          # menghapus data pada list -> pop(index)
          """

          print(f'Barang "{nama_barang}" berhasil dihapus')
        else:
            print(f'Barang "{nama_barang}" tidak ditemukan')
        return self.cart
    
    def hitung_total(self):
        # variable penampung
        total = 0

        # Looping cart to get price (harga)
        for value in self.cart:
            total += int(value.harga)

        print(f"Total belanja: Rp {total:.2f}")
        return total

    def tampilkan_cart(self):
        statement = ""
        print("Barang yang dikeranjang :")
        
        # Looping cart
        for index, value in enumerate(self.cart):
            print(f'{str(index)}. {value.nama} - Rp {int(value.harga):.2f}')
            statement += f'{str(index)}. {value.nama} - Rp {int(value.harga):.2f}\n'

        return statement
    def play(self):
        try:
            menu = 0
            while menu != 5:
                print("MENU")
                print("1. Menambah Barang")
                print("2. Hapus Barang")
                print("3. Tampilkan Barang di Keranjang")
                print("4. Lihat Total Belanja")
                print("5. Exit")
                menu = int(input("Masukkan menu yang diinginkan : "))
                if menu == 1:
                    # input data
                    nama_barang = input("Masukkan nama barang : ")
                    harga = input("Masukkan harga : ")
                    self.tambah_barang(nama_barang, harga)
                elif menu == 2:
                    nama_barang =  input("Masukkan nama barang yang ingin dihapus :")
                    self.hapus_barang(nama_barang)
                elif menu == 3:
                    self.tampilkan_cart()
                elif menu == 4:
                    self.hitung_total()
                elif menu != 5:
                    print("Pilihannya salah. Coba lagi ya.")
        except: # code dibawah akan dieksekusi ketika ada error yang terjadi di proses input
            print("Pilihannya salah. Coba lagi ya.")
            self.play()

if __name__ == '__main__':
    datas = []
    sc = ShoppingCart(datas)
    sc.play()
