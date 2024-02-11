import hikari, lightbulb

plugin = lightbulb.Plugin('clear_command')

def load(bot):
 bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
 print(event.content)

@plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option('lines', 'Number of lines you want to delete',int)
@lightbulb.command('clear', 'Clear messages')
@lightbulb.implements(lightbulb.SlashCommand)
async def clear_command(ctx):
 lines = int(ctx.options.lines)
 channel = str(ctx.channel_id)
 msgs = await ctx.bot.rest.fetch_messages(channel).limit(lines)
 await ctx.bot.rest.delete_messages(channel, msgs)
#Creates the command ^

#Coded by Velocity7
