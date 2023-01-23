from sizze_logic_client.api.base import Client, ServerResponse


class VariableClient(Client):
    async def create(self, data) -> ServerResponse:
        self.path = "variable/create/"
        response = await self.send_request(method="post", data=data)
        return response

    async def add_to_category(self, variable_indicator, category_indicator) -> ServerResponse:
        self.path = f"variable/{variable_indicator}/category/add/"
        response = await self.send_request(method="post", data={"category_indicator": category_indicator})
        return response

    async def remove_from_category(self, variable_indicator, category_indicator) -> ServerResponse:
        self.path = f"variable/{variable_indicator}/category/remove/"
        response = await self.send_request(method="post", data={"category_indicator": category_indicator})
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

    async def retrieve(self, variable_indicator: int) -> ServerResponse:
        self.path = f"variable/{variable_indicator}/retrieve/"
        response = await self.send_request(method="get", variable_indicator=variable_indicator)
        return response

    async def list(self, category_indicator) -> ServerResponse:
        self.path = "variable/list/"
        response = await self.send_request(
            method="get", category_indicator=category_indicator
        )
        return response

    async def nested_list(self, category_indicator) -> ServerResponse:
        self.path = "variable/nested_list/"
        response = await self.send_request(
            method="get", category_indicator=category_indicator
        )
        return response

    async def update(self, variable_indicator: int, data) -> ServerResponse:
        self.path = f"variable/{variable_indicator}/update/"
        response = await self.send_request(method="put", data=data)
        return response

    async def delete(self, variable_indicator: int) -> ServerResponse:
        self.path = f"variable/{variable_indicator}/delete/"
        response = await self.send_request(method="delete", variable_indicator=variable_indicator)
        return response

    async def multiple_delete(self, category_indicator: int):
        self.path = "variable/multiple-delete/"
        response = await self.send_request(method="delete", category_indicator=category_indicator)
        return response


variable_client = VariableClient()


class CategoryClient(Client):
    async def create(self, data) -> ServerResponse:
        self.path = "variable/category/create/"
        response = await self.send_request(method="post", data=data)
        return response

    async def add_to_parent(self, child, parent) -> ServerResponse:
        self.path = f"variable/category/{child}/add/"
        response = await self.send_request(method="post", data={"category_indicator": parent})
        return response

    async def remove_from_parent(self, child, parent) -> ServerResponse:
        self.path = f"variable/category/{child}/remove/"
        response = await self.send_request(method="post", data={"category_indicator": parent})
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

    async def retrieve(self, category_indicator: str) -> ServerResponse:
        self.path = f"variable/category/{category_indicator}/retrieve/"
        response = await self.send_request(method="get", category_indicator=category_indicator)
        return response

    async def list(self, parent: str = None) -> ServerResponse:
        self.path = "variable/category/list/"
        response = await self.send_request(
            method="get", parent=parent
        )
        return response

    async def update(self, category_indicator: str, data) -> ServerResponse:
        self.path = f"variable/category/{category_indicator}/update/"
        response = await self.send_request(method="put", data=data)
        return response

    async def delete(self, category_indicator: str) -> ServerResponse:
        self.path = f"variable/category/{category_indicator}/delete/"
        response = await self.send_request(method="delete", category_indicator=category_indicator)
        return response


category_client = CategoryClient()
