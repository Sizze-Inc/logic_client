class Client:
    def __init__(self):
        self.base_url = None

    def set_base_url(self, base_url):
        self.base_url = base_url

    def get_base_url(self):
        return self.base_url

    async def validate_params(self, params):
        validate_params = {}
        for key, val in params.items():
            if val is not None:
                validate_params[key] = val
        return validate_params
