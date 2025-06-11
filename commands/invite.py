import hikari, lightbulb

plugin = lightbulb.Plugin('invite')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.command('invite', 'Link to invite this bot to your server')
@lightbulb.implements(lightbulb.SlashCommand)
async def invite(ctx):
 await ctx.respond('Click [**here**](https://discord.com/oauth2/authorize?client_id=1113864828424036482&scope=bot&permissions=8192) :link: to invite this bot to your server')

#Coded by Velocity7