from bs4 import BeautifulSoup


class IActionOnPage:
    def action_on_the_page(self, page):
        pass


class ActionsOnPage(IActionOnPage):
    def __init__(self):
        self.actions = []

    def append(self, action: IActionOnPage):
        self.actions.append(action)

    def action_on_the_page(self, page):
        for i in self.actions:
            i.action_on_the_page(page)


class ActionOnPageScreenshot(IActionOnPage):
    def __init__(self, name="example.png"):
        self.name = name

    def action_on_the_page(self, page, name="example.png"):
        page.screenshot(path=name)
        print("скриншот выполнен")


class ActionOnPageSoup(IActionOnPage):
    def action_on_the_page(self, page):
        content = page.content()
        soup = BeautifulSoup(content, 'html5lib')
        print(soup.prettify())


class ActionOnPageFill(IActionOnPage):
    def __init__(self, role="", tag=""):
        self.role = role
        self.tag = tag

    def action_on_the_page(self, page):
        page.get_by_role(self.role).fill(self.tag)


class ActionOnPageClick(IActionOnPage):
    def __init__(self, text=""):
        self.text = text

    def action_on_the_page(self, page):
        page.get_by_text(self.text).click()
        page.wait_for_load_state()


class ActionOnPageGoto(IActionOnPage):
    def __init__(self, url="example.png"):
        self.url = url

    def action_on_the_page(self, page):
        page.goto(self.url)
