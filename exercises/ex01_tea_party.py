"""Determining supplies needed for a tea party"""

__author__: str = "730520390"


def main_planner(guests: int) -> None:
    """Main function for tea party"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    "Determines number of tea bags"
    return people * 2


def treats(people: int) -> int:
    "Determines number of treats"
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    "Determines cost of the party"
    return (treat_count * 0.75) + (tea_count * 0.5)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
