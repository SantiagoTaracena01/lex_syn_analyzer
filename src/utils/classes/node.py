class Node(object):
    def __init__(self, value, start, end):
        self.value = value
        self.start = start
        self.end = end
        self.done = False
