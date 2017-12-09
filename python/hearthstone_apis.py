import requests


# Encapsulates Hearthstone APIs
class HearthstoneApis:

    api_key = ""


    def __init__(self):

        # Parse the API key
        key_file = open("../keys/hearthstone_key", "r")
        self.api_key = key_file.read().strip()
        key_file.close()


    # Hearthstone card
    def card(self, card):
        """ Return image link in string

        Accesses Mashape's Hearthstone API to get a card's image link
        """

        # Web address
        url = "https://omgvamp-hearthstone-v1.p.mashape.com/cards/search/%s" % card

        # Create a request, attach the key
        request = requests.Session()
        request.headers.update({"X-Mashape-Key": self.api_key})

        # Get, parse, and print the information
        data = request.get(url).json()

        # Final output if data contains > 0 cards, but none of them have images to display
        output = "%d card%s found, but no image%s to display" % (len(data),
                                                                 "" if len(data) > 1 else "s",
                                                                 "" if len(data) > 1 else "s")

        # Check its validity - "error" key is only in invalid data
        if "error" not in data:

            # Post the first image link
            for d in data:
                if "img" in d:
                    if "collectible" in d:
                        output = d["img"]
                        break

                    else:
                        output = "Did not find a collectible card, but found this (might not work):\n%s" % d["img"]

        else:

            # Card not found error
            if data["error"] == 404:
                output = "Card not found."

            else:
                output = "Hearthstone API error. (non-404)"

        return output
