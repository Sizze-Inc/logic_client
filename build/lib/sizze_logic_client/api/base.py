class Client:
    def __init__(self):
        self.base_url = None

    def set_base_url(self, base_url):
        self.base_url = base_url

    def get_base_url(self):
        return self.base_url
