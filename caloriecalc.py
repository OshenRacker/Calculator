def main():
    print("Калькулятор калорий")
    print("Введите данные о еде. Для завершения введите 'стоп'.")

    food_data = {}
    total_calories = 0

    while True:
        food = input("Название еды (или 'стоп' для завершения): ").strip().lower()
        if food == 'стоп':
            break

        try:
            servings = float(input(f"Количество порций '{food}': "))
            calories_per_serving = float(input(f"Калорий в одной порции '{food}': "))
        except ValueError:
            print("Ошибка: введите числовое значение для порций и калорий.")
            continue

        calories = servings * calories_per_serving
        total_calories += calories

        if food in food_data:
            food_data[food]['servings'] += servings
            food_data[food]['calories'] += calories
        else:
            food_data[food] = {'servings': servings, 'calories': calories}

    print("\nРезультаты:")
    print(f"Уникальных типов еды: {len(food_data)}")
    print(f"Общее количество калорий: {total_calories:.2f} ккал")

    for food, data in food_data.items():
        print(f"- {food}: {data['servings']} порций, {data['calories']:.2f} ккал")

if __name__ == "__main__":
    main()
