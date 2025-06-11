import hikari, lightbulb

plugin = lightbulb.Plugin('about')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.command('about', 'Learn about our policies')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def about_group(ctx):
 pass

@about_group.child
@lightbulb.command('downloads', 'About our downloads policy')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def about_downloads(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='About', colour='00FFFF')
 embed.add_field('Downloads policiy', 'All of our downloads using the `Blunt Mark Bot` which have :white_check_mark: are from direct and **OFFICIAL** links so you can have a safe experience')
 embed.set_thumbnail('https://cdn.discordapp.com/attachments/971651606204522506/1129751247776387152/Blunt_Mark-1_1.png')
 await ctx.respond(embed)

@about_group.child
@lightbulb.command('bot', 'About our bot firmware policy')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def about_bot(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='About', colour='00FFFF')
 embed.add_field('Bot firmware policy', 
 'The bot runs on 2 types of firmware either \n1. Stable channel  which is represented by :blue_circle: \n2. Beta channel which is represented by :red_circle: \n\nIf the bot status is on `Do Not Disturb` mode it means the bot is running :red_circle: and if the bot status is on `Idle` mode it means the bot is running :blue_circle:')
 embed.set_thumbnail('https://cdn.discordapp.com/attachments/971651606204522506/1129751247776387152/Blunt_Mark-1_1.png')
 await ctx.respond(embed)

#Coded by Velocity7