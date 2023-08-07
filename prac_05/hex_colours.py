"""
CP1404 Practical - Austin Liandro
Hexadecimal colour lookup
"""

CODE_COLOURS = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Aquamarine1": "#7fffd4",
                "Amaranth": "#e52b50", "Amethyst": "#9966cc", "Azure1": "#f0ffff", "Azure2": "e0eeee",
                "Azure3": "#c1cdcd", "Barn Red": "#7c0a02", "Bistre": "#3d2b1f"}

colours = input("Enter the colour name: ")
while colours != "":
    print(f"The code for {colours} colour is {CODE_COLOURS.get(colours)}.")
    colours = input("Enter the colour name: ")