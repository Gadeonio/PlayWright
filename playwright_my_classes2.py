import time

from playwright.sync_api import Playwright, sync_playwright, expect
from playwright_my_classes import *
from command import *
from parcer_habr import *


'''dict_browser = {'firefox': Playwright.firefox,
                'chromium': Playwright.chromium,
                'webkit': Playwright.webkit}'''
fields=['Название статьи', 'Дата', 'Теги', 'Ссылка', 'Название сайта']


class ParcerStatesHabr(IParcerStates, IBrowser, IUserAgent):
    def __init__(self, tags):
        super().__init__(url="https://habr.com/ru/hubs/", tags=tags, fields=fields)
        self.page = None
        self.browser = BrowserChromium()
        self.user_agent: IUserAgent = UserAgentChrome()


    def parcing(self):
        with sync_playwright() as p:
            self.browser = self.get_browser(p)
            self.page = self.browser.new_page(user_agent=self.get_user_agent(), base_url=self.url)
            self.page.goto('')

            j = 0
            for i in self.tags:
                self.page.screenshot(path=f"Start page {j}.png")
                textbox = self.page.get_by_role("textbox", name="Поиск")
                textbox.fill(i)
                textbox.press("Enter")

                # Костыль, нужно понять как сделать скрин (beatsoup), после прогрузки страницы
                time.sleep(2)
                #self.page.wait_for_load_state() # не работает

                self.page.screenshot(path=f"Habs {i}.png")

                j += 1

            self.browser.close()

    def input_tag(self):
        pass


    def get_browser(self, p):
        return self.browser.get_browser(p)

if __name__=="__main__":
    tags = ['python']
    parcer = ParcerStatesHabr(tags)
    parcer.parcing()














