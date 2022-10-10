cook_book = {}
dish_list = []
with open('List1.txt', 'rt', encoding='utf8') as file:
    for l in file:
        dish_name = l.strip()
        ingredients_list = []
        dish = {dish_name: ingredients_list}
        dish_count = file.readline()
        for i in range(int(dish_count)):
            dsh = file.readline().strip().split(' | ')
            ingredients_list.append({'ingredient_name': dsh[0],
                                     'quantity': int(dsh[1]),
                                     'measure': dsh[2]})
            dish_list.append(dish)
        cook_book.update(dish)
        blank_line = file.readline()
    print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for loc in cook_book[dish]:
                person_q = int(loc['quantity']) * person_count
                dict_list = {loc['ingredient_name']: {'measure': loc['measure'], 'quantity': person_q}}
                shop_list.update(dict_list)
        return shop_list


print(get_shop_list_by_dishes(['Омлет'], 2))

dishes = []
with open('List1.txt', 'rt', encoding='utf8') as file:
  for l in file:
    dish_name = l.strip()
    dish = {'name': dish_name, 'ingredient_ls': []}
    dish_count = file.readline()
    for i in range(int(dish_count)):
        dsh = file.readline().strip().split(' | ')
        dish['ingredient_ls'].append({'ingredient_name': dsh[0],
                                    'quatity': int(dsh[1]),
                                    'measure': dsh[2]})
        dishes.append(dish)
    blank_line = file.readline()


print(dishes)