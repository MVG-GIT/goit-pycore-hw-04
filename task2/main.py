def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки
                
                parts = line.split(',')
                if len(parts) != 3:
                    # Якщо формат рядка неправильний - пропускаємо
                    continue
                
                cat_id, name, age = parts
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

        return cats

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return (0, 0)
    
    # Пошкоджений файл = помилка при читанні
    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")
        return (0, 0)


# Приклад використання:
cats_info = get_cats_info("cats.txt")
print(cats_info)

# Файл відсутній
cats_info = get_cats_info("kitties.txt")
print(cats_info)
