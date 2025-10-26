# Program Data Penjualan Sederhana (Simple Sales Data Program)

# Struktur data untuk menyimpan semua data penjualan
# Format: { 'nama_produk': [jumlah_terjual, harga_satuan, total_pendapatan_produk] }
data_penjualan = {}

# Fungsi untuk Input data penjualan
# Keterangan: Nama produk, jumlah terjual, harga satuan
def input_data_penjualan():
    print("\n--- Input Data Penjualan ---")
    nama_produk = input("Masukkan Nama Produk: ").strip()

    # Validasi input numerik
    while True:
        try:
            jumlah_terjual = int(input("Masukkan Jumlah Terjual: "))
            if jumlah_terjual < 0:
                print("Jumlah terjual tidak boleh negatif.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka untuk jumlah terjual.")

    while True:
        try:
            harga_satuan = float(input("Masukkan Harga Satuan (Rp): "))
            if harga_satuan < 0:
                print("Harga satuan tidak boleh negatif.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka untuk harga satuan.")

    # Hitung otomatis total pendapatan per produk
    total_pendapatan_produk = jumlah_terjual * harga_satuan

    # Simpan atau update data
    data_penjualan[nama_produk] = [jumlah_terjual, harga_satuan, total_pendapatan_produk]
    print(f"\n✅ Data penjualan untuk '{nama_produk}' berhasil disimpan/diperbarui.")


# Fungsi untuk Hitung otomatis Total pendapatan per produk & keseluruhan
def hitung_ringkasan_penjualan():
    print("\n--- Ringkasan Penjualan ---")

    if not data_penjualan:
        print("Belum ada data penjualan yang tercatat.")
        return

    total_pendapatan_keseluruhan = 0

    print(f"{'Produk':<20} | {'Jumlah':<8} | {'Harga Satuan':<15} | {'Total Pendapatan':<18}")
    print("-" * 65)

    # Iterasi melalui data untuk menampilkan per produk dan menghitung total keseluruhan
    for produk, data in data_penjualan.items():
        jumlah, harga, total_produk = data
        total_pendapatan_keseluruhan += total_produk
        print(f"{produk:<20} | {jumlah:<8} | Rp{harga:,.2f}{'':<12} | Rp{total_produk:,.2f}{'':<15}")

    print("-" * 65)
    print(f"💰 Total Pendapatan Keseluruhan: Rp{total_pendapatan_keseluruhan:,.2f}")

# Fungsi untuk Dapat dikembangkan (Contoh: Menampilkan Laporan Sederhana)
def tampilkan_laporan_sederhana():
    """Simulasi fitur ekspor laporan ke file, grafik penjualan, dll."""
    hitung_ringkasan_penjualan()
    print("\n💡 Fitur ini dapat dikembangkan lebih lanjut, misalnya:")
    print("   - Mengekspor data ringkasan ke file CSV/Excel.")
    print("   - Menghasilkan visualisasi grafik penjualan bulanan.")
    print("   - Menambahkan fitur filtering atau sorting data.")
    
# Fungsi utama untuk Menu interaktif
# Keterangan: Mudah digunakan untuk siswa PKWU
def menu_interaktif():
    while True:
        print("\n==============================")
        print("  📊 Program Data Penjualan PKWU")
        print("==============================")
        print("1. Input Data Penjualan")
        print("2. Lihat Ringkasan Penjualan (Hitung Otomatis)")
        print("3. Tampilkan Potensi Pengembangan Laporan")
        print("4. Keluar")
        print("------------------------------")

        pilihan = input("Masukkan pilihan Anda (1-4): ")

        if pilihan == '1':
            input_data_penjualan()
        elif pilihan == '2':
            hitung_ringkasan_penjualan()
        elif pilihan == '3':
            tampilkan_laporan_sederhana()
        elif pilihan == '4':
            print("\nTerima kasih telah menggunakan program data penjualan. Sampai jumpa! 👋")
            break
        else:
            print("\n❌ Pilihan tidak valid. Silakan masukkan angka antara 1 sampai 4.")

# Jalankan program
if __name__ == "__main__":
    menu_interaktif()
