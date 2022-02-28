#Run this 'python -m pip install -U hikari'
#Run this 'pip install hikari-lightbulb'
import lightbulb

bot = lightbulb.BotApp(tokren='Your Bot Token',
    default_enabled_guilds=(YOUR_GUID_ID))
#This part is not required ^
    
@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')
#Basic Slash command ^    
    
@bot.command
@lightbulb.command("embed", "Sends an embed in the command channel")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="Like this bot?", description="[Click here to add this bot to your server](https://youtube.com)")
    embed.set_thumbnail("https://i.imgur.com/EpuEOXC.jpg")
    await ctx.respond(embed)    
#Embed ^
   
bot.run()

#Coded by Velocity7
