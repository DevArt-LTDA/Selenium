import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Función para rellenar campos letra por letra
def escribir_lento(elemento, texto, pausa=0.05):
    for letra in texto:
        elemento.send_keys(letra)
        time.sleep(pausa)


def test1(driver):

    # === PRIMER CASO: LOGIN INVÁLIDO ===
    print("=== PRIMER CASO: LOGIN INVÁLIDO ===")
    driver.get("https://devartcl.vercel.app/login")

    element1 = driver.find_element(By.ID, "email")
    print("Campo:", element1.get_attribute("id"))
    element1.click()
    escribir_lento(element1, "correo_invalido@asd.asd")
    time.sleep(1)

    element2 = driver.find_element(By.ID, "password")
    print("Campo:", element2.get_attribute("id"))
    element2.click()
    escribir_lento(element2, "clave123")
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
    escribir_lento(element1, "Usuario de Prueba")
    time.sleep(1)

    element2 = driver.find_element(By.ID, "email")
    print("Campo:", element2.get_attribute("id"))
    element2.click()
    correo_nuevo = f"usuario@duoc.cl"
    escribir_lento(element2, correo_nuevo)
    time.sleep(1)

    element3 = driver.find_element(By.ID, "username")
    print("Campo:", element3.get_attribute("id"))
    element3.click()
    escribir_lento(element3, "usuario_prueba")
    time.sleep(1)

    element4 = driver.find_element(By.ID, "password")
    print("Campo:", element4.get_attribute("id"))
    element4.click()
    escribir_lento(element4, "clave123")
    time.sleep(1)

    element5 = driver.find_element(By.ID, "confirmPassword")
    print("Campo:", element5.get_attribute("id"))
    element5.click()
    escribir_lento(element5, "clave123")
    time.sleep(1)
    
    element6 = driver.find_element(By.ID, "birthDate")
    print("Campo:", element6.get_attribute("id"))
    element6.click()
    escribir_lento(element6, "12-12-1990")
    time.sleep(1)

    element7 = driver.find_element(By.ID, "terms")
    print("Campo:", element7.get_attribute("id"))
    driver.execute_script("arguments[0].click();", element7)
    time.sleep(1)

    element5 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print("Botón:", element5.text)
    element5.click()

    print("Segundo caso probado exitosamente. El sistema redirigió al login.")

    # === TERCER CASO: LOGIN VÁLIDO ===
    print("\n=== TERCER CASO: LOGIN VÁLIDO ===")
    driver.get("https://devartcl.vercel.app/login")

    element1 = driver.find_element(By.ID, "email")
    print("Campo:", element1.get_attribute("id"))
    element1.click()
    escribir_lento(element1, correo_nuevo)
    time.sleep(1)

    element2 = driver.find_element(By.ID, "password")
    print("Campo:", element2.get_attribute("id"))
    element2.click()
    escribir_lento(element2, "clave123")
    time.sleep(1)

    element3 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print("Botón:", element3.text)
    element3.click()

    # Esperar a que cargue el home y mostrarlo 5 segundos
    WebDriverWait(driver, 10).until(EC.url_contains("devartcl.vercel.app"))
    print("Tercer caso probado exitosamente. El sistema redirigió al home.")
    time.sleep(2)

    print("\n=== TODAS LAS PRUEBAS FINALIZADAS ===")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    test1(driver)
    driver.quit()
