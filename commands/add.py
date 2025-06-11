import hikari, lightbulb

plugin = lightbulb.Plugin('add')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.option('num_2', 'Number 2',int)
@lightbulb.option('num_1', 'Number 1',int)
@lightbulb.option('num_4', 'Number 4 (optional)',int, default=None)
@lightbulb.option('num_3', 'Number 3 (optional)',int, default=None)
@lightbulb.command('add', "Add upto 4 numbers together")
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
 sum = ctx.options.num_1 + ctx.options.num_2
 if ctx.options.num_3 is not None:
  sum += ctx.options.num_3
 if ctx.options.num_4 is not None:
  sum+= ctx.options.num_4
 await ctx.respond(f'The sum of the numbers is {sum}.', flags=hikari.MessageFlag.EPHEMERAL)

#Coded by Velocity7