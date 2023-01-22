from sizze_logic_client.api.base import Client, ServerResponse


class VariableClient(Client):
    async def create(self, data) -> ServerResponse:
        self.path = "variable/create/"
        response = await self.send_request(method="post", data=data)
        return response

    async def add_to_category(self, variable_id, category_id) -> ServerResponse:
        self.path = f"variable/{variable_id}/category/add/"
        response = await self.send_request(method="post", data={"category_id": category_id})
        return response

    async def remove_from_category(self, variable_id, category_id) -> ServerResponse:
        self.path = f"variable/{variable_id}/category/remove/"
        response = await self.send_request(method="post", data={"category_id": category_id})
        return response

    async def create_field_variable(self, field_name, field_id, field_path, categories) -> ServerResponse:
        data = {
            "name": field_name,
            "type": "field",
            "indicator": field_id,
            "path": field_path,
            "categories": categories
        }
        field_variable = await self.create(data=data)
        return field_variable

    async def retrieve(self, variable_id: int) -> ServerResponse:
        self.path = f"variable/{variable_id}/retrieve/"
        response = await self.send_request(method="get", variable_id=variable_id)
        return response

    async def list(self, variable_type: str = None, category_id: int = None,
                   category_type: str = None, category_indicator: str = None)\
            -> ServerResponse:
        self.path = "variable/list/"
        response = await self.send_request(
            method="get", category_id=category_id, category_type=category_type,
            category_indicator=category_indicator, type=variable_type
        )
        return response

    async def nested_list(self, category_id) -> ServerResponse:
        self.path = "variable/nested_list/"
        response = await self.send_request(
            method="get", category_id=category_id
        )
        return response

    async def update(self, variable_id: int, data) -> ServerResponse:
        self.path = f"variable/{variable_id}/update/"
        response = await self.send_request(method="put", data=data)
        return response

    async def delete(self, variable_id: int) -> ServerResponse:
        self.path = f"variable/{variable_id}/delete/"
        response = await self.send_request(method="delete", variable_id=variable_id)
        return response

    async def multiple_delete(self, category_id: int):
        self.path = "variable/multiple-delete/"
        response = await self.send_request(method="delete", category_id=category_id)
        return response


variable_client = VariableClient()


class CategoryClient(Client):
    async def create(self, data) -> ServerResponse:
        self.path = "variable/category/create/"
        response = await self.send_request(method="post", data=data)
        return response

    async def create_table_category(self, parent_id, table_id, field_list=None) -> ServerResponse:
        data = {
            "type": "table",
            "indicator": table_id,
            "parent": parent_id
        }
        table_category = await self.create(data=data)
        if field_list:
            for field in field_list:
                field["categories"] = [table_category.id]
                await variable_client.create_field_variable(**field)
        return table_category

    async def retrieve(self, category_id: int) -> ServerResponse:
        self.path = f"variable/category/{category_id}/retrieve/"
        response = await self.send_request(method="get", category_id=category_id)
        return response

    async def list(self, type: str = None, indicator: str = None, parent: int = None) -> ServerResponse:
        self.path = "variable/category/list/"
        response = await self.send_request(
            method="get", type=type, indicator=indicator, parent=parent
        )
        return response

    async def update(self, category_id: int, data) -> ServerResponse:
        self.path = f"variable/category/{category_id}/update/"
        response = await self.send_request(method="put", data=data)
        return response

    async def delete(self, category_id: int) -> ServerResponse:
        self.path = f"variable/category/{category_id}/delete/"
        response = await self.send_request(method="delete", category_id=category_id)
        return response


category_client = CategoryClient()
