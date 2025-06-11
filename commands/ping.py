import hikari, lightbulb

plugin = lightbulb.Plugin('ping')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.add_cooldown(30, 1, lightbulb.UserBucket)
@lightbulb.command('ping', 'Command to test if the bot is online')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
 await ctx.respond('https://cdn.discordapp.com/emojis/657823874003763201.gif?size=48&name=yes&quality=lossless')

#Coded by Velocity7