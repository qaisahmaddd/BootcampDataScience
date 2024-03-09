import unittest # ini wajib ditulis untuk menandakan kita akan melakukan unit test
from ahmadqais_app import ShoppingCart # ahmadqais_app adalah nama file, sedangkan ShoppingCart adalah nama class


class TestShoppingCart(unittest.TestCase):
    # setUp digunakan untuk membentuk object dari class Shopping Cart
    def setUp(self):
        datas = []
        self.shopping_cart = ShoppingCart(datas)
    
    def test_tambah_barang(self):
        result = self.shopping_cart.tambah_barang('Apel', '10000')

        # assertEqual artinya membandingkan 2 buah nilai apakah sama atau tidak
        # assertEqual(nilai_pertama, nilai_kedua, kalo_nilainya_tidak_sama_maka_tampilkan_apa)
        self.assertEqual(result[0].nama, 'Apel', 'Nama barang seharusnya Apel')
        self.assertEqual(result[0].harga, '10000', 'Harga barang seharusnya 10000')

        """
        Notes : kita menggunakan index ke 0 karena data yang kita tambahkan cuman 1, artinya data cuman ada di index ke 0
        """

    def test_hapus_barang(self):
        # insert data
        result = self.shopping_cart.tambah_barang('Apel', '10000')
        result = self.shopping_cart.tambah_barang('Jeruk', '20000')

        # setelah proses insert, data pasti sudah terisi dengan Apel dan Jeruk

        # delete data
        result = self.shopping_cart.hapus_barang('Apel')

        self.assertEqual(result[0].nama, 'Jeruk', 'Nama barang seharusnya Jeruk')
        self.assertEqual(result[0].harga, '20000', 'Harga barang seharusnya 20000')
    
    def test_hitung_total(self):
        # insert data
        result = self.shopping_cart.tambah_barang('Apel', '10000')
        result = self.shopping_cart.tambah_barang('Jeruk', '50000')

        result = self.shopping_cart.hitung_total()
        self.assertEqual(result, 60000, 'Total harga seharusnya 60000')
    
    def test_tampilkan_cart(self):
        # insert data
        result = self.shopping_cart.tambah_barang('Apel', '10000')
        result = self.shopping_cart.tambah_barang('Jeruk', '50000')

        result = self.shopping_cart.tampilkan_cart()
        
        # \n wajib ditulis agar tulisan ke enter ke bawah
        statement = "0. Apel - Rp 10000.00\n1. Jeruk - Rp 50000.00\n"
        self.assertEqual(result, statement)


if __name__ == '__main__':
    unittest.main()