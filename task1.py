def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_salary = 0
            num_developers = 0
            
            for line in lines:
                # Розділяємо дані про розробника за комою
                data = line.strip().split(',')
                
                # Перевіряємо, чи отримано два значення
                if len(data) == 2:
                    # Додаємо зарплату до загальної суми та збільшуємо кількість розробників
                    total_salary += int(data[1])
                    num_developers += 1
            
            # Обчислюємо середню зарплату
            average_salary = total_salary / num_developers if num_developers > 0 else 0
            
            return total_salary, average_salary
        
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")

# Приклад
total, average = total_salary("task1.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")