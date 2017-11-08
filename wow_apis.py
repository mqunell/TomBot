import requests


class WowApi:

    api_key = ""

    wow_races = {1: "Human", 2: "Orc", 3: "Dwarf", 4: "Night Elf", 5: "Undead", 6: "Tauren", 7: "Gnome", 8: "Troll",
                 9: "Goblin", 10: "Blood Elf", 11: "Draenei", 22: "Worgen", 25: "A. Panda", 26: "H. Panda"}

    wow_classes = {1: "Warrior", 2: "Paladin", 3: "Hunter", 4: "Rogue", 5: "Priest", 6: "Death Knight",
                   7: "Shaman", 8: "Mage", 9: "Warlock", 10: "Monk", 11: "Druid", 12: "Demon Hunter"}


    def __init__(self):

        # Parse the API key
        key_file = open("PATH TO FILE", "r")
        self.api_key = key_file.read().strip()
        key_file.close()


    # World of Warcraft average item level
    def wow_item_level(self, character, server):

        # Format the input
        character = character.title()
        server = server.title()

        # Web address
        fields = "items&"  # Change for different fields
        url = "https://us.api.battle.net/wow/character/%s/%s?fields=%slocale=en_US&apikey=%s" \
              % (server, character, fields, self.api_key)

        # Retrieve the data
        data = requests.get(url).json()

        output = ""

        # Check its validity - "status" key is only in invalid data
        if "status" not in data:

            # Level
            character_level = int(data['level'])

            # Race
            race_num = int(data['race'])
            character_race = self.wow_races[race_num]

            # Class
            class_num = int(data['class'])
            character_class = self.wow_classes[class_num]

            # Average item level
            character_ilevel = data['items']['averageItemLevel']

            # Remove the "-" from a server name for displaying
            server = server.replace("-", " ")

            # Output
            output += "%s-%s\n" % (character, server)
            output += "%d %s %s\n" % (character_level, character_race, character_class)
            output += "Average item level: %d" % character_ilevel

        else:
            output += "Invalid character name and/or server"

        return output