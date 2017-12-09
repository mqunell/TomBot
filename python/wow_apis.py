import requests


# Encapsulates World of Warcraft APIs
class WowApis:

    api_key = ""

    # Dictionaries for parsing in item_level()
    wow_races = {1: "Human", 2: "Orc", 3: "Dwarf", 4: "Night Elf", 5: "Undead", 6: "Tauren", 7: "Gnome", 8: "Troll",
                 9: "Goblin", 10: "Blood Elf", 11: "Draenei", 22: "Worgen", 25: "A. Panda", 26: "H. Panda"}

    wow_classes = {1: "Warrior", 2: "Paladin", 3: "Hunter", 4: "Rogue", 5: "Priest", 6: "Death Knight",
                   7: "Shaman", 8: "Mage", 9: "Warlock", 10: "Monk", 11: "Druid", 12: "Demon Hunter"}

    # Final output for item_level()
    item_level_invalid = "Invalid character name and/or server"

    # Final output for mythic_plus()
    mythic_plus_not_found = "Could not find character"


    def __init__(self):

        # Parse the API key
        key_file = open("../keys/wow_key", "r")
        self.api_key = key_file.read().strip()
        key_file.close()


    # Average item level
    def item_level(self, character, server):
        """ Return formatted item level string

        Accesses the Battle.net API to get a character's level, race, class, and average item level
        """

        # Web address
        fields = "items&"  # Change for different fields
        url = "https://us.api.battle.net/wow/character/%s/%s?fields=%slocale=en_US&apikey=%s" \
              % (server, character, fields, self.api_key)

        # Make the request
        r = requests.get(url)

        output = ""

        # If the request is successful
        if r.status_code == 200:

            # Retrieve the data
            data = r.json()

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
            output += "%s-%s\n" % (character.title(), server.title())
            output += "%d %s %s\n" % (character_level, character_race, character_class)
            output += "Average item level: %d" % character_ilevel

        else:
            output += self.item_level_invalid

        return output


    # Mythic Plus info
    def mythic_plus(self, character, server):
        """ Return formatted Mythic Plus string

        Accesses the Raider.IO API to get a character's overall Mythic Plus score, highest completed Mythic Plus dungeon
        in the last week, and a link to their Raider.IO profile
        """

        # Web address
        url = "https://raider.io/api/v1/characters/profile?region=us&realm=%s&name=%s" % (server, character)
        url += "&fields=mythic_plus_scores%2Cmythic_plus_weekly_highest_level_runs"

        # Make the request
        r = requests.get(url)

        output = ""

        # If the request is successful
        if r.status_code == 200:

            # Retrieve the data
            data = r.json()

            # Name
            name = data["name"]

            # Profile URL
            profile_url = data["profile_url"]

            # Overall M+ score
            overall_score = data["mythic_plus_scores"]["all"]

            # Attempt to find the highest completed in the last week
            highest = "-"
            if len(data["mythic_plus_weekly_highest_level_runs"]) > 0:
                highest = "%s %d" % (data["mythic_plus_weekly_highest_level_runs"][0]["dungeon"],
                                     data["mythic_plus_weekly_highest_level_runs"][0]["mythic_level"])

            output += "%s-%s\n" % (character.title(), server.title())
            output += "Overall Mythic Plus score: %s\n" % overall_score
            output += "Highest Mythic Plus this week: %s\n" % highest
            output += "Raider.IO profile: <%s>\n" % profile_url

        else:
            output = self.mythic_plus_not_found

        return output


    # All WoW API info
    def all(self, character, server):
        """ Return formatted item level and Mythic Plus string

        Gathers information from both other WowApis functions
        """

        # Get the item_level() info
        output = self.item_level(character, server)

        # If valid item_level() info was received, attempt to get mythic_plus() info
        if output != self.item_level_invalid:
            output += "\n\n"

            mplus = self.mythic_plus(character, server)

            # If valid mythic_plus() info was received, parse it to remove "<name>-<server>"
            if mplus != self.mythic_plus_not_found:
                output += mplus[mplus.index("\n")+1:]

            else:
                output += "No Mythic Plus data"

        return output
