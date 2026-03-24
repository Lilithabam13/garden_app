# The garden_advice app offers gardening advice to users based
# on season and plant type

# Prompt user for the current season
season = input("Enter the season (summer/winter)").lower()


# Prompt user for the plant type
plant_type = input("Enter the plant type (flower/vegatable)").lower()

# Variable to store gardening advice
advice = ""

# Conditional statements determine advice based on the season entered by user.
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Conditional statements determine advice based on the plant type
# entered by user.
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Prints the gardening advice to the user.
print(advice)


# Not part of final issue 2
# ----------------------------------------------

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.

# ----------------------------------------------
