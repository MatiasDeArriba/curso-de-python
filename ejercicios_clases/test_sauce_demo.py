import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestSauceDemo:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        # Configuración inicial (Fixture)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10) # Espera implícita para estabilidad
        yield
        self.driver.quit() # Cierre del navegador (Finally)

    def test_full_workflow(self):
        driver = self.driver
        
        # --- ACTIVIDAD 1: Login ---
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Validaciones Actividad 1
        assert "/inventory.html" in driver.current_url
        # Reto extra: Validación del título
        assert driver.title == "Swag Labs"
        print("Test OK: Login exitoso")

        # --- ACTIVIDAD 2: Explora el Inventario ---
        title_element = driver.find_element(By.CLASS_NAME, "title")
        assert title_element.text == "Products"
        
        inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(inventory_items) > 0
        
        first_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        first_item_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"Producto: {first_item_name} | Precio: {first_item_price}")

        # --- ACTIVIDAD 3: Carrito Rápido ---
        # 1. Clic en "Add to cart" del primer producto
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        
        # 2. Verifica que el contador del carrito muestre 1
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.text == "1"
        
        # 3. Navega al carrito y comprueba el producto
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        item_in_cart = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert item_in_cart == first_item_name
        print("Test OK: Carrito verificado")