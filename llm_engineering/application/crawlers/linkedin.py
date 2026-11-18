from selenium.webdriver.common.by import By

from .base import BaseSeleniumCrawler

from llm_engineering.domain.documents import ArticleDocument
from llm_engineering.settings import settings

class LinkedinCrawler(BaseSeleniumCrawler):
    
    model = ArticleDocument

    def __init__(self, scroll_limit: int = 5, is_deprecated: bool = True) -> None:
        super().__init__(scroll_limit)

        self.is_deprecated = is_deprecated

    def set_extra_driver_options(self, options):
        options.add_argument("detach", True)

    def login(self) -> None:
        if self.is_deprecated:
           raise DeprecationWarning(
               "As Linkedin has updated its security measures, the login() method is no longer supported"
           )

        self.driver.get("https://linkedin.com/login")
        if not settings.LINKEDIN_USERNAME or not settings.LINKEDIN_PASSWORD:
            raise Exception(
                "Linkedin Scraper required the {LINKEDIN_USERNAME} and {LINKEDIN_PASSOWRD} settings"
            )

        try :

            self.driver.find_element(By.CSS_SELECTOR, "input#_R_e3pptiejj35656j6_").send_keys(settings.LINKEDIN_USERNAME)
            self.driver.find_element(By.CSS_SELECTOR, "input#_R_e3pptiejj35656j6_").send_keys(settings.LINKEDIN_PASSOWRD)
            self.driver.find_element(By.CSS_SELECTOR, "#auto-component-8ea9141d-fe7e-401a-924b-0d1ff1ec8cf1 > div > div > div.aaaayq.aaal5q > div > div.aaal6d.aaaayy.aaaiun.aaaj1t.aaaj08.aaaj1j.aaaixb.aaal5q > button").click()

        except Exception as e:

            print(f"ERROR: {e}")

    # NEEDS MORE IMPLEMENTATION