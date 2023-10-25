from playwright_my_classes import *

if __name__ == '__main__':
    actions = [ActionOnPageFill("combobox", "python"), ActionOnPageClick("Найти"), ActionOnPageScreenshot(), ActionOnPageSoup()]
    playwright = PlayWrightWiseSyncChangeBrowserUserAgent("https://ya.ru/", actions)
    '''main_url = "https://habr.com/ru/hubs/"
    tags = ["natural language processing", "python", "machine learning",
        "data mining", "tensorflow", "pytorch", "api",
        "django", "flask", "fastapi", "sql", "postgresql"]
    
    tags = tags[:2]'''







#парсинг на хабре
#поиск по тегам через хабр
#Часовой пояс UTS
#Название, дата, теги(в нижне регистре, без лишних знаков), ссылка (полный адрес, чтоб ссыкла была рабочей), название сайта (Пока HABR)) хранить в json или в питоноском слове.
#Сделать тесты по тегам django, postgres

