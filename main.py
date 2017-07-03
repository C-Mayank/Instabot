import requests

ACCESS_TOKEN = '5683656431.a4b1c44.182dcfe7f7124b2d9b873838cfa886bc'

BASE_URL = 'https://api.instagram.com/v1/'


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