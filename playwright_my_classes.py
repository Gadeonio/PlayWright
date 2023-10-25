from playwright.sync_api import sync_playwright

from fake_useragent import UserAgent
from commands_playwright import *


class IUserAgent:
    def get_user_agent(self):
        return None


class UserAgentChrome(IUserAgent):
    def get_user_agent(self):
        return UserAgent().chrome


class IBrowserHeadless:
    def get_headless(self):
        return False


class IBrowser:
    def get_browser(self, p):
        return None


class BrowserWebkit(IBrowser, IBrowserHeadless):
    def get_browser(self, p):
        return p.webkit.launch(headless=self.get_headless())


class BrowserChromium(IBrowser, IBrowserHeadless):
    def get_browser(self, p):
        return p.chromium.launch(headless=self.get_headless())


class BrowserFirefox(IBrowser, IBrowserHeadless):
    def get_browser(self, p):
        return p.firefox.launch(headless=self.get_headless())
# Подумать как реализовать выбор BrowserType (Скорее всего либо через паттерн Command, либо надо подумать)


class IPlayWrightWise:
    def __init__(self, url=""):
        self.url = url

    def loading_page(self):
        pass

    def perform_an_actions_on_the_page(self, page):
        pass


class IPlayWrightWiseSyncChangeBrowser(IPlayWrightWise, IBrowser):
    def __init__(self, url):
        super().__init__(url)

    def loading_page(self):
        with sync_playwright() as p:
            browser = self.get_browser(p)
            page = browser.new_page()
            page.goto(self.url)
            self.perform_actions_on_page()
            browser.close()

    def perform_actions_on_page(self):
        pass


class IPlayWrightWiseSync(IPlayWrightWise):
    def __init__(self, url):
        super().__init__(url)

    def loading_page(self):
        with sync_playwright() as p:
            browser = p.firefox.launch()
            page = browser.new_page()
            page.goto(self.url)
            self.perform_actions_on_page()
            browser.close()

    def perform_actions_on_page(self):
        pass


class PlayWrightWiseSync(IPlayWrightWise):
    def __init__(self, url, actions_on_page: list):
        super().__init__(url)
        self.actions_on_page = actions_on_page
        self.loading_page()

    def loading_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(self.url)
            self.perform_an_actions_on_the_page(page)
            browser.close()

    def perform_an_actions_on_the_page(self, page):
        for i in self.actions_on_page:
            i.action_on_the_page(page)


class PlayWrightWiseSyncWithFakeUser(IPlayWrightWise):
    def __init__(self, url, actions_on_page: list):
        super().__init__(url)
        self.actions_on_page = actions_on_page
        self.loading_page()

    def loading_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(user_agent=UserAgent().chrome)
            page.goto(self.url)
            self.perform_an_actions_on_the_page(page)
            browser.close()

    def perform_an_actions_on_the_page(self, page):
        for i in self.actions_on_page:
            i.action_on_the_page(page)


class IPlayWrightWiseSyncChangeBrowser(IPlayWrightWise, IBrowser):
    def __init__(self, url):
        super().__init__(url)

    def loading_page(self):
        with sync_playwright() as p:
            browser = self.get_browser(p)
            page = browser.new_page()
            page.goto(self.url)
            self.perform_actions_on_page()
            browser.close()

    def perform_actions_on_page(self):
        pass


class IPlayWrightWiseSync(IPlayWrightWise):
    def __init__(self, url):
        super().__init__(url)

    def loading_page(self):
        with sync_playwright() as p:
            browser = p.firefox.launch()
            page = browser.new_page()
            page.goto(self.url)
            self.perform_actions_on_page()
            browser.close()

    def perform_actions_on_page(self):
        pass


class PlayWrightWiseSync(IPlayWrightWise):
    def __init__(self, url, actions_on_page: list):
        super().__init__(url)
        self.actions_on_page = actions_on_page
        self.loading_page()

    def loading_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(self.url)
            self.perform_an_actions_on_the_page(page)
            browser.close()

    def perform_an_actions_on_the_page(self, page):
        for i in self.actions_on_page:
            i.action_on_the_page(page)


class PlayWrightWiseSyncChangeBrowserUserAgent(IPlayWrightWise, IBrowser, IUserAgent):
    def __init__(self, url, actions_on_page: list, browser=BrowserChromium(), user_agent=UserAgentChrome()):
        super().__init__(url)
        self.browser: IBrowser = browser
        self.user_agent: IUserAgent = user_agent
        self.actions_on_page = actions_on_page
        self.loading_page()

    def loading_page(self):
        with sync_playwright() as p:
            browser = self.get_browser(p)
            page = browser.new_page(user_agent=self.get_user_agent())
            page.goto(self.url)
            self.perform_an_actions_on_the_page(page)
            browser.close()

    def perform_an_actions_on_the_page(self, page):
        for i in self.actions_on_page:
            i.action_on_the_page(page)

    def get_browser(self, p):
        return self.browser.get_browser(p)

    def get_user_agent(self):
        return self.user_agent.get_user_agent()




# Нужно реализовать действия с помощью locale (https://playwright.dev/python/docs/writing-tests) используя fill
# Подумать о реализации паттерна Command
