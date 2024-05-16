import hikari, lightbulb

plugin = lightbulb.Plugin('ping_command')

def load(bot):
 bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
 print(event.content)
#Helpful for debugging ^  

@plugin.command
@lightbulb.command('ping_command', 'Ping_Command')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping_command(ctx):
 await ctx.respond('Pong!')
#Creates the command ^

#Coded by Velocity7