# 📊 Twitter Analytics App

## 📌 Deskripsi Aplikasi
Twitter Analytics App adalah aplikasi berbasis Streamlit yang digunakan untuk menganalisis percakapan di Twitter berdasarkan kata kunci atau hashtag tertentu. Aplikasi ini memungkinkan pengguna untuk mendapatkan data dari Twitter, melakukan analisis eksploratif (EDA), menganalisis sentimen tweet, serta mendeteksi topik pembicaraan yang sedang berkembang.

## ⚡ Fitur Utama
1. **📥 Download Data Twitter**
   - Mengambil data percakapan berdasarkan kata kunci atau hashtag tertentu.
   - Batas jumlah tweet yang dapat diambil ditentukan oleh pengguna.

2. **📊 Exploratory Data Analysis (EDA)**
   - Menampilkan statistik dasar seperti jumlah akun yang berinteraksi, total tweet, total engagement (likes, retweets, replies, shares).
   - Analisis time series untuk melihat tren tweet berdasarkan waktu.
   - Visualisasi data dalam bentuk grafik (barchart, line chart).
   - Menampilkan akun/top tweet dengan engagement tertinggi.
   - Feedback AI terkait hasil analisis untuk wawasan tambahan.

3. **😊 Analisis Sentimen**
   - Menggunakan model OpenAI `gpt-4o-mini` untuk menganalisis sentimen tweet (positif, negatif, atau netral).
   - Menampilkan ringkasan total tweet per sentimen.
   - Feedback AI terkait pola sentimen yang terdeteksi.

4. **🗣️ Deteksi Topik Pembicaraan**
   - Menggunakan OpenAI untuk mengelompokkan dan mengidentifikasi topik utama dalam percakapan.
   - Ringkasan dalam bentuk teks untuk memahami tren yang sedang berkembang.
   - Feedback AI terkait konteks diskusi berdasarkan topik yang ditemukan.

## 🚀 Cara Menjalankan Aplikasi
1. **Persyaratan yang Diperlukan**
   - Python (>=3.9)
   - Streamlit
   - Tweepy
   - OpenAI API Key
   - Pandas, Matplotlib, Seaborn

2. **Instalasi Dependensi**
   ```sh
   pip install -r requirements.txt
   ```
   Jika terdapat masalah dengan dependensi, pastikan untuk menginstal ulang `openai` dengan:
   ```sh
   pip install --upgrade openai
   ```

3. **Menjalankan Aplikasi**
   ```sh
   streamlit run app.py
   ```

4. **Masukkan API Key OpenAI**
   - Saat aplikasi berjalan, masukkan OpenAI API Key di sidebar untuk mengaktifkan analisis sentimen dan deteksi topik.

## 🔍 Contoh Kueri Twitter yang Didukung
Berikut beberapa contoh pencarian yang dapat dilakukan:
- `"elon musk"` → Menganalisis percakapan tentang Elon Musk.
- `"#AI"` → Mengambil data terkait AI dari hashtag.
- `"tesla OR spacex"` → Menganalisis topik terkait Tesla dan SpaceX.
- `"from:elonmusk"` → Menganalisis tweet yang hanya berasal dari akun Elon Musk.
- `"dogecoin min_faves:100"` → Menganalisis tweet tentang Dogecoin dengan minimal 100 likes.

## 📌 Catatan Tambahan
- Pastikan API Key OpenAI valid dan memiliki cukup kuota untuk analisis.
- Jika terjadi error koneksi, coba jalankan ulang aplikasi atau periksa koneksi internet.
- Analisis sentimen dan topik memerlukan beberapa detik karena menggunakan API OpenAI.

---
✨ **Twitter Analytics App membantu Anda memahami tren, sentimen, dan topik hangat di Twitter dengan lebih mendalam!**

