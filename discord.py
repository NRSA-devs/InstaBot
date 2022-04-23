from discord_webhook import DiscordWebhook, DiscordEmbed



def send_msg(username,unfollowers,newfollowers, time, webhook_url):

    # print("In the discord")
    newfollowers_content=''
    unfollowers_content=''
    
    if newfollowers == [] and unfollowers == []:
        print("No change in followers, so not sending message to discord")
        return

    if newfollowers == []:
        newfollowers_content = 'None'

    if unfollowers == []:
        unfollowers_content = 'None'
    
    for x in newfollowers:
        newfollowers_content=newfollowers_content+x+'\n'
    for x in unfollowers:
        unfollowers_content=unfollowers_content+x+'\n'
    
    webhook = DiscordWebhook(url= webhook_url)
    embed = DiscordEmbed(title=':notebook: Report for %s' %(username), description='%s' %(time))
    
    embed.add_embed_field(name='People who followed you', value=newfollowers_content ,inline=False)
    embed.add_embed_field(name='People who unfollowed you', value=unfollowers_content)

    # Attaches a footer
    embed.set_footer(text='--Tony Stark')
    webhook.add_embed(embed)
    response = webhook.execute()

    print("Sent message to discord")



