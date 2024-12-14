import uuid
import random
from enum import Enum
from typing import TypeAlias

# modeling

class MealTime(Enum):
    BREAKFAST = 1,
    LUNCH = 2,
    DINNER = 3

class FoodItem:
    def __init__(self, name: str, calories: int, carbs: int, fat: int, protein: int, sugars: int, fiber: int, meal_time: MealTime):
        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.fat = fat
        self.protein = protein
        self.sugars = sugars
        self.fiber = fiber
        self.meal_time = meal_time

    def __str__(self) -> str:
        return f"FoodItem(name={self.name}, calories={self.calories}, carbs={self.carbs}, fat={self.fat}, protein={self.protein}, sugars={self.sugars}, fiber={self.fiber}, meal_time={self.meal_time})"

    def __repr__(self) -> str:
        return str(self)

class MealCombination:
    def __init__(self, food_items: list[FoodItem]):
        if len(food_items) < 1:
            raise Exception("A meal combination cannot be empty")

        sliding_index_pairs: list[tuple[int, int]] = [(i, i + 1) for i in range(len(food_items) - 1)]
        for index_pair in sliding_index_pairs:
            if food_items[index_pair[0]].meal_time != food_items[index_pair[1]].meal_time:
                raise Exception("All food items in a meal combination must be the same meal time")

        self.food_items = food_items

    def meal_time(self) -> MealTime:
        return self.food_items[0].meal_time

    def total_calories(self) -> int:
        return sum(food_item.calories for food_item in self.food_items)

    def total_carbs(self) -> int:
        return sum(food_item.carbs for food_item in self.food_items)

    def total_fat(self) -> int:
        return sum(food_item.fat for food_item in self.food_items)

    def total_protein(self) -> int:
        return sum(food_item.protein for food_item in self.food_items)

    def total_sugars(self) -> int:
        return sum(food_item.sugars for food_item in self.food_items)

    def total_fiber(self) -> int:
        return sum(food_item.fiber for food_item in self.food_items)

    def __str__(self) -> str:
        return f"MealCombination(food_items={self.food_items})"

    def __repr__(self) -> str:
        return str(self)

# utils

def generate_food_items(amount: int) -> list[FoodItem]:
    """
    just utility function. this would normally be read from a DB
    """

    food_items: list[FoodItem] = []

    for _ in range(amount):
        name = str(uuid.uuid4())[:8] # just for convenience, is not significant
        calories = random.randint(100, 600)
        carbs = random.randint(0, 60)
        fat = random.randint(0, 50)
        protein = random.randint(0, 50)
        sugars = random.randint(0, 30)
        fiber = random.randint(0, 30)
        meal_time = random.choice(list(MealTime))

        food_items.append(FoodItem(name, calories, carbs, fat, protein, sugars, fiber, meal_time))

    return food_items

# core problem

DailyMealPlan: TypeAlias = tuple[MealCombination, MealCombination, MealCombination]

def find_all_daily_meal_plans(
    input_food_items: list[FoodItem],
    calorie_range: tuple[int, int],
    carbs_range: tuple[int, int],
    fat_range: tuple[int, int],
    protein_range: tuple[int, int],
    sugars_range: tuple[int, int],
    fiber_range: tuple[int, int]
) -> set[DailyMealPlan]:
    """
    goal: generate every possible daily meal plan given the input food items that meet the given nutritional requirements

    q&a: how many food items to aim for per meal combination? 2-4 is fair
    q&a: does it matter how evenly distributed the nutritional value is across meal combinations? no, just give every possible one

    hint: you will probably also want a find_all_meal_combinations function.
    hint: you will need 1 or more other functions to solve this recursively
    """

    daily_meal_plans: set[DailyMealPlan] = set()

    return daily_meal_plans
