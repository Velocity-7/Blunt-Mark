#Run this 'python -m pip install -U hikari'
#Run this 'pip install hikari-lightbulb'
import hikari
import lightbulb

bot = lightbulb.BotApp(token='YOUR_BOT_TOKEN',
#Required ^                       
    default_enabled_guilds=(YOUR_GUILD_ID))
#This part is not required ^ (Only use for faster command loading in specific Guilds)
    
@bot.command
@lightbulb.command('ping', 'Your_Context_Field')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')
#Basic Slash command ^    
    
@bot.command
@lightbulb.command("embed", "Your_Context_Field")
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title="Your_Title", description="Your_Description")
    embed.add_field("Your_Field_Name", "Your_Field_Context")
    embed.set_thumbnail("https:https://example.com/")
    embed.set_footer("Your_Footer")
    await ctx.respond(embed)    
#Embed ^
   
bot.run()

#Coded by Velocity7
