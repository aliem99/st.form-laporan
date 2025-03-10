import streamlit as st
from libs import Motor, Pelaporan

st.title("Laporan sepeda motor hilang")

if "laporan" not in st.session_state:
    st.session_state.laporan = Pelaporan()

page = st.sidebar.selectbox("Menu", ["Form laporan", "Daftar Laporan"])

if page == "Form laporan":
  with st.form("motor_form"):
      st.write("Form laporan")
      tanggal = st.date_input("Tanggal Kejadian", value=None)
      nama_pelapor = st.text_input("Nama Pelapor")
      nomor_polisi = st.text_input("Nomor Polisi")
      merk_type = st.text_input("Merk/Type")
      warna = st.text_input("Warna")
      lokasi_kehilangan = st.text_input("Lokasi Kehilangan")
      keterangan = st.text_area("Keterangan")
      no_telp = st.text_input("Nomor Telepon Pelapor")
      
      submit_btn = st.form_submit_button(label="Tambah Laporan")

      if submit_btn:
          
          if not tanggal or not nama_pelapor or not nomor_polisi or not merk_type or not warna or not lokasi_kehilangan or not keterangan or not no_telp:
            st.error("Semua field harus diisi sebelum laporan dapat ditambahkan!")
          else:                 
            motor = Motor(tanggal, nama_pelapor, nomor_polisi, merk_type, warna, lokasi_kehilangan, keterangan, no_telp)
            
            st.session_state.laporan.tambah_laporan(motor)
            st.success("Laporan berhasil ditambahkan!")

elif page == "Daftar Laporan":
    
    if st.session_state.laporan.get_all_laporan():
        st.write("Berikut adalah daftar laporan sepeda motor yang hilang:")

        for i, laporan in enumerate(st.session_state.laporan.get_all_laporan(), start=1):
            st.subheader(f"Laporan #{i}")
            st.write(f"**Tanggal Kejadian:** {laporan.tanggal}")
            st.write(f"**Nama Pelapor:** {laporan.nama_pelapor}")
            st.write(f"**Nomor Polisi:** {laporan.nomor_polisi}")
            st.write(f"**Merk/Type:** {laporan.merk_type}")
            st.write(f"**Warna:** {laporan.warna}")
            st.write(f"**Lokasi Kehilangan:** {laporan.lokasi_kehilangan}")
            st.write(f"**Keterangan:** {laporan.keterangan}")
            st.write(f"**Nomor Telepon Pelapor:** {laporan.no_telp}")
            st.write("---")
    else:
        st.write("Belum ada laporan yang ditambahkan.")