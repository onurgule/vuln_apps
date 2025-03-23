import sqlite3

# Basit bir veritabanı oluştur
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Örnek tablo oluştur
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()

# Örnek kullanıcı ekle
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
conn.commit()

print("=== Kullanıcı Giriş Ekranı ===")
username = input("Kullanıcı adı: ")
password = input("Şifre: ")

#  burada bilerek zafiyet ekledik!
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
print(f"[DEBUG] Sorgu: {query}")

cursor.execute(query)
result = cursor.fetchone()

if result:
    print(f"Giriş başarılı. Hoşgeldin {result[1]}!")
else:
    print("Giriş başarısız.")

conn.close()
