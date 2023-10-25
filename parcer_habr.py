class IParcerStates:
    def __init__(self, url, tags, fields):
        self.url = url
        self.tags = tags
        self.dict_sample = dict.fromkeys(fields)
        self.dicts = []

    def parcing(self):
        for i in self.tags:
            self.input_tag()
            states = self.skraping()
            while (len(state) == len(self.dicts)):
                self.dicts.append(self.processing(j))

    def input_tag(self):
        pass

    def skraping(self):
        return []

    def processing(self, j):
        pass





















