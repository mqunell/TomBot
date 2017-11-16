import requests


class HearthstoneApis:

    api_key = ""


    def __init__(self):

        # Parse the API key
        key_file = open("../keys/hearthstone_key", "r")
        self.api_key = key_file.read().strip()
        key_file.close()


    # Hearthstone card
    def card(self, card):

        # Web address
        url = "https://omgvamp-hearthstone-v1.p.mashape.com/cards/search/%s" % card

        # Create a request, attach the key
        request = requests.Session()
        request.headers.update({"X-Mashape-Key": self.api_key})

        # Get, parse, and print the information
        data = request.get(url).json()

        output = ""

        # Check its validity - "error" key is only in invalid data
        if "error" not in data:

            # Post the first image link
            for d in data:
                if "img" in d and "collectible" in d:
                    output = d["img"]
                    break

        else:

            # Card not found error
            if data["error"] == 404:
                output = "Card not found."

            else:
                output = "Error code 2"

        return output