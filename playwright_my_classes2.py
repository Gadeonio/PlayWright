from datetime import datetime
import pandas as pd

from tabulate import tabulate

from playwright.sync_api import Playwright, sync_playwright, expect
from playwright_my_classes import *

from command import *
from parcer_habr import *

'''dict_browser = {'firefox': Playwright.firefox,
                'chromium': Playwright.chromium,
                'webkit': Playwright.webkit}'''
fields = ['Название статьи', 'Дата', 'Теги', 'Ссылка', 'Название сайта']


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


            j = 0
            for i in self.tags:
                self.page.goto('')
                self.page.screenshot(path=f"Start page {j}.png")
                textbox = self.page.get_by_role("textbox", name="Поиск")
                textbox.fill(i)
                textbox.press("Enter")

                # Костыль, нужно понять как сделать скрин (beatsoup), после прогрузки страницы
                # time.sleep(2)
                # self.page.wait_for_load_state() # не работает
                # Нужно использовать Xpuff и Auto-waiting (Нашел другое решение, нужно спросить норм ли оно)
                expect(self.page.locator("em")).to_be_enabled()

                self.page.screenshot(path=f"Habs {i}.png")

                j += 1
                hub = self.page.locator('em')
                parent = hub.locator('xpath=..')
                # print(parent.inner_html())
                grandparent = parent.locator('xpath=..')
                # print(grandparent.inner_html())
                grandgrandparent = grandparent.locator('xpath=..')
                # print(grandgrandparent.inner_html())
                url = grandgrandparent.get_by_role('link').get_attribute('href')
                print(url)
                self.page.goto(url)

                # find_results_designation= self.page.locator('.tm-title__link')
                # для for: text = element.locator('xpath=..').get_by_role('link').get_attribute('href')
                find_results = self.page.locator('.tm-articles-list__item')

                # get the number of elements/tags
                count = find_results.count()
                # loop through all elements/tags
                for i in range(count):
                    # get the element/tag
                    element = find_results.nth(i)
                    # get the text of the element/tag
                    # text = element.locator('.tm-user-info__user_appearance-default').get_by_role('link').get_attribute('href')
                    text_name = element.locator('.tm-title__link').locator('span').inner_text()
                    text2 = element.locator('time').get_attribute('datetime')
                    res3 = element.locator('.tm-publication-hub__link-container')
                    count3 = res3.count()
                    text3 = []
                    for j in range(count3):
                        this_text = res3.nth(j).locator('span').nth(0).inner_text()
                        text3.append(this_text)
                    text4 = "https://habr.com" + element.locator('.tm-title__link').get_attribute('href')
                    # print(this_text)
                    # print the text
                    print(f"\nСтатья {i + 1}")
                    print(text_name)

                    text2 = datetime.strptime(text2, "%Y-%m-%dT%H:%M:%S.000Z").strftime("%d.%m.%Y %H:%M:%S")
                    print(text2)
                    print(text3)
                    print(text4)
                    print("habr")
                    attribute = [text_name, text2, text3, text4, "habr"]

                    self.dicts.append(dict(list(zip(self.fields, attribute))))

            self.browser.close()

    def parcing2(self):
        with sync_playwright() as p:
            self.browser = self.get_browser(p)
            self.page = self.browser.new_page(user_agent=self.get_user_agent(), base_url=self.url)

            self.pass_by_tags()

            self.print_dict_pandas()

            self.browser.close()

    def pass_by_tags(self):
        for i in self.tags:
            self.page.goto('')
            textbox = self.page.get_by_role("textbox", name="Поиск")
            textbox.fill(i)
            textbox.press("Enter")
            #Подумать какой локатор вставить
            expect(self.page.locator(".tm-hub__title").nth(0)).to_be_enabled()
            url = self.page.locator('.tm-hub__title').nth(0).locator('xpath=..').get_by_role(
                'link').get_attribute('href')
            self.page.goto(url)
            self.pass_by_article()

    def pass_by_article(self):
        find_results = self.page.locator('.tm-articles-list__item')
        count = find_results.count()

        for i in range(count):
            element = find_results.nth(i)
            text_name = element.locator('.tm-title__link').locator('span').inner_text()
            text_datetime = element.locator('time').get_attribute('datetime')
            res3 = element.locator('.tm-publication-hub__link-container')
            count3 = res3.count()
            text_tags = []
            for j in range(count3):
                this_text = res3.nth(j).locator('span').nth(0).inner_text()
                text_tags.append(this_text)
            text_href = "https://habr.com" + element.locator('.tm-title__link').get_attribute('href')
            text_datetime = datetime.strptime(text_datetime, "%Y-%m-%dT%H:%M:%S.000Z").strftime("%d.%m.%Y %H:%M:%S")
            attribute = [text_name, text_datetime, text_tags, text_href, "habr"]
            self.dicts.append(dict(list(zip(self.fields, attribute))))

    def get_browser(self, p):
        return self.browser.get_browser(p)

    def print_dict_pandas(self):
        df = pd.DataFrame(self.dicts)
        print(tabulate(df, headers='keys', tablefmt='psql'))

if __name__ == "__main__":
    tags = ["python", "natural language processing", "machine learning",
            "data mining", "tensorflow", "pytorch", "api",
            "django", "flask", "fastapi", "sql", "postgresql"]
    parcer = ParcerStatesHabr(tags)
    parcer.parcing2()
