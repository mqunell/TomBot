import python.Profile


#Spam Controller class for the bot
#the_num_messages: Number of messages in a given time frame
#the_time_posts: Time frame for posts
#the_num_identical: Number of identical adjacent posts allowed.
class Spam_Controller:

    #List to hold profiles
    __profiles = {}

    #Num of messages within that can be posted in a given time frame
    __num_messages = 5

    #Seconds between posts of total num_messages
    __time_posts = 10

    #Number of identical messages that can be posted
    __num_identical = 2

    #Constructor for creating a spam controller
    def __init__(self, the_num_messages, the_time_posts, the_num_identical):
        self.__num_messages = the_num_messages
        self.__time_posts = the_time_posts
        self.__num_identical = the_num_identical

    #Check if the User is creating spam.
    #name: Author of the message
    #time: Time of the post
    #message: Content of the post
    def check_spam(self, name, time, message):

        #Determine if the user is already a profile
        if name in self.__profiles:
            return self.__profiles[name].update(time, message,
                                                self.__num_messages,
                                                self.__time_posts,
                                                self.__num_identical)
        else:
            self.__profiles[name] = python.Profile.Profile(name, time, message)

            #Debugging code
            #print("User added to Profiles")
            #self.__profiles[name].show()
            return False