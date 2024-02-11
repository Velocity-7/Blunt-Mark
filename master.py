#Run 'python -m pip install -U hikari' before you start
#Run 'pip install hikari-lightbulb' before you start
#Run 'python -m pip install -U hikari-miru==3.4.0' before you start

import hikari, lightbulb

bot = lightbulb.BotApp(token='YOUR_BOT_TOKEN', default_enabled_guilds=(YOUR_GUILD_ID))
#Required ^                    
#Too add more than one guild use: (YOUR_GUILD_ID, ANOTHER_GUILD_ID) | (Used for loading commands faster in guilds)

@bot.listen(hikari.StartedEvent)
async def start(event):
 await bot.update_presence(status=hikari.Status.ONLINE)
#Changes the bot status ||DO_NOT_DISTURB, IDLE, ONLINE|| ^

bot.load_extensions_from('./commands')
#Loads Commands ^
    
bot.run()

#Coded by Velocity7
