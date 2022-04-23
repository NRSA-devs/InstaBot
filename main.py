from time import sleep
import instaloader
import discord
from pytz import timezone
import datetime
from os import path
import sys
import ast

insta_username = ''
insta_password = ''
username = ''
MINS_TO_SLEEP = 40
discord_webhook_url = ''

def check_unfollowers(current,old):
    return list(set(old) - set(current))

def check_followers(current,old):
	return list(set(current) - set(old))



def start():
    #login to Instagram
    L = instaloader.Instaloader()
    L.login(insta_username, insta_password)

    while True:
        curr_time = datetime.datetime.now(timezone('Asia/Kolkata'))
        curr_time = curr_time.strftime("%b %d, %Y - %H:%M:%S")

        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, username)

        new_followers = []
        old_followers=[]


        for followee in profile.get_followers():
            new_followers.append(followee.username)

        if path.exists('followers.txt'):
            with open("followers.txt") as f:
                for i in f.readlines():
                    old_followers.append(i[:-1])


        if path.exists("followers.txt"):
            unfollowers = check_unfollowers(new_followers,old_followers)
            newfollowers = check_followers(new_followers,old_followers)
            discord.send_msg(username,unfollowers,newfollowers, curr_time,discord_webhook_url)

        with open("followers.txt", "w") as f:
            for x in new_followers:
                f.write(x)
                f.write("\n")      
        sleep(MINS_TO_SLEEP*60)


if __name__ == '__main__':
	if not path.exists('config_file.txt'):
		print("You have not configured your details yet.\nRun config.py first")
		sys.exit(0)

	f = open('config_file.txt','r')
	config = f.read()
	f.close()
	config = ast.literal_eval(config)
	insta_username = config['insta_username']
	insta_password = config['insta_password']
	username = config['username']
	discord_webhook_url = config['discord_webhook_url']

	start()