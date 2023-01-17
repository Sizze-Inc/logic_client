from sizze_logic_client.api.base import Client, ServerResponse


class VariableClient(Client):
    async def create(self, data) -> ServerResponse:
        self.path = "variable/create/"
        response = await self.send_request(method="post", data=data)
        return response

    async def create_by_table(self, data) -> ServerResponse:
        self.path = "variable/create_by_table/"
        response = await self.send_request(method="post", data=data)
        return response

    async def create_field_variable(self, page_id, project_id, variable_name,
                                    field_id, field_index, table_id, table_index,
                                    path):
        variable_body = dict(
            type="TABLE_FIELD_VALUE",
            path=path,
            table=dict(table_id=table_id, table_index=table_index),
            field=dict(field_id=field_id, field_index=field_index)
        )
        data = dict(
            name=variable_name,
            variable=variable_body,
            page_id=page_id,
            project_id=project_id,
        )
        create_variable = await self.create(data=data)

    async def retrieve(self, variable_id: int) -> ServerResponse:
        self.path = f"variable/{variable_id}/retrieve/"
        response = await self.send_request(method="get", variable_id=variable_id)
        return response

    async def list(self, page_id: int = None, project_id: int = None) -> ServerResponse:
        self.path = "variable/list/"
        response = await self.send_request(method="get", page_id=page_id, project_id=project_id)
        return response

    async def update(self, variable_id: int, data) -> ServerResponse:
        self.path = f"variable/{variable_id}/update/"
        response = await self.send_request(method="put", data=data)
        return response

    async def delete(self, variable_id: int) -> ServerResponse:
        self.path = f"variable/{variable_id}/delete/"
        response = await self.send_request(method="delete", variable_id=variable_id)
        return response

    async def multiple_delete(self, page_id: int = None, project_id: int = None,
                              table_id: str = None, field_id: str = None):
        self.path = "variable/multiple-delete/"
        response = await self.send_request(method="delete", page_id=page_id, project_id=project_id,
                                           table_id=table_id, field_id=field_id)
        return response


variable_client = VariableClient()
