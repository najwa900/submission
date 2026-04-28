import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Fungsi untuk load data agar lebih cepat (caching)
@st.cache_data
def load_data():
    
    df = pd.read_csv("dashboard/main_data.csv")
    return df

df = load_data()


with st.sidebar:
    st.title("Bike Sharing Analysis 🚲")
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Filter Musim (Season)
    season_filter = st.multiselect(
        label="Pilih Musim:",
        options=df['season'].unique(),
        default=df['season'].unique()
    )

# Filter data berdasarkan pilihan di sidebar
main_df = df[df['season'].isin(season_filter)]


st.title("Proyek Analisis Data: Bike Sharing Dataset")

# Menampilkan Metric Sederhana (Total Penyewaan)
col1, col2 = st.columns(2)
with col1:
    total_rentals = main_df['cnt'].sum()
    st.metric("Total Penyewaan", value=f"{total_rentals:,}")
with col2:
    avg_rentals = round(main_df['cnt'].mean(), 2)
    st.metric("Rata-rata Penyewaan", value=avg_rentals)

st.divider()

# Visualisasi 1: Berdasarkan Cuaca
st.subheader("Seberapa besar pengaruh kondisi cuaca (weathersit, temp, hum, windspeed) 
terhadap jumlah penyewaan sepeda (cnt) pada hari kerja dibandingkan hari libur selama tahun 2011–2012?")
st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(
    x='weathersit', 
    y='cnt', 
    data=main_df, 
    ax=ax, 
    palette='rocket'
)
ax.set_title("Rata-rata Penyewaan per Kondisi Cuaca", fontsize=15)
st.pyplot(fig)

# Visualisasi 2: Berdasarkan Jam (Pola Harian)
st.subheader("Pada jam berapa (hr) terjadi puncak penyewaan sepeda (cnt) dan bagaimana perbedaannya 
antara pengguna casual dan registered selama hari kerja di tahun 2012?")
st.subheader("Pola Penyewaan Sepeda per Jam")
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.lineplot(
    x='hr', 
    y='cnt', 
    hue='workingday', 
    data=main_df, 
    ax=ax2
)
ax2.set_title("Pola Penyewaan: Hari Kerja vs Hari Libur", fontsize=15)
st.pyplot(fig2)

st.caption('Copyright © 2026 | Penulis: [Najwanz]')

with st.expander("Lihat Detail Analisis"):
    st.write("**Kesimpulan Pertanyaan 1:** Cuaca cerah meningkatkan penyewaan hingga 3x lipat dibanding cuaca hujan. Di hari kerja, penurunan akibat cuaca tidak se-ekstrem di hari libur karena adanya kebutuhan transportasi wajib.")
    st.write("**Kesimpulan Pertanyaan 2:** Puncak aktivitas terjadi jam 8 pagi dan 5 sore. Pengguna Registered sangat mendominasi jam sibuk, sementara pengguna Casual lebih banyak di tengah hari.")
