import hikari, lightbulb

plugin = lightbulb.Plugin('basic_slash_command')

def load(bot):
  bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
  print(event.content)

@plugin.command
@lightbulb.command('your_command_name', 'your_command_description')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Your_Command_Response')

#Coded by Velocity7
