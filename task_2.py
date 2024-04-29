def get_cats_info(path):
    cats_info = []
 
    try:
        # Відкриття файлу та обробка його рядків
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділення рядка за комою
                cat_data = line.strip().split(',')
                # Створення словника з інформацією про кота
                cat_info = {
                    'id': cat_data[0],
                    'name': cat_data[1],
                    'age': int(cat_data[2])
                }
                # Додавання кота в словник
                cats_info.append(cat_info)

    except FileNotFoundError:
        print(f"-= Файл '{path}' не знайдено! =-")
        return None

    return cats_info

# Приклад використання функції
path_to_file = 'cats.txt'
cats = get_cats_info(path_to_file)

# Виводимо красиво вміст словника cats
if cats is not None:
    for cat in cats:
        print(cat)
