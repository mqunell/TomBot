
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

    #Print name of Profile for debugging
    def show(self):
        print(self.name);

    #Update profile
    def update(self):
        print("updating")

    #Check messages for the profile and determine if it is spam
    def __check_Messages(self):
        print("Checking messages")

    #Check message times for the profile and determine if it is spam
    def __check_Times(self):
        print("Checking times")