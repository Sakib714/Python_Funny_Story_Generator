import pyttsx3

engine = pyttsx3.init()

# rate
engine.setProperty('rate', 150)

# voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text=text)
    engine.runAndWait()

speak('Welcome to funny story generator.')
print('Welcome to funny story generator.')


speak('Enter a town name')
town_name = input('\nEnter a town name: ')


speak('Enter a name of your female family member: ')
family_member = input('\nEnter a name of your female family member: ')

speak('Enter a describing word')
describing_word = input('\nEnter a describing word: ')

speak('Enter a action word')
action_word = input('\nEnter a action word: ')

speak('Enter a object')
object = input('\nEnter a object: ')

speak('Enter a place name: ')
place_name = input('\nEnter a object: ')


# Generating story

story = f'One day in {town_name}. I saw my {family_member} acting {describing_word}. She was {action_word}ing a big {object}. Then she want to {place_name} and did it again!'

print(story)
speak(story)
