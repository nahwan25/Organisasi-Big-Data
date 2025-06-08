import streamlit as st
from cassandra_connector import ambil_data_dari_cassandra
from mongo_connector import ambil_data_dari_mongodb
import pandas as pd

# Fungsi aggregator
def gabungkan_semua_data2():
    data_cassandra = ambil_data_dari_cassandra()
    data_mongodb = ambil_data_dari_mongodb()
    return data_cassandra + data_mongodb

# UI Streamlit
st.set_page_config(page_title="Data Gabungan", layout="wide")
st.title("📊 Dashboard Data Gabungan: Cassandra + MongoDB")

# Ambil data
with st.spinner("Mengambil data dari Cassandra dan MongoDB..."):
    data = gabungkan_semua_data2()

if data:
    df = pd.DataFrame(data)
    
    st.success(f"✅ Berhasil mengambil {len(df)} data!")
    
    # Tampilkan tabel interaktif
    st.dataframe(df)

    # Filter berdasarkan sumber
    sumber = st.selectbox("Filter berdasarkan sumber data:", ["Semua", "Cassandra", "MongoDB"])
    if sumber != "Semua":
        df = df[df["sumber"] == sumber]
        st.dataframe(df)

    # Export opsi
    if st.button("Download CSV"):
        st.download_button("📥 Download data sebagai CSV", data=df.to_csv(index=False), file_name="data_gabungan.csv", mime="text/csv")
else:
    st.warning("❌ Data kosong atau gagal diambil.")
