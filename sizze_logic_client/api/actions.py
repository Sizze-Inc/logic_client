from sizze_logic_client.api.base import Client, ServerResponse


class ActionClient(Client):
    async def create(self, data):
        self.path = "action/create/"
        response = await self.send_request(method="post", data=data)
        return response

    async def retrieve(self, action_id: int):
        self.path = f"action/{action_id}/retrieve/"
        response = await self.send_request(method="get", action_id=action_id)
        return response

    async def list(self, page_id: int = None, project_id: int = None):
        self.path = "action/list/"
        response = await self.send_request(method="get", page_id=page_id, project_id=project_id)
        return response

    async def update(self, action_id: int, data):
        self.path = f"action/{action_id}/update/"
        response = await self.send_request(method="put", data=data)
        return response

    async def delete(self, action_id: int):
        self.path = f"action/{action_id}/delete/"
        response = await self.send_request(method="delete", action_id=action_id)
        return response

    async def multiple_delete(self, page_id: int = None, project_id: int = None):
        self.path = "action/multiple-delete/"
        response = await self.send_request(method="delete", page_id=page_id, project_id=project_id)
        return response


action_client = ActionClient()
