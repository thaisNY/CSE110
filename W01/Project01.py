"""
Thais Rodrigues

Project 01: Clever Stories

Enhancements:
1. Expanded the story with more prompts to make it more engaging.
2. Added logic to automatically select "a" or "an" before the animal.
3. The exclamation is automatically capitalized regardless of user input.
"""

# Function to determine "a" or "an"
def a_or_an(word):
    vowels = 'aeiou'
    if word[0].lower() in vowels:
        return 'an'
    else:
        return 'a'

adjective = input("Type an adjective: ").lower()
animal = input("Type an animal name: ").lower()
verb1 = input("Type a verb: ").lower()
exclamation = input("Type an exclamation: ").capitalize()
verb2 = input("Type another verb: ").lower()
verb3 = input("Type a final verb: ").lower()
place = input("Type a place: ").capitalize()
plural_noun = input("Type a plural animal noun: ").lower()

print(f"""
The other day, I was really in trouble. It all started when I saw {a_or_an(animal)} very {adjective} {animal} {verb1} down the hallway. 
"{exclamation}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} 
right in front of my family. Then, we all ran to {place}, where we were surrounded by {plural_noun}.
""")
