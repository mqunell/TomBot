import re


# Profile class, reprensents a profile in discord.
# Parameters:
# name is a String for the user name
# messages is a list of length 5 that contains Strings
# times is a list of length 5 that contains floats
class Profile:
    __name = "None"
    __messages = [5]
    __times = [5]

    # Constructor
    def __init__(self, name, time, message):
        self.__name = name
        self.__times[0] = self.__splice_time(time)
        self.__messages[0] = message

    # Print name of Profile for debugging
    def show(self):
        print("Show Name: " + self.__name);

    # Update profile
    def update(self, time, message, num_messages, time_posts, num_identical):

        # Check the size of messages or times, only append if size list than 5
        if (len(self.__messages) >= 5):
            self.__messages.pop(0)
            self.__times.pop(0)

        self.__messages.append(message)
        self.__times.append(self.__splice_time(time))

        #For debugging
        #j = 0
        #print("------------")
        #for i in self.__times:
            #print(str(j) + ". " + str(i))
            #j += 1

        # Check for messages and times here
        # print("Identical Posts " + str(self.__check_Identical()))
        return self.__check_Identical(num_identical) or self.__check_times(num_messages,time_posts)

    # Check message times for the profile and determine if it is spam
    def __check_times(self, num_messages, num_posts_in_secs):

        check = False

        # check if the length of times is large enough
        if (len(self.__times) >= num_messages):

            # for each time check its most recent times up to num_messages
            for i in range(len(self.__times)):

                # get the times to check
                list_2 = self.__times[i:i + num_messages]

                #count how many are in violation of the rule
                num_of_checks = 0

                #loop through all the times in the new list
                for j in range(len(list_2)):

                    # Check to see if j is at end of list
                    if (j != len(list_2) - 1):
                        # If the mins times are the same and the difference from each time to the last post is less
                        # than the num_posts_in_secs than it is in violation
                        if (list_2[j][0:3] == list_2[j + 1][0:3] and
                                    (int(list_2[j + 1][3:]) - int(list_2[0][3:])) < num_posts_in_secs):
                            num_of_checks += 1

                # check if there are to many violations
                if (num_messages - 1 == num_of_checks):
                    check = True
        else:
            check = False

        #print("Check Times: " + str(check))
        return check

    # Check for identical messages that are next to each other
    def __check_Identical(self, num_identical):

        # Subtract 1 from num_posts because of slice length, so
        # to check 2 posts put in 1, for 3, do 2 ect...
        num_posts = num_identical - 1

        # Check boolean for return
        check = False

        # If there are not enough posts to check skip loop
        if (len(self.__messages) >= num_posts):

            # for every message in messages check its neigbors
            for i in range(len(self.__messages)):

                # Get appropriate slice to check neigbors
                list_2 = self.__messages[i:i + num_posts + 1]

                # Count the number of identical posts and compare with num_posts
                num_of_checks = 0

                # For element 0 check each other element, as if one is not the same
                # then it fails
                for j in range(len(list_2)):

                    # checking if j is at the end of the list
                    if (j != len(list_2) - 1):
                        if (list_2[j] == list_2[j + 1]):
                            num_of_checks += 1

                if (num_of_checks == num_posts):
                    check = True
                    break
        return check

    # Splices the time given so that the reutrned String is only the seconds left in that minute
    def __splice_time(self, time):
        new_time = time[14:19]
        return new_time
