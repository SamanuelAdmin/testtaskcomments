from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self, AdvancedQueue):
        super().__init__()
        self.advTagQueue = AdvancedQueue()
        self.oppenedTags = []

    def feed(self, data):
        self.rawdata = data
        self.goahead(0)

    def handle_starttag(self, tag, attrs):
        self.advTagQueue.add_( {tag: attrs})
        self.oppenedTags.append(tag)

    def handle_endtag(self, tag):
        self.oppenedTags.remove(tag)

    def handle_data(self, data): pass

    def checkOpenTags(self):
        if len(self.oppenedTags) == 0:
            return True
        return False