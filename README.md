# submission
submission dicoding kelas belajar analisis data

# deskripsi proyek
Proyek ini bertujuan untuk menganalisis pola penggunaan layanan bike sharing menggunakan data riwayat penyewaan sepeda. Dataset yang digunakan memiliki informasi tentang informasi waktu, musim, serta kondisi cuaca yang cocok digunakan untuk analisis yang menggunakan beberapa faktor. Analisis ini diharapkan dapat memberikan insight yang berguna dalam pengambilan keputusan, seperti peningkatan jumlah pengguna dan peningkatan layanan.

# tujuan analisis
- Mengetahui pengaruh musim terhadap jumlah penyewaan sepeda
- Menganalisis hubungan kondisi cuaca dengan jumlah pengguna
- Mengidentifikasi jam sibuk (peak hours) penggunaan sepeda
- Membandingkan pola penggunaan antara hari kerja dan akhir pekan

# dataset
dataset yang digunakan adalah https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view?usp=sharing
Fitur utama dataset:
dteday, hr → informasi waktu
season, mnth, weekday → informasi temporal
weathersit, temp, hum, windspeed → kondisi cuaca
casual, registered, cnt → jumlah penyewaan sepeda

# tools
- pyton
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab
- streamlit (untuk menjalankan dashboard)

# proses analisis
 - Pertanyaan 1: Seberapa besar pengaruh kondisi cuaca (weathersit, temp, hum, windspeed) terhadap jumlah penyewaan sepeda (cnt) pada hari kerja dibandingkan hari libur selama tahun 2011–2012?
SMART:
Specific: Fokus pada variabel cuaca + perbandingan hari kerja vs libur
Measurable: Bisa pakai korelasi, regresi, atau feature importance
Action-Oriented: Bisa bantu operator menentukan strategi saat cuaca buruk
Relevant: Cuaca = faktor utama di dataset
Time-bound: Tahun 2011–2012
- Pertanyaan 2: Pada jam berapa (hr) terjadi puncak penyewaan sepeda (cnt) dan bagaimana perbedaannya antara pengguna casual dan registered selama hari kerja di tahun 2012?
SMART:
Specific: Fokus ke jam (hr), tipe user (casual vs registered)
Measurable: Peak hour (nilai maksimum cnt)
Action-Oriented: Bisa optimasi distribusi sepeda
Relevant: Penting untuk operasional bike sharing
Time-bound: Tahun 2012

## data wrangling
1. Gathering Data
Dataset dimuat ke dalam DataFrame menggunakan library Pandas
2. Assessing Data
Permasalahan yang ditemukan:
Terdapat missing values pada beberapa kolom
Nilai kategori masih berupa angka (inconsistent value)
Tipe data belum sesuai (datetime belum dikonversi)
3. Cleaning Data
Langkah yang dilakukan:
Menangani missing values
Mengubah tipe data ke format datetime
Melakukan mapping kategori:
Season → Spring, Summer, Fall, Winter
Weather → Clear, Mist, Light Rain, Heavy Rain

## Exploratory Data Analysis (EDA)
Analisis dilakukan untuk menjawab pertanyaan bisnis:
Analisis 1: Pengaruh Cuaca
Mengelompokkan data berdasarkan kondisi cuaca
Menghitung rata-rata jumlah penyewaan
Analisis 2: Pola Jam Penggunaan
Mengelompokkan data berdasarkan jam
Mengidentifikasi jam dengan jumlah penyewaan tertinggi

## Visualization & Explanatory Analysis
Visualisasi yang digunakan:
Grafik rata-rata penyewaan berdasarkan kondisi cuaca
Grafik jumlah penyewaan berdasarkan jam
Hasil visualisasi menunjukkan pola yang jelas terkait faktor cuaca dan waktu terhadap penggunaan sepeda.

## insight hasil analisis
- Penggunaan sepeda tertinggi terjadi pada jam sibuk (pagi dan sore hari)
- Musim Summer dan Fall memiliki jumlah penyewaan tertinggi
- Kondisi cuaca cerah meningkatkan jumlah penyewaan secara signifikan
- Pola penggunaan pada hari kerja berbeda dengan akhir pekan

## rekomendasi
- Menambah ketersediaan sepeda pada jam sibuk
- Memaksimalkan operasional pada musim dengan permintaan tinggi
- Memberikan promo saat kondisi cuaca kurang mendukung
- Menyesuaikan strategi layanan antara hari kerja dan akhir pekan

# cara menjalankan Project
1. Menjalankan Analisis di Google Colab
Buka file notebook melalui link Google Colab
Klik Runtime → Run All untuk menjalankan seluruh proses analisis
Pastikan semua proses berjalan tanpa error
2. Menyimpan Dataset Hasil Analisis
Setelah proses analisis selesai, simpan dataset yang sudah dibersihkan:
main_data.to_csv("main_data.csv", index=False)
Kemudian download file tersebut dari Colab ke komputer lokal.
3. Menyiapkan Project di Lokal
Pindahkan file main_data.csv ke dalam folder project
Contoh:
bike-sharing-analysis/
│── main_data.csv
│── dashboard.py
4. Install Dependencies
Jalankan perintah berikut di terminal:
pip install pandas matplotlib seaborn streamlit
5. Menjalankan Dashboard
Jalankan dashboard menggunakan Streamlit:
streamlit run app.py
Setelah itu, buka browser di:
http://localhost:8501
6. Hasil Akhir
Dataset hasil cleaning digunakan untuk dashboard
Dashboard menampilkan visualisasi interaktif
Insight dapat dianalisis secara langsung oleh user

# struktur folder
submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───data_1.csv
| └───data_2.csv
├───notebook.ipynb
├───README.md
└───requirements.txt

# dashboard
Dashboard dibuat menggunakan Streamlit untuk menampilkan hasil analisis secara interaktif, seperti:
- Filter berdasarkan kondisi cuaca
- Visualisasi penggunaan sepeda
- Analisis jam sibuk

# kesimpulan
Hasil akhir menunjukkan bahwa faktor utama yang memengaruhi penggunaan bike sharing adalah kondisi cuaca dan waktu. Dengan memahami pola ini, pengelola dapat meningkatkan efisiensi layanan serta pengalaman pengguna.
