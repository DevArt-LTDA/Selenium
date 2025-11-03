import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test1(driver):

    # === PRIMER CASO: LOGIN INVÁLIDO ===
    print("=== PRIMER CASO: LOGIN INVÁLIDO ===")
    driver.get("https://devartcl.vercel.app/login")

    element1 = driver.find_element(By.ID, "email")
    print("Campo:", element1.get_attribute("id"))
    element1.click()
    element1.send_keys("correo_invalido@asd.asd")

    element2 = driver.find_element(By.ID, "password")
    print("Campo:", element2.get_attribute("id"))
    element2.click()
    element2.send_keys("clave123")

    time.sleep(1)

    element3 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print("Botón:", element3.text)
    element3.click()

    time.sleep(2)
    print("Primer caso probado exitosamente. El sistema NO dejó iniciar sesión.")

    # === SEGUNDO CASO: REGISTRO NUEVO ===
    print("\n=== SEGUNDO CASO: REGISTRO NUEVO ===")
    driver.get("https://devartcl.vercel.app/register")

    element1 = driver.find_element(By.ID, "fullName")
    print("Campo:", element1.get_attribute("id"))
    element1.click()
    element1.send_keys("Usuario de Prueba")

    element2 = driver.find_element(By.ID, "username")
    print("Campo:", element2.get_attribute("id"))
    element2.click()
    element2.send_keys("usuario_prueba")

    element3 = driver.find_element(By.ID, "email")
    print("Campo:", element3.get_attribute("id"))
    element3.click()
    correo_nuevo = f"usuario{int(time.time())}@gmail.com"
    element3.send_keys(correo_nuevo)

    element4 = driver.find_element(By.ID, "password")
    print("Campo:", element4.get_attribute("id"))
    element4.click()
    element4.send_keys("clave123")

    element5 = driver.find_element(By.ID, "confirmPassword")
    print("Campo:", element5.get_attribute("id"))
    element5.click()
    element5.send_keys("clave123")
    
    element6 = driver.find_element(By.ID, "birthDate")
    print("Campo:", element6.get_attribute("id"))
    element6.click()
    element6.send_keys("12-12-1990")

    element7 = driver.find_element(By.ID, "terms")
    print("Campo:", element7.get_attribute("id"))
    driver.execute_script("arguments[0].click();", element7)




    time.sleep(1)

    element5 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print("Botón:", element5.text)
    element5.click()

    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    print("Segundo caso probado exitosamente. El sistema redirigió al login.")

    # === TERCER CASO: LOGIN VÁLIDO ===
    print("\n=== TERCER CASO: LOGIN VÁLIDO ===")
    driver.get("https://devartcl.vercel.app/login")

    element1 = driver.find_element(By.ID, "email")
    print("Campo:", element1.get_attribute("id"))
    element1.click()
    element1.send_keys(correo_nuevo)

    element2 = driver.find_element(By.ID, "password")
    print("Campo:", element2.get_attribute("id"))
    element2.click()
    element2.send_keys("clave123")

    time.sleep(1)

    element3 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print("Botón:", element3.text)
    element3.click()

    #WebDriverWait(driver, 10).until(EC.url_to_be("https://devartcl.vercel.app"))
    print("Tercer caso probado exitosamente. El sistema redirigió al home.")

    time.sleep(3)
    print("\n=== TODAS LAS PRUEBAS FINALIZADAS ===")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    test1(driver)
    driver.quit()
