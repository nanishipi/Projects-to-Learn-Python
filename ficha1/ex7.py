dataset = [
    ["user_name", "age", "weight"],
    ["Rui", 18, 75],
    ["Pedro", 28, 82],
    ["Mafalda", 33, 53],
]


def format_txt(text: str) -> str:
    return text.replace("_", " ").title()


def nice_print(dataset):
    formatted_username_header = format_txt(dataset[0][0])
    
    W_NAME = 10
    W_AGE = 5
    W_WEIGHT = 8

    header_line = (
        f"{formatted_username_header:<{W_NAME}} | "
        f"{dataset[0][1]:^{W_AGE}} | "
        f"{dataset[0][2]:>{W_WEIGHT}}"
    )
    print(header_line)
    
    print("-" * len(header_line))

    for elements in dataset[1:]: 
        data_line = (
            f"{elements[0]:<{W_NAME}} | "
            f"{elements[1]:^{W_AGE}} | "
            f"{elements[2]:>{W_WEIGHT}}"
        )
        print(data_line)
        

nice_print(dataset)
print(format_txt("user_name"))