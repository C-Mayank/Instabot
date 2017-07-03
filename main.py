import requests

ACCESS_TOKEN = '5683656431.a4b1c44.182dcfe7f7124b2d9b873838cfa886bc'

BASE_URL = 'https://api.instagram.com/v1/'





def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
    print "GET request url: %s" % (request_url)
    user_info = requests.get(request_url).json()

    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]):
            print "Username: %s" %(user_info["data"]["username"])
            print "Full Name: %s" % (user_info["data"]["fullname"])
            print "Bio: %s" % (user_info["data"]["bio"])
            print "Website: %s" % (user_info["data"]["website"])
            print "Number of followers: %s" % (user_info["data"]["count"]["followed_by"])
            print "Number of post: s" % (user_info["data"]["count"]["media"])
            print "Number of people you are following: %s" % (user_info["data"]["count"]["follows"])
        else:
            print "User does not exist!!!"
    else:
        print "INVALID REQUEST!!!"
        print "Please check the request"



def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Exit"

        choice=raw_input("Enter you choice: ")
        if choice=="a":
            self_info()
        elif choice=="b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)

        elif choice=="c":
            exit()
        else:
            print "wrong choice"

start_bot()