from sizze_logic_client.api.base import Client
import aiohttp


class VariableClient(Client):
    async def create(self, data) -> (str, bool):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=self.base_url + "variable/create/",
                json=data
            ) as response:
                response_body = await response.json()
            return response_body, response.status

    async def create_by_table(self, data):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    url=self.base_url + "variable/create_by_table/",
                    json=data
            ) as response:
                response_body = await response.json()
            return response_body, response.status

    async def retrieve(self, variable_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=self.base_url + f"variable/{variable_id}/retrieve/"
            ) as response:
                response_body = await response.json()
                return response_body, response.status

    async def list(self, **params):
        validate_params = await self.validate_params(params=params)

        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=self.base_url + "variable/list/",
                params=validate_params
            ) as response:
                response_body = await response.json()
                return response_body, response.status

    async def update(self, variable_id: int, data) -> (str, bool):
        async with aiohttp.ClientSession() as session:
            async with session.put(
                    url=self.base_url + f"variable/{variable_id}/update/",
                    json=data
            ) as response:
                response_body = await response.json()
                return response_body, response.status

    async def delete(self, variable_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                url=self.base_url + f"variable/{variable_id}/delete/",
            ) as response:
                if response.status == 204:
                    return None, response.status
                else:
                    response_body = await response.json()
                    return response_body, response.status

    async def multiple_delete(self, **params):
        validate_params = await self.validate_params(params=params)

        async with aiohttp.ClientSession() as session:
            async with session.delete(
                url=self.base_url + "variable/multiple-delete/",
                params=validate_params
            ) as response:
                if response.status == 204:
                    return None, response.status
                else:
                    response_body = await response.json()
                    return response_body, response.status
