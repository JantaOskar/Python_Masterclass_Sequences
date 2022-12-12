menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

# deleting spam from lists:

for meal in menu:
    top_index = len(meal) - 1
    for index, value in enumerate(reversed(meal)):
        if value == "spam":
            del meal[top_index - index]
    print(", ".join(meal))

