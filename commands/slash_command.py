import hikari, lightbulb

plugin = lightbulb.Plugin('slash_command')

def load(bot):
  bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
  print(event.content)

@plugin.command
@lightbulb.command('your_command_name', 'Your_Command_Description')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Your_Command_Response')
#Creates the command ^

#Coded by Velocity7