from logging import warning
from os import path
import sys
import getpass

warning = "Make sure you use a temporary bot account with this script,and not your original account.\nThe temporary account will retrieve the followers of your original account.\nMultiple logins can lead to account ban."

if path.exists('config_file.txt'):
    inp = input('The config file already exists, do you want to overwrite it? (Y/N)')
    inp = inp.upper()
    if inp == 'N':
        sys.exit(0)


print(f"NOTE :\n{warning}")
print("-"*100+"\n")

insta_username = input("InstaBot account Username : ")
insta_password = getpass.getpass()

username = input("Enter username of your original account (whose followers you want to monitor) : ")
discord_webhook_url = input("Enter your discord webhook URL : ")


if not "discordapp.com" in discord_webhook_url:
	discord_webhook_url = discord_webhook_url.replace("discord.com","discordapp.com")

f = open("config_file.txt","w")
f.write(str({"insta_username":insta_username,"insta_password":insta_password,"username":username,"discord_webhook_url":discord_webhook_url}))
f.close()
print("Configured successfully!")

