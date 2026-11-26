from loguru import get_logger

from selenium.webdriver.common.by import By

from .base import BaseSeleniumCrawler

from llm_engineering.domain.documents import PostDocument
from llm_engineering.settings import settings

logger = get_logger(__name__)

class LinkedinCrawler(BaseSeleniumCrawler):
    
    model = PostDocument

    def __init__(self, scroll_limit: int = 5, is_deprecated: bool = True) -> None:
        super().__init__(scroll_limit)

        self._is_deprecated = is_deprecated

    def set_extra_driver_options(self, options):
        options.add_argument("detach", True)

    def login(self) -> None:
        if self._is_deprecated:
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

            logger.error(f"error {e!s}")

    def extract(self, link: str, **kwargs) -> None:
        if self._is_deprecated:
            raise DeprecationWarning(
                "As linkedin has updated its security measures, the extract() method is no longer supported"
            )

        if self.model.link is not None:
            old_model = self.model.find(link=link)
            if old_model is not None:
                logger.info(f"Post already exists in the database: {link}")

                return

        logger.info(f"Starting scraping data for profile: {link}")

        self.login()

        soup = self._get_page_content(link)

        data = {
            "Name": self._Scrape_section(soup, "h1", class_="text-heading-xlarge")
        }
    