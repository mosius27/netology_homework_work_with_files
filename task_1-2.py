# -*- coding: utf-8 -*-
import json

class Cooking():

    # Инициализация класа Cooking и создание словаря с рецептами
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            recipes = []
            recipe = []
            for line in file:
                line = line.strip()
                if line == '':
                    recipes.append(recipe)
                    recipe = []
                else:
                    recipe.append(line.strip())

        self.cook_book = {}
        for recipe in recipes:
            self.cook_book[recipe[0]] = []
            nums_igredients = recipe[1]
            for i in range(2, 2 + int(nums_igredients)):
                ingredient = recipe[i].split(' | ')
                self.cook_book[recipe[0]].append({'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})

    # Определение количества необходимых для блюд готовки на определенное количество людей 
    def get_shop_list_by_dishes(self, dishes: list, person_count: int) -> dict:
        shop_list = {}
        for dish in dishes:
            for ingredient in self.cook_book[dish]:
                shop_list.setdefault(ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': 0})
                shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count

        return shop_list

if __name__ == '__main__':
    cook_book = Cooking('./files/task_1-2/recipes.txt')
    person_count = int(input('Укажите на какое количество человек готовить: '))
    shop_list = cook_book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], person_count)