# Mad Libs Game 🎭 - Python Project

def mad_libs():
    print("Welcome to the Mad Libs Game! 🎉\n")
    

    name = input("Enter a name: ")
    animal = input("Enter an animal: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb: ")
    food = input("Enter a food item: ")

    
    story = f"""
    Once upon a time, {name} was walking through the {place} when they saw a {animal}.
    The {animal} looked at {name} and suddenly started to {verb}!
    Surprised, {name} decided to join in and together they had an amazing time.
    At the end of the day, they both enjoyed a delicious {food} and became best friends! 🍽️😄
    """


    print("\n✨ Here is your Mad Libs story: ✨")
    print(story)
mad_libs()
