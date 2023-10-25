class Human:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, num):
        self.height += num


class Grow:
    def __init__(self, human, num):
        self.human = human
        self.human.grow(num)


if __name__ == "__main__":
    girl = Human("Alina", 165)
    Grow(girl, 165)

