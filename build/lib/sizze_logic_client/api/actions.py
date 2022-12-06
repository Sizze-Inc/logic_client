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
                if response.status == 201:
                    response = response_body.get("id")
                else:
                    response = response_body
        return response

    async def retrieve(self, action_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=self.base_url + f"variable/{action_id}/retrieve/"
            ) as response:
                response_body = await response.json()
                return response_body

    async def list(self, page_id: int = None, project_id: int = None):
        params = {"page_id": page_id, "project_id": project_id}
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=self.base_url + "action/list/",
                params=params
            ) as response:
                response_body = await response.json()
                return response_body

    async def update(self, action_id: int, data):
        async with aiohttp.ClientSession() as session:
            async with session.put(
                    url=self.base_url + f"action/{action_id}/update/",
                    json=data
            ) as response:
                response_body = await response.json()
                if response.status == 200:
                    return response_body.get("id")
                else:
                    return response_body

    async def delete(self, action_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=self.base_url + f"action/{action_id}/delete/",
            ) as response:
                response_body = await response.json()
                return response_body

    async def multiple_delete(self, page_id: int = None, project_id: int = None):
        params = {"page_id": page_id, "project_id": project_id}
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                url=self.base_url + "action/multiple-delete/",
                params=params
            ) as response:
                response_body = await response.json()
                return response_body
