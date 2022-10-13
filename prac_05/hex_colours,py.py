HEXADECIMAL_CODE_TO_COLOUR = {"amethyst": "#9966cc", "absolute zero": "#0048ba", "acid green": "#b0bf1a",
                              "aliceblue": "#f0f8ff", "amaranth": "#e52b50", "aqua": "#00ffff", "bone": "#e3dac9",
                              "boysenberry": "#873260", "chocolate": "	#d2691e", "nyanza": "#e9ffdb"}

colour = input("Name of Colour: ").lower()
while colour != "":
    try:
        print(f"The hexadecimal code for {colour} is {HEXADECIMAL_CODE_TO_COLOUR[colour]}")
    except KeyError:
        print("invalid colour")
    colour = input("Name of Colour: ").lower()
