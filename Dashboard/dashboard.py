import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Gunakan raw URL dari GitHub untuk membaca dataset langsung
url_day = "https://raw.githubusercontent.com/ilham-mulia/Dicoding-Proyek-Analisis-Data/main/Data/day.csv"
url_hour = "https://raw.githubusercontent.com/ilham-mulia/Dicoding-Proyek-Analisis-Data/main/Data/hour.csv"

df_day = pd.read_csv(url_day)
df_hour = pd.read_csv(url_hour)

# Tambahkan kolom 'hour' pada df_day agar kompatibel dengan df_hour
df_day["hour"] = None  

# Gabungkan dataset berdasarkan tanggal (dteday)
df_combined = pd.concat([df_day, df_hour], ignore_index=True)

# url_main = "https://raw.githubusercontent.com/ilham-mulia/Dicoding-Proyek-Analisis-Data/main/Dashboard/main_data.csv"
# df_combined = pd.read_csv(url_main)

# Judul Dashboard
st.title("📊 Dashboard Analisis Penyewaan Sepeda 🚲")

# Sidebar - Pilihan Analisis
st.sidebar.header("🔍 Pilih Analisis:")
analisis = st.sidebar.radio("Pilih kategori:", ["Penyewaan per Bulan", "Penyewaan per Jam", "Pengaruh Cuaca"])

# Sidebar - Filter Interaktif
st.sidebar.header("🎛 Filter Data")

default_start_date = pd.to_datetime("2011-01-01").date()
default_end_date = pd.to_datetime("2011-12-31").date()
selected_date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [default_start_date, default_end_date], min_value=pd.to_datetime("2011-01-01").date(), max_value=pd.to_datetime("2012-12-31").date())

if len(selected_date_range) == 2:
    start_date, end_date = selected_date_range
    df_day = df_day[(pd.to_datetime(df_day['dteday']).dt.date >= start_date) & (pd.to_datetime(df_day['dteday']).dt.date <= end_date)]
    df_hour = df_hour[(pd.to_datetime(df_hour['dteday']).dt.date >= start_date) & (pd.to_datetime(df_hour['dteday']).dt.date <= end_date)]

# 1️⃣ Visualisasi Penyewaan Sepeda per Bulan
if analisis == "Penyewaan per Bulan":
    st.subheader("📅 Rata-rata Penyewaan Sepeda per Bulan")
    plt.figure(figsize=(10, 5))
    sns.barplot(x="mnth", y="cnt", data=df_day, palette="Blues")
    plt.title("Rata-rata Penyewaan Sepeda per Bulan")
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Penyewaan Sepeda")
    plt.xticks(ticks=range(12), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    st.pyplot(plt)

# 2️⃣ Visualisasi Penyewaan Sepeda per Jam
elif analisis == "Penyewaan per Jam":
    st.subheader("⏰ Tren Penyewaan Sepeda Berdasarkan Jam")
    plt.figure(figsize=(10, 5))
    sns.lineplot(x="hr", y="cnt", data=df_hour, marker="o", color="red")
    plt.title("Tren Penyewaan Sepeda Berdasarkan Jam")
    plt.xlabel("Jam")
    plt.ylabel("Jumlah Penyewaan Sepeda")
    plt.xticks(range(0, 24))
    plt.grid()
    st.pyplot(plt)

# 3️⃣ Visualisasi Pengaruh Cuaca terhadap Penyewaan
elif analisis == "Pengaruh Cuaca":
    st.subheader("🌦️ Pengaruh Cuaca terhadap Penyewaan Sepeda")
    plt.figure(figsize=(10, 5))
    sns.boxplot(x="weathersit", y="cnt", data=df_day, palette="coolwarm")
    plt.title("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Jumlah Penyewaan Sepeda")
    plt.xticks(ticks=[0, 1, 2, 3], labels=["Cerah", "Mendung", "Hujan Ringan", "Hujan Lebat"])
    st.pyplot(plt)

# Footer
st.markdown("---")
st.markdown("🚀 **Dashboard ini dibuat dengan Streamlit**")
