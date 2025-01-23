"""Writing a code that performs multiple individual tasks"""

__author__: str = "730830842"


def main_planner(guests: int) -> None:
    """Prints each function in code given number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculates the amount of teabags."""
    return 2 * people


def treats(people: int) -> int:
    """Calculates the amount of treats."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost based on amount of treats and tea bags."""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
