#Run 'python -m pip install -U hikari' before you start
#Run 'pip install hikari-lightbulb' before you start

import hikari
import lightbulb

bot = lightbulb.BotApp(token='YOUR_BOT_TOKEN',
#Required ^                    
    default_enabled_guilds=(YOUR_GUILD_ID))
#Too add more than one guild use: (YOUR_GUILD_ID, ANOTHER_GUILD_ID) (Used for loading commands faster in guilds) 
    
@bot.command
@lightbulb.command('your_command_name', 'your_command_description')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Your_Command_Response')
#Basic Slash command ^   
    
@bot.command
@lightbulb.command('your_command_name_2', 'your_command_description_2')
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title='Your_Embed_Title', description='Your_Embed_Description')
    embed.add_field('Your_Embed_Field_Name', 'Your_Embed_Field_Description')
    embed.set_thumbnail("https://example.com/")
    embed.set_footer('Your_Embed_Footer')
    await ctx.respond(embed)    
#Embed Slash Command ^

#Group Start
@bot.command
@lightbulb.command('your_group_command_name', 'your_group_command_description')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def your_group_name(ctx):
  pass

@your_group_name.child
@lightbulb.command('your_sub_command_name', 'your_sub_command_description')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title='Your_Embed_Title', description='Your_Embed_Description')
    embed.add_field('Your_Embed_Field_Name', 'Your_Embed_Field_Description')
    embed.set_thumbnail("https:https://example.com/")
    embed.set_footer('Your_Embed_Footer')
    await ctx.respond(embed)

@your_group_name.child
@lightbulb.command('your_sub_command_name_2', 'your_sub_command_description_2')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ping(ctx):
    await ctx.respond('Your_Command_Response')
#Group End
    
bot.run()

#Coded by Velocity7