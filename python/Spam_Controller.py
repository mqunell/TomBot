import python.Profile

#Spam Controller class for the bot
class Spam_Controller:

    __profiles = {}
    __num_messages = 5
    __time_posts = 10
    __num_identical = 2

    #Check if the User is creating spam
    def check_spam(self, name, time, message):

        #Determine if the user is already a profile
        if name in self.__profiles:
            return self.__profiles[name].update(time, message)
        else:
            self.__profiles[name] = python.Profile.Profile(name, time, message)
            print("Added to Profiles")
            self.__profiles[name].show()
            return False