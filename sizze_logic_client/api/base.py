import aiohttp
from sizze_logic_client import settings


class Client:
    def __init__(self):
        self.__path = None

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @property
    def base_url(self):
        return settings.base_url

    async def get_url(self):
        return self.base_url + self.path

    async def validate_params(self, params):
        validate_params = {}
        for key, val in params.items():
            if val is not None:
                validate_params[key] = val
        return validate_params

    async def get_id_from_data(self, data):
        if isinstance(data, dict):
            _id = data.get("_id") or data.get("id")
        else:
            _id = None
        return _id

    async def send_request(self, method, data=None, **params):
        for key, val in params.copy().items():
            if val is None:
                del params[key]

        url = await self.get_url()
        async with aiohttp.ClientSession() as session:
            match method:
                case "get":
                    response = await session.get(url=url, params=params)
                case "post":
                    response = await session.post(url=url, params=params, json=data)
                case "put":
                    response = await session.put(url=url, params=params, json=data)
                case "delete":
                    response = await session.delete(url=url, params=params)
                case _:
                    raise ValueError("Method not found")
            if response.status == 204:
                response_data = dict()
            else:
                response_data = await response.json()
            await session.close()

        if response.status in [400, 422]:
            raise ServerError(response_data.get("message"))
        _id = await self.get_id_from_data(data=response_data)
        return ServerResponse(status=response.status, data=response_data, _id=_id)


class ServerResponse:
    def __init__(self, status: int, data: dict, _id=None):
        self.status = status
        self.data = data
        self.id = _id


class ServerError(Exception):
    pass
