def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо пропуски та символи нового рядка
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки
                
                # Розділяємо рядок на ім'я та зарплату
                parts = line.split(',')
                if len(parts) != 2:
                    # Якщо формат неправильний — пропускаємо рядок
                    continue

                salary_str = parts[1]
                try:
                    salary = int(salary_str)
                    total += salary
                    count += 1
                except ValueError:
                    # Якщо зарплата не є числом — пропускаємо рядок
                    continue

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return (0, 0)
    
    # Пошкоджений файл = помилка при читанні
    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")
        return (0, 0)



# Приклад використання:
total, average = total_salary("salaries/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# Файл відсутній
total, average = total_salary("salaries/salary_file_not_existant.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
