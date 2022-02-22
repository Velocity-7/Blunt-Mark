#Run this 'python -m pip install -U hikari'
#Run this 'pip install hikari-lightbulb'
import lightbulb

bot = lightbulb.BotApp( token='Your Bot Token',
    default_enabled_guilds=(YOUR_GUID_ID))
    #This part is not required ^
    
@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@bot.command
@lightbulb.command('ping', 'ping command')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
  await ctx.respond('pong!')

@bot.command
@lightbulb.option('num1','First number',type=int)
@lightbulb.option('num2','Second number',type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
  await ctx.respond(ctx.options.num1 + ctx.options.num2)

bot.run()
