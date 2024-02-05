def get_cats_info(path):
    cat_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                # Розділяємо дані про кота
                data = line.strip().split(',')

                # Перевіряємо чи є 3 значення
                if len(data) == 3:
                    # Створюємо словник
                    cat_info = {"id": data[0], "name": data[1], "age": data[2]}
                    cat_list.append(cat_info)

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")

    return cat_list

# Приклад використання
cats_info = get_cats_info("task2.txt")
print(cats_info)