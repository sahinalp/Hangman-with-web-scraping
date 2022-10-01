from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class RandomWord:
    def __init__(self):

        self.word=""
        self.defination=""
        self.GuessCount=6
        self.RandomWordWebsite="https://randomwordgenerator.com/"
        self.DictionaryWebsite="https://dictionary.cambridge.org/dictionary/english/"        

        self.options = Options()
        self.options.headless=True

        self.timeout=3
    
    def GetRandomWord(self):
        self.driver.get(self.RandomWordWebsite)
        val=0
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'support'))
            WebDriverWait(self.driver, self.timeout).until(element_present)
        except TimeoutException:
            val=-1
        try:
            self.word=self.driver.find_element(by=By.CSS_SELECTOR,value="#result > li").text
        except:
            self.word=""

    def GetDefination(self):
        if self.word!="":
            self.driver.get(self.DictionaryWebsite+self.word)
            val=0
                        
            definationTextPath="#page-content > div.page > div:nth-child(1) > div.link > div > div.di-body > div > div > div > div.pos-body > div > div.sense-body.dsense_b > div:nth-child(1) > div.ddef_h > div"
            try:
                element_present = EC.presence_of_element_located((By.ID, "main"))
                WebDriverWait(self.driver, self.timeout).until(element_present)
            except TimeoutException:
                val=-1
            try:
                definationTexts=self.driver.find_element(by=By.CSS_SELECTOR, value=definationTextPath)
                self.defination=definationTexts.text
                self.defination=self.defination.strip(":")
            except:
                self.defination=""
    def Close(self):
        self.driver.close()
    def Open(self):
        self.driver=webdriver.Firefox(options=self.options)
