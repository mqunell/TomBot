
#Spam Controller class for the bot 
class Spam_Controller:

    __profiles = {}
    __num_messages = 5
    __time_posts = 10
    __num_identical = 2

    #Check if the User is creating spam
    def check_spam(self, name):
        return "Checking " + name + " if is spam"