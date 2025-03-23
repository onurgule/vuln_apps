import os

print("=== Ping Aracı ===")
ip_address = input("Ping atmak istediğiniz IP adresini girin: ")

# bilerek zafiyet ekledik burada!
command = f"ping -c 2 {ip_address}"
print(f"[DEBUG] Çalıştırılan komut: {command}")
os.system(command)
