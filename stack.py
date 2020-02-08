class Stack:

    def __init__(self):
        self.elements = []

    def add(self, item):
        if item != None:
            self.elements.reverse()
            self.elements.append(item)
            self.elements.reverse()

    def pop(self, index=None):
        item = 0
        if len(self.elements) > 0:
            self.elements.reverse()
            item = self.elements.pop()
            self.elements.reverse()

        return item

    def pick(self):
        item = 0

        if len(self.elements) > 0:
            item = self.elements[0]

        return item

    def find(self, element):
        if element is not None:
            return self.elements.index(element)

    def print(self):
        print(self.elements)

    def get_elements(self):
        return self.elements

    def set_elements(self, elements):
        self.elements = elements

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def length(self):
        return len(self.elements)

    def removeFirst(self, item):
        if item in self.elements: self.elements.remove(item)

    def removeAll(self, item):
        filter(lambda a: a != item, self.elements)
