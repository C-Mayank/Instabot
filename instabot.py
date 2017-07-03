#importing 'requests' package
import requests

#define access token of your account
ACCESS_TOKEN = '5683656431.a4b1c44.182dcfe7f7124b2d9b873838cfa886bc'

#define base url
BASE_URL = 'https://api.instagram.com/v1/'




#function to read details of self account
def self_info():
    #get the request url
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
    #print the request url
    print "GET request url: %s" % (request_url)
    user_info = requests.get(request_url).json()

    #check if the request status is OK or not
    if user_info["meta"]["code"] == 200:
        #check if user exists or not
        if len(user_info["data"]):
            #print the details
            print "Username: %s" %(user_info["data"]["username"])
            print "Full Name: %s" % (user_info["data"]["full_name"])
            print "Bio: %s" % (user_info["data"]["bio"])
            print "Website: %s" % (user_info["data"]["website"])
            print "Number of followers: %s" % (user_info["data"]["counts"]["followed_by"])
            print "Number of post: %s" % (user_info["data"]["counts"]["media"])
            print "Number of people you are following: %s" % (user_info["data"]["counts"]["follows"])
        else:
            print "User does not exist!!!"
    else:
        print "INVALID REQUEST!!!"
        print "Please check the request"



#function to get user id
def get_user_id(insta_username):
    #get request url
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username,ACCESS_TOKEN)
    #print the request url
    print "GET request url: %s" % (request_url)
    user_info = requests.get(request_url).json()

    #check if request status is OK or not
    if user_info["meta"]["code"] == 200:
        #check if user data exists
        if len(user_info["data"]):
            #print the userid
            return user_info["data"][0]["id"]
        else:
            return None
    else:
        #display invalid request
        print "INVALID REQUEST!!!Please try again"
        exit()



#function to retreive user information
def get_user_info(insta_username):
    #define user id
    user_id = get_user_id(insta_username)
    #check if there is userid or not
    if user_id == None:
        print "User doesn't exist!!!"
        exit()
    #define request url
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id,ACCESS_TOKEN)
    #print the request url
    print "GET request url: %s" % (request_url)
    user_info = requests.get(request_url).json()

    #check if request status is OK or not
    if user_info["meta"]["code"] == 200:
        #check if data exists for the user
        if len(user_info["data"]):
            #print the details of the user
            print "Username: %s" % (user_info["data"]["username"])
            print "Full Name: %s" % (user_info["data"]["full_name"])
            print "Bio: %s" % (user_info["data"]["bio"])
            print "Website: %s" % (user_info["data"]["website"])
            print "Number of followers: %s" % (user_info["data"]["counts"]["followed_by"])
            print "Number of post: %s" % (user_info["data"]["counts"]["media"])
            print "Number of people you are following: %s" % (user_info["data"]["counts"]["follows"])
        else:
            #display that no data is available for the user
            print "No data is available for this particular user!!!"
    else:
        #show invalid request message
        print "INVALID REQUEST!!!Please try again"



#function to start the project
def start_bot():
    #continue until the condition becomes false
    while True:
        #greeting the user
        print "\nHey! Welcome to InstaBot\n"
        #displaying the menu
        print "Menu:-\n"
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Exit\n"

        #accept user input
        choice=raw_input("Enter you choice: ")
        #if user chooses option (a)
        if choice=="a":
            #print the details of your own account
            self_info()
        #if user chooses option (b)
        elif choice=="b":
            #accept username from the user
            insta_username = raw_input("Enter the username of the user: ")
            #display the user details
            get_user_info(insta_username)
        #if user chooses option (c)
        elif choice=="c":
            #terminate the project processing
            exit()
        #if user chooses any other option
        else:
            #print the message that the choice is invalid
            print "INVALID CHOICE"



#calling the start_bot function
start_bot()