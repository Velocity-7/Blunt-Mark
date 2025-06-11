import datetime, hikari, lightbulb

plugin = lightbulb.Plugin('uptime')
record_time = datetime.datetime.utcnow()

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.command('uptime', 'Check the bot uptime')
@lightbulb.implements(lightbulb.SlashCommand)
async def uptime(ctx):
 current_time = datetime.datetime.utcnow()
 uptime = current_time - record_time
 days = uptime.days
 hours, remainder = divmod(uptime.seconds, 3600)
 minutes, seconds = divmod(remainder, 60)
 await ctx.respond(f'Bot has been online for: `{days}` days, `{hours}` hours, `{minutes}` minutes, `{seconds}` seconds.')

#Coded by Velocity7
