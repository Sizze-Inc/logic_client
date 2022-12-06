from sizze_logic_client.api import variables, actions


variables_client = None
actions_client = None


def client(base_url: str):
    global variables_client, actions_client
    variables_client = variables.VariableClient(base_url=base_url)
    actions_client = variables.VariableClient(base_url=base_url)
