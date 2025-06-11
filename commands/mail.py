import hikari, lightbulb

plugin = lightbulb.Plugin('mail')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.command('mail', 'Get our support email address')
@lightbulb.implements(lightbulb.SlashCommand)
async def mail(ctx):
 await ctx.respond('**Contact us for support at** `help.bluntmark@gmail.com`')

#Coded by Velocity7