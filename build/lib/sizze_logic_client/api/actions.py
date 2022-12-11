from sizze_logic_client.api.base import Client
import aiohttp


class ActionClient(Client):
    async def create(self, data):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=self.base_url + "action/create/",
                json=data
            ) as response:
                response_body = await response.json()
            return response_body, response.status

    async def retrieve(self, action_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=self.base_url + f"action/{action_id}/retrieve/"
            ) as response:
                response_body = await response.json()
                return response_body, response.status

    async def list(self, **params):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=self.base_url + "action/list/",
                params=params
            ) as response:
                response_body = await response.json()
                return response_body, response.status

    async def update(self, action_id: int, data):
        async with aiohttp.ClientSession() as session:
            async with session.put(
                    url=self.base_url + f"action/{action_id}/update/",
                    json=data
            ) as response:
                response_body = await response.json()
                return response_body, response.status

    async def delete(self, action_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                url=self.base_url + f"action/{action_id}/delete/",
            ) as response:
                if response.status == 204:
                    return None, response.status
                else:
                    response_body = await response.json()
                    return response_body, response.status

    async def multiple_delete(self, **params):
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                url=self.base_url + "action/multiple-delete/",
                params=params
            ) as response:
                if response.status == 204:
                    return None, response.status
                else:
                    response_body = await response.json()
                    return response_body, response.status
