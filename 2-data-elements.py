#import library
import pandas as pd
import streamlit as st
import numpy as np 
import altair as alt 

# Menampilkan judul dan deskripsi
st.title("Praktikum 1 - Visualisasi Data") #menampilkan judul halaman diutama
st.caption("Bagian 2 : Data Elements") #menampilkan keterangan bagian

#st.markdown digunakan untuk menampilkan teks dengan format Markdown (bullet list, bold, italic, dll.)
st.markdown("""
Kelompok 19 :
- Muhammad Daffa Shafwan - 0110222275
- Dewi Nuraini – 0110122122 
- Muhammad Saputra Adi Firmansyah – 0110222105 
""")

#Data frame : struktur data terbentuk tabel (baris dan kolom) yang disediakan oleh library pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

#menampilkan data frame
st.dataframe(df)

#Highlight nilai minimum
st.subheader("Highlight Minimum Value di DataFrame")

#highlight nilai terkecil disetiap kolam dataframe
#axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

#tabel statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

#menampilkan tabel statis
st.table(df)

#metrics: komponen tampilan angka penting
st.subheader("Metrics")
st.metric(label="Temperature", value="31 °C", delta="1.2 °C")#kenaikan 1.2 °C

#metrics sesuai delta_color
#delta_color digunakan untuk memberi warna sesuai arah perubahan:
# - "normal" (default) : naik -> hijau, turun -> merah
# - "inverse" : kebalikannya (naik -> merah)
# - "off" tidak menampilkan warna perubahan

#mendefinisikan variabel metrics
col1, col2, col3 = st.columns(3)

#menampilkan indikator data
col1.metric("Curah Hujan", "100 cm","10 cm" )#naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") # naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10,
delta_color="off") # netral

#menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) #kosong #naik baik karena di setting default
st.metric("Trees", "91456", "-1132649") #penurunan

