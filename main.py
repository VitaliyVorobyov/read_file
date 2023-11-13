def cook_book_reader(path: str) -> dict:
    with open(path, 'r') as file:
        cook_book = {}
        for line in file:
            line = line.strip()
            if not line.isdigit() and '|' not in line and line != '':
                dish = line
                cook_book[dish] = []
            elif '|' in line:
                ingredient_name, quantity, measure = line.split('|')
                cook_book[dish].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    cook_book = cook_book_reader('recipes.txt')
    cook_dishes = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in cook_dishes.keys():
                cook_dishes[ingredient['ingredient_name']] = {}
                cook_dishes[ingredient['ingredient_name']].update({
                    'measure': ingredient['measure'], 'quantity': (int(ingredient['quantity'])*person_count)
                })
            elif ingredient['ingredient_name'] in cook_dishes.keys():
                cook_dishes[ingredient['ingredient_name']]['quantity'] += (int(ingredient['quantity'])*person_count)
    return cook_dishes


def file_reader(*file_names: str):
    count_string = {}
    for file_name in file_names:
        with open(file_name, 'r') as file:
            for lines in file:
                if file_name not in count_string.keys():
                    count_string[file_name] = 1
                elif file_name in count_string.keys():
                    count_string[file_name] += 1
    for elements in sorted(list(count_string.values()), reverse=True):
        for key, values in count_string.items():
            if values == elements:
                with open(key, 'r') as file_read:
                    with open('results.txt', 'a') as file_append:
                        file_append.write(f'{key}\n{elements}\n')
                    for line in file_read:
                        with open('results.txt', 'a') as file_add:
                            file_add.write(f'{line.strip()}\n')
    return


print(cook_book_reader('recipes.txt'))
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
file_reader('1.txt', '2.txt', '3.txt')
