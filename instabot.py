#importing 'requests' and 'urllib' packages
import requests,urllib

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
        #display invalid request
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



#function to get your recent posts
def get_own_post():
    #get request url
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)

    #print the request url
    print "GET request url: %s" % (request_url)

    #define own media
    own_media = requests.get(request_url).json()

    #check if request is valid
    if own_media["meta"]["code"] == 200:
        #check if own_media has data
        if len(own_media["data"]):
            #define name of the image
            image_name = own_media["data"][0]["id"] + ".jpeg"
            #define url of the image
            image_url = own_media["data"][0]["images"]["standard_resolution"]["url"]
            #retreive the image post
            urllib.urlretrieve(image_url,image_name)
            #print an appropriate message
            print "Your image has been downloaded!!!"
        else:
            print "Post does not exist!"
    else:
        print "INVALID REQUEST!!!!Please try again"



#function to get an user's most recent post
def get_users_post(insta_username):
    #retrieve an user id
    user_id = get_user_id(insta_username)

    #check if userid is none
    if user_id == None:
        #print the user does not exist
        print "User does not exist!!!"
        exit()

    #define request url
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id,ACCESS_TOKEN)

    #display request url
    print "GET request url: %s" % (request_url)

    #define a variable for media
    user_media = requests.get(request_url).json()

    #check if request is valid
    if user_media["meta"]["code"] == 200:
        #check if user_media has data
        if len(user_media["data"]):
            #define the name for the image
            image_name= user_media["data"][0]["id"] + ".jpeg"
            #define the url for the image
            image_url = user_media["data"][0]["images"]["standard_resolution"]["url"]
            #retrieve the image
            urllib.urlretrieve(image_url, image_name)
            #print a suitable message
            print "The image has been downloaded!!!"
        else:
            print "No recent posts!!!"
    else:
        print "INVALID REQUEST"



#function to start the project
def start_bot():
    #continue until the condition becomes false
    while True:
        #greeting the user
        print "\nHey! Welcome to InstaBot\n"

        #displaying the menu
        print "Menu:-\n"
        print "a. Retrieve your own details\n"
        print "b. Retrieve details of a user\n"
        print "c. Retrieve your own recent posts\n"
        print "d. Retrieve the recent post of an user\n"
        print "e. Exit\n"

        #accept user input
        choice = raw_input("Enter you choice: ")

        #if user chooses option (a)
        if choice == "a":
            #print the details of your own account
            self_info()
        #if user chooses option (b)
        elif choice == "b":
            #accept username from the user
            insta_username = raw_input("Enter the username of the user: ")
            #display the user details
            get_user_info(insta_username)
        #if user chooses option (c)
        elif choice =="c":
            #retrieve your recent post
            get_own_post()
        #if user chooses option (d)
        elif choice == "d":
            #accept username from the user
            insta_username = raw_input("Enter the username of the user: ")
            #retrieve the most recent post of another user
            get_users_post(insta_username)
        #if user chooses option (c)
        elif choice == "e":
            #terminate the project processing
            exit()
        #if user chooses any other option
        else:
            #print the message that the choice is invalid
            print "INVALID CHOICE"



#starting the processing
start_bot()