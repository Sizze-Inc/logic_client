from sizze_logic_client.api.base import Client, ServerResponse


class FilterClient(Client):
    async def create(self, data) -> ServerResponse:
        self.path = "filter/create/"
        response = await self.send_request(method="post", data=data)
        return response

    async def retrieve(self, filter_id: int) -> ServerResponse:
        self.path = f"filter/{filter_id}/retrieve/"
        response = await self.send_request(method="get", filter_id=filter_id)
        return response

    async def list(self, page_id: int = None, project_id: int = None) -> ServerResponse:
        self.path = "filter/list/"
        response = await self.send_request(method="get", page_id=page_id, project_id=project_id)
        return response

    async def update(self, filter_id: int, data) -> ServerResponse:
        self.path = f"filter/{filter_id}/update/",
        response = await self.send_request(method="put", data=data)
        return response

    async def delete(self, filter_id: int) -> ServerResponse:
        self.path = f"filter/{filter_id}/delete/"
        response = await self.send_request(method="delete", filter_id=filter_id)
        return response

    async def multiple_delete(self, page_id: int = None, project_id: int = None) -> ServerResponse:
        self.path = "filter/multiple-delete/"
        response = await self.send_request(method="delete", page_id=page_id, project_id=project_id)
        return response


filter_client = FilterClient()
