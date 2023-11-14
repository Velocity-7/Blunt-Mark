import hikari, lightbulb

plugin = lightbulb.Plugin('slash_command')

def load(bot):
  bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
  print(event.content)

@plugin.command
@lightbulb.command('your_command_name_field', 'Your_Command_Context_Field')
@lightbulb.implements(lightbulb.SlashCommand)
async def your_slash_command_name(ctx):
    await ctx.respond('Your_Command_Response')
#Creates the command ^

#Coded by Velocity7