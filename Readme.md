# Bike Sharing Dashboard 🚲

Dashboard ini dibuat untuk menganalisis pola penggunaan sepeda berdasarkan dataset Bike Sharing dari Washington D.C. tahun 2011-2012. Dashboard ini dibangun menggunakan **Python, Pandas, Matplotlib, Seaborn, dan Streamlit**.

## 🌐 Akses Dashboard
Akses dashboard yang sudah dideploy di Streamlit melalui link berikut:
[https://dicoding-ilham-mulia.streamlit.app/](https://dicoding-ilham-mulia.streamlit.app/)

## 📂 Struktur Direktori
```
Bike-Sharing-Dashboard/
│── Dashboard/
│   │── run.py
│   │── main_data.csv
│── Data/
│   │── Readme.txt
│   │── day.csv
│   │── hour.csv
│── Notebook.ipynb
│── requirements.txt
│── README.md
│── url.txt
```

## 📦 Setup Environment - Anaconda
```bash
conda create --name bike-sharing python=3.9
conda activate bike-sharing
pip install -r requirements.txt
```

## 🛠️ Setup Environment - Shell/Terminal
```bash
mkdir bike_sharing_dashboard
cd bike_sharing_dashboard
pipenv install
pipenv shell
pip install -r requirements.txt
```

## 🚀 Jalankan Streamlit App
```bash
python -m streamlit run Dashboard/dashboard.py
```
