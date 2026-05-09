from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_opens():
    # Configura el driver automáticamente
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Abre una página
    driver.get("https://www.google.com")
    print(f"\nTítulo de la página: {driver.title}")
    
    # Pausa de 3 segundos para que veas que funciona
    time.sleep(3)
    driver.quit()