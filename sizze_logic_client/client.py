from sizze_logic_client.api import variables, actions, filters


variables_client = variables.VariableClient()
actions_client = actions.ActionClient()
filter_client = filters.FilterClient()


def client(base_url: str):
    variables_client.set_base_url(base_url)
    actions_client.set_base_url(base_url)
    filter_client.set_base_url(base_url)
