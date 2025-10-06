lista = [
    "lamp_hall_1",
    "lamp_hall_2",
    ["lamp_sala_1", "lamp_sala_2", "lamp_sala_3"],
    ["lamp_cozinha_1", "lamp_cozinha_2"],
    ["lamp_quarto_1"],
    ["lamp_banho_2"],
]


def flat_list(nested_list):
    """
    Flattens a list that may be nested to an arbitrary depth.
    """
    flat = []  # 1. Initialize the result list for the current call
    for element in nested_list:
        if isinstance(element, list):
            # 2. Recursive Step: The function calls itself
            #    to flatten the sublist (the simpler problem).
            flattened_sublist = flat_list(element)
            flat.extend(flattened_sublist)
        else:
            # 3. Base Case Action: Add the single item to the result list.
            flat.append(element)
    return flat

print(flat_list(lista))