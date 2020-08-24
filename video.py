"""
Pedro Tortello - 24/08/2020
IBM Behind the code marathon - Challenge #3

Retrieves data from given urls and saves into JSON files.
For "body" content check TXT file.
"""

from bs4 import BeautifulSoup
from requests import get
from json import dump


def jsoner(address):
    # Webscraping address argument
    req = get(address).text
    soup = BeautifulSoup(req, 'lxml')
    data = soup.title.text

    # Putting data into dictionary
    dataDict = {}
    dataDict["title"] = data[data.find(':')+2:data.find('|')-1]
    dataDict["author"] = data[:data.find(':')]
    dataDict["body"] = ""
    dataDict["type"] = "video"      # hard coded type !!
    dataDict["url"] = address

    # Creating JSON file
    filename = dataDict["author"].replace(" ", "") + "_video.json"  # !!
    with open(filename, "w", encoding="utf-8") as file:
        dump(dataDict, file, indent=4, ensure_ascii=False)


# Given urls list
addresses = [
"https://www.ted.com/talks/helen_czerski_the_fascinating_physics_of_everyday_life/transcript?language=pt-br#t-81674",
"https://www.ted.com/talks/kevin_kelly_how_ai_can_bring_on_a_second_industrial_revolution/transcript?language=pt-br",
"https://www.ted.com/talks/sarah_parcak_help_discover_ancient_ruins_before_it_s_too_late/transcript?language=pt-br",
"https://www.ted.com/talks/sylvain_duranton_how_humans_and_ai_can_work_together_to_create_better_businesses/transcript?language=pt-br",
"https://www.ted.com/talks/chieko_asakawa_how_new_technology_helps_blind_people_explore_the_world/transcript?language=pt-br",
"https://www.ted.com/talks/pierre_barreau_how_ai_could_compose_a_personalized_soundtrack_to_your_life/transcript?language=pt-br",
"https://www.ted.com/talks/tom_gruber_how_ai_can_enhance_our_memory_work_and_social_lives/transcript?language=pt-br"
]

# Main loop
for address in addresses:
    jsoner(address)
