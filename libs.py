class Motor:
    def __init__(self, tanggal,nama_pelapor, nomor_polisi, merk_type, warna, lokasi_kehilangan, keterangan, no_telp):
        self.tanggal = tanggal
        self.nama_pelapor = nama_pelapor
        self.nomor_polisi = nomor_polisi
        self.merk_type = merk_type
        self.warna = warna
        self.lokasi_kehilangan = lokasi_kehilangan
        self.keterangan = keterangan
        self.no_telp = no_telp


class Pelaporan:
    def __init__(self):
        self.laporan = []

    def tambah_laporan(self, motor: Motor):
        self.laporan.append(motor)

    def get_all_laporan(self):
        return self.laporan

