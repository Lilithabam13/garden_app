# The garden_advice app offers gardening advice to users based
# on season and plant type 


def user_season():
    """Prompt user for the current season."""
    return input("Enter the season (summer/winter): ").lower()


def user_plant_type():
    """Prompt user for the plant type."""
    return input("Enter the plant type (flower/vegatable)").lower()


def season_advice(season):
    """Returns advice to user based on season."""

    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"

    elif season == "winter":
        return "Protect your plants from frost with covers.\n"

    else:
        return "No advice for this season.\n"


def plant_type_advice(plant_type):
    """Returns advice to user based on plant type."""

    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."

    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"

    else:
        return "No advice for this type of plant."


def main():
    """Main function to run garden application."""

    season = user_season()
    plant_type = user_plant_type()

    advice = ""

    season_message = season_advice(season)
    advice = advice + season_message

    plant_type_message = plant_type_advice(plant_type)
    advice = advice + plant_type_message

    print(advice)
