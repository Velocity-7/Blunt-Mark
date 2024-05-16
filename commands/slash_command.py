import hikari, lightbulb

plugin = lightbulb.Plugin('slash_command')

def load(bot):
 bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
 print(event.content)
#Helpful for debugging ^ 

@plugin.command
@lightbulb.command('slash_command_name', 'Slash_Command_Context')
@lightbulb.implements(lightbulb.SlashCommand)
async def your_slash_command_name(ctx):
 await ctx.respond('Slash_Command_Response')
#Creates the command ^

#Coded by Velocity7