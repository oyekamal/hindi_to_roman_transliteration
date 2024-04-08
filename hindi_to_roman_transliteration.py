
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless') # Run in headless mode

# Setup WebDriver
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

# Setup Chrome driver
# Navigate to the URL
def hindi_to_roman_transliteration(text="",target_language='en', source_language='hi'):
    url = f"https://translate.google.com/?sl={source_language}&tl={target_language}&text={text}&op=translate"
    driver.get(url)

    # Wait for the page to load and the translation to appear
    driver.implicitly_wait(100) # Adjust the wait time as needed

    # Find the div with class 'kO6q6e' using the provided CSS path
    css_path = 'html body#yDmH0d.tQj5Y.ghyPEc.IqBfM.ecJEib.EWZcud.EIlDfe.cjGgHb.d8Etdd.LcUz9d c-wiz.zQTmif.SSPGKf.kXN2zb.BIdYQ div.T4LgNb div.ToWKne c-wiz.MOkH4e.iYelWb.yF6Zo div.OlSOob c-wiz.QsA0jb div.ccvoYb div.AxqVh div.OPPzxe c-wiz.rm1UF.dHeVVb.UnxENd div.UdTY9.BwTYAc.leDWne div.kO6q6e'
    transliteration_text = driver.find_element(By.CSS_SELECTOR, css_path).text
    
    css_path_translated = 'html body#yDmH0d.tQj5Y.ghyPEc.IqBfM.ecJEib.EWZcud.EIlDfe.cjGgHb.d8Etdd.LcUz9d c-wiz.zQTmif.SSPGKf.kXN2zb.BIdYQ div.T4LgNb div.ToWKne c-wiz.MOkH4e.iYelWb.yF6Zo div.OlSOob c-wiz.QsA0jb div.ccvoYb div.AxqVh div.OPPzxe c-wiz.sciAJc div.QcsUad.BDJ8fb.sMVRZe.wneUed div.usGWQd div.KkbLmb div.lRu31 span.HwtZe span.jCAhz.ChMk0b span.ryNqvb'
    translated_text = driver.find_element(By.CSS_SELECTOR, css_path_translated).text
    # print(translated_text)
    return translated_text, transliteration_text

text = 'हाय, कैसे हो भाई?'
tras = hindi_to_roman_transliteration(text=text,target_language='en', source_language='hi')
print("---")
print(tras)
print("---")

text = 'ہیلو بھائی کیسے ہیں آپ؟'
tras = hindi_to_roman_transliteration(text=text,target_language='en', source_language='ur')
print("---")
print(tras)
print("---")

text = 'こんにちは、お兄さん、お元気ですか？'
tras = hindi_to_roman_transliteration(text=text,target_language='en', source_language='ja')
print("---")
print(tras)
print("---")