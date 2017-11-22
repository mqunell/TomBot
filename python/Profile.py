
#Profile class, reprensents a profile in discord.
#Parameters:
# name is a String for the user name
# messages is a list of length 5 that contains Strings
# times is a list of length 5 that contains floats
class Profile:
    __name = "None"
    __messages = []
    __times = []

    #Constrouctor
    def __init__(self, name, time, message):
        self.name = name
        self.times = [time]
        self.messages = [message]

    def show(self):
        print(self.name);

    def update(self):
        print("updating")

    def __check_Messages(self):
        print("Checking messages")

    def __check_Times(self):
        print("Checking times")