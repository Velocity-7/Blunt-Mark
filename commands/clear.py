import hikari, lightbulb

plugin = lightbulb.Plugin('clear')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option('lines', 'Number of lines you want to delete',int)
@lightbulb.command('clear', 'Clear messages')
@lightbulb.implements(lightbulb.SlashCommand)
async def clear(ctx):
 lines = int(ctx.options.lines)
 channel = str(ctx.channel_id)
 msgs = await ctx.bot.rest.fetch_messages(channel).limit(lines)
 await ctx.bot.rest.delete_messages(channel, msgs)
 await ctx.respond(f'Deleted {lines} lines.',  flags=hikari.MessageFlag.EPHEMERAL)

#Coded by Velocity7