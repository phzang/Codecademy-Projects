"""Introduction

Opening your comic book store, the Sorcery Society, has been a lifelong
dream come true. You quickly diversified your shop offerings to include
miniatures, plush toys, collectible card games, and board games. Eventually,
the store became more a games store with a selection of this week's newest
comic books and a small offering of graphic novel paperbacks. Completing
your transformation means offering space for local tabletop gamers. They
love to play their favorite RPG, "Abruptly Goblins!" and will happily pay
you per chair to secure the space to do it. Unfortunately, planning the game
night has fallen to you. If you pick the wrong night, not enough people will
come and the game night will be cancelled. You decide it's best that you
automate the game night selector to get the most people through the door.
First you need to create a list of people who will be attending the game night.
"""


"""Each gamer should be a dictionary with the following keys:

    "name": a string that contains the gamer's full or presumed name. E.g.,
    "Vicky Very"
    "availability": a list of strings containing the names of the days of the
    week that the gamer is available. E.g., ["Monday", "Thursday", "Sunday"]"""

gamers = []

def add_gamer(gamer, gamers_list):
    if ['name','availability'] == list(gamer.keys()):
        gamers_list.append(gamer)
    

kiberly = {'name':'Kimberly Warner', 'availablility': ["Monday", "Tuesday", "Friday"]}
add_gamer(kiberly, gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


"""Create a function called build_daily_frequency_table that takes no argument returns a dictionary with
the days of the week as keys and 0s for values. We'll be using this to count the availability per night.
Call build_daily_frequency_table and save the results to a variable called count_availability"""

def build_daily_frequency_table():
    return { "Sunday": 0, "Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0,
             "Friday": 0, "Saturday": 0 }

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        days = gamer['availability']
        for day in days:
            available_frequency[day] += 1
  
            
calculate_availability(gamers,count_availability)

def find_best_night(availability_table):
    return max(availability_table, key=availability_table.get)

game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list, day):
    name_list = []
    for gamer in gamers_list:
        days = gamer['availability']
        for gamer_day in days:
            if gamer_day == day:
                name_list.append(gamer['name'])
    return name_list

attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)

form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
the Sorcery Society
"""

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer['name'], day_of_week=day, game=game))
        
send_email(attending_game_night, game_night, "Abruptly Goblins!")
