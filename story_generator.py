import random as rnd


def madlib(name, role, place, adjective, verb):
    name = name.get()
    role = role.get()
    place = place.get()
    adjective = adjective.get()
    verb = verb.get()

    return f"I am {name.capitalize()}, I came from {place.capitalize()}, a {adjective.lower()} place." \
           f" Back home, I'm known as a {role.capitalize()}, who's job is to {verb.lower()}. One day, my" \
           f" adventures will bring back either treasure, love, or glory!"


def random_madlib():
    name = ["James", "Lucas", "Sophia", "Elijah", "Emma", "Amelia"]
    role = ["Engineer", "Soldier", "Knight", "Caretaker", "Doctor"]
    place = ["Rochester", "Keltner", "Pinton", "Wyno", "Qaziun", "Trinton"]
    place_filler = [" came into the land of", " journey into", " explores through"]
    role_filler = ["an found employment as a", "to become a well-known", "working in the field as a"]
    begin_story = ["The story begins as", "As", "It was time that"]
    story_element = ["They'd soon learn they would have to work vigorously every coming day", "Their life became " +
                     "routine, work became increasingly more transient", "As time passed, work had given them new " +
                     "experiences both good and bad"]
    end_story = ["The time eventually came for them to move onto new ventures", "Finally accomplishing their dreams," +
                 " they'd continue to work for the people"]
    return f"{rnd.choice(begin_story)} {rnd.choice(name)}{rnd.choice(place_filler)} {rnd.choice(place)}" \
           f" {rnd.choice(role_filler)} {rnd.choice(role)}. {rnd.choice(story_element)}. {rnd.choice(end_story)}."
