from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def _createDriver():
    option = webdriver.ChromeOptions()

    # Fake a non-headless browser, making sites with weak bot protection think you're a regular browser
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
    option.add_argument(f'user-agent={user_agent}')

    # Remove everything that the browser doesn't need to improve performance
    option.add_argument('--headless')
    option.add_argument("--disable-infobars")
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-blink-features=AutomationControlled")

    print("Starting selenium...")
    try:
        driver = webdriver.Chrome(options=option)
    except:
        print("Failed to start selenium!")
        exit(1)

    # Go to start page
    driver.get("https://www.cardmarket.com/en/Pokemon")

    print("Success")

    return driver

if __name__ == '__main__':
    # Cardmarket uses ids for languages
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

    driver = _createDriver()

    while True:
        print()

        cardId = input("Card ID:")
        language = input("Language (en, fr, de, sp, it, s-ch, ja, po, ko, t-ch):")

        if(cardId == "" or language == ""):
            driver.close()
            exit(0)

        try:
            languageId = languages[language]
        except:
            print("Invalid language")
            continue

        # Find the search input and enter card id
        try:
            searchInput = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f"//input[@id='ProductSearchInput']")))
            oldUrl = driver.current_url
            searchInput.send_keys(cardId)
            searchInput.send_keys(Keys.ENTER)
            searchInput = WebDriverWait(driver, 5).until_not(EC.url_to_be(oldUrl))
        except:
            print("Page couldn't load, most likely blocked due to too many requests, restart the program and try again in a few seconds")
            driver.close()
            exit(0)

        # Append language id to URL
        driver.get(driver.current_url + "?language=" + str(languageId))
        print("URL: " + driver.current_url)

        # Grab the first entry in the table (default sorted by cheapest)
        try:
            firstRow = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f"//div[contains(@id, 'articleRow')][1]")))
            price = firstRow.find_element(By.XPATH, f"//div[@class='col-offer col-auto']//span[last()]").get_attribute('innerHTML')
            print(price)
        except:
            print("No offers found, most likely blocked due to too many requests, restart the program and try again in a few seconds")
            driver.close()
            exit(0)
