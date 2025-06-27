from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# dri081
if __name__ == '__main__':
    languages = {
        "en": 1,
        "fr": 2,
        "de": 3,
        "sp": 4,
        "it": 5,
        "s-ch": 6,
        "ja": 7,
        "po": 8,
        "ko": 10,
        "t-ch": 11
    }

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

    option = webdriver.ChromeOptions()
    option.add_argument(f'user-agent={user_agent}')
    option.add_argument('--headless')
    option.add_argument("--disable-infobars")
    option.add_argument("--disable-extensions")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--incognito")
    driver = webdriver.Chrome(options=option)

    while True:
        driver.get("https://www.cardmarket.com/en/Pokemon")

        print("Karten ID:")
        cardId = input()
        print("Sprache eingeben (en, fr, de, sp, it, s-ch, ja, po, ko, t-ch):")
        language = input()

        if(cardId == "" or language == ""):
            driver.close()
            exit(0)

        try:
            languageId = languages[language]
        except:
            print("Ungültige Sprache")
            continue

        try:
            searchInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//input[@id='ProductSearchInput']")))
        except:
            driver.save_screenshot("screenshot.png")
            print("Seite konnte nicht geladen werden!")
            driver.close()
            exit(1)

        searchInput.send_keys(cardId)
        searchInput.send_keys(Keys.ENTER)

        try:
            driver.get(driver.current_url + "?language=" + str(languageId))
        except:
            driver.save_screenshot("screenshot.png")
            print("Sprache konnte nicht ausgewählt werden!")
            driver.close()
            exit(1)

        try:
            rows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, f"//div[contains(@id, 'articleRow')]")))
            price = rows[0].find_element(By.XPATH, f"//div[@class='col-offer col-auto']//span[last()]").get_attribute('innerHTML')
            print(price)
        except:
            driver.save_screenshot("screenshot.png")
            print("Seite konnte nicht geladen werden!")
            driver.close()
            exit(1)
