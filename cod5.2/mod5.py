import pandas as pd

# Membaca file CSV
data = pd.read_csv(r'D:\smester 5\fungsional prak\code\cod5.2\data.CSV')

# Menampilkan 5 baris pertama
print("5 data pertama")
print(data.head())

# Menampilkan informasi DataFrame
print("data info")
data.info()

# Menampilkan statistik
print("data statistik")
print(data.describe())

# Menampilkan kolom tertentu
print("data Calories")
print(data['Calories'])

# Menampilkan nama kolom
print("nama data")
print("Nama kolom:", data.columns)

# Memeriksa apakah kolom 'Maxpules' ada sebelum memfilter
print("data lebih dari 135")
if 'Maxpules' in data.columns:
    filtered_data = data[data['Maxpules'] > 135]
    print(filtered_data)
else:
    print("Kolom 'Maxpules' tidak ditemukan dalam data.")
