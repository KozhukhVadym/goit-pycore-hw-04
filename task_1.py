def total_salary(path):
    total_salary = 0
    count = 0 

    try: # Облобка виключення
        # Відкриття файлу правильним чином
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # обробка рядка та вирізання сепаратора ','
                surname, salary = line.strip().split(',')

                # Обчислюємо загальну суму зарплат
                total_salary += int(salary)
                count += 1

        # Обчислення середньої заробітної плати
        if count != 0:
            average_salary = total_salary / count
            
        else:
            print("Файл пошкоджений або відсутній")
            average_salary = 0

        print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}")

    except FileNotFoundError:
        print(f"-= Файл '{path}' не знайдено! =-")
    
# Приклад використання функції
path_to_file = 'salary.txt'
total_salary(path_to_file)
