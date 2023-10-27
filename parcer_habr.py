class IParcerStates:
    def __init__(self, url, tags, fields):
        self.url = url
        self.tags = tags
        self.fields = fields
        self.dicts = []

    def parcing(self):
        for i in self.tags:
            self.input_tag()
            states = self.skraping()
            while (len(states) == len(self.dicts)):
                self.dicts.append(self.processing(j))

    def input_tag(self):
        pass

    def skraping(self):
        return []

    def processing(self, j):
        pass





















