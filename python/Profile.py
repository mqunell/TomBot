
#Profile class, reprensents a profile in discord.
#Parameters:
# name is a String for the user name
# messages is a list of length 5 that contains Strings
# times is a list of length 5 that contains floats
class Profile:
    __name = "None"
    __messages = [5]
    __times = [5]

    #Constrouctor
    def __init__(self, name, time, message):
        self.__name = name
        self.__times[0] = time
        self.__messages[0] = message

    #Print name of Profile for debugging
    def show(self):
        print("Show Name: " + self.__name);

    #Update profile
    def update(self, time, message):

        #Check the size of messages or times, only append if size list than 5
        if (len(self.__messages) > 5):
            self.__messages.pop(0)
            self.__times.pop(0)
        else:
            self.__messages.append(message)
            self.__times.append(time)

        j = 0
        for i in self.__messages:
            print(str(j) + " " + i)
            j += 1


        #Check for messages and times here
        #print("Identical Posts " + str(self.__check_Identical()))
        return self.__check_Identical()
        #self.__check_Messages()
        #self.__check_Times()

    #Check messages for the profile and determine if it is spam
    def __check_Messages(self):
        print("Checking messages")

    #Check message times for the profile and determine if it is spam
    def __check_Times(self):
        print("Checking times")

    #Check for identical messages that are next to each other
    def __check_Identical(self):

        #Subtract 1 from num_posts because of slice length, so
        #to check 2 posts put in 1, for 3, do 2 ect...
        num_posts = 2

        #Check boolean for return
        check = False

        #If there are not enough posts to check skip loop
        if (len(self.__messages) >= num_posts):

            #for every message in messages check its neigbors
            for i in range(len(self.__messages)):

                #Get appropriate slice to check neigbors
                list_2 = self.__messages[i:i + num_posts + 1]

                #Count the number of identical posts and compare with num_posts
                num_of_checks = 0

                #For element 0 check each other element, as if one is not the same
                #then it fails
                for j in range(len(list_2)):
                    if (j != len(list_2) - 1):
                        if (list_2[j] == list_2[j + 1]):
                            num_of_checks += 1
                if (num_of_checks == num_posts):
                    check = True
                    break
        return check
