from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

# Tentukan path ke Microsoft Edge binary
options = Options()
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Tentukan path ke profil Edge Anda
user_profile = r"C:\Users\Iphone-8Pro\AppData\Local\Microsoft\Edge\User Data"  # Ganti "Username" dengan nama user Anda
options.add_argument(f"user-data-dir={user_profile}")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
# options.add_argument("--headless")  # Jika Anda ingin menjalankan Edge dalam mode headless (tanpa GUI)

# Tentukan path ke EdgeDriver
service = Service(executable_path=r"C:\webdriver\msedgedriver.exe")

# Buat instance WebDriver dengan service dan options yang telah diatur
driver = webdriver.Edge(service=service, options=options)

# Membuka halaman Facebook
try:
    driver.get("https://www.fb.com/")
except Exception as e:
    print(f"Error: {e}")

time.sleep(50)  # Tunggu selama 50 detik atau sesuaikan sesuai kebutuhan
