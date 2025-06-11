import hikari, lightbulb

bot = lightbulb.BotApp(
 token=
 'BOT_TOKEN',
 default_enabled_guilds=(1040951775743713350, 967927221035606058, 915817248818593813, 1177278653575462923))

bot.load_extensions_from('./commands')

@bot.listen(hikari.StartedEvent)
async def start(event):
 await bot.update_presence(status=hikari.Status.DO_NOT_DISTURB, activity=hikari.Activity(name='Using Beta Firmware V4.7', type=hikari.ActivityType.CUSTOM))

@bot.listen(lightbulb.CommandErrorEvent)
async def errorhandler(event: lightbulb.CommandErrorEvent) -> None:

 exception = event.exception
 
 if isinstance(event.exception, lightbulb.CommandInvocationError):
  await event.context.respond(f':warning: **Something went wrong trying to execute the `{event.context.command.name}` command.** :warning:', flags=hikari.MessageFlag.EPHEMERAL)
  raise exception
 if isinstance(exception, lightbulb.NotOwner):
  await event.context.respond('You must be the owner of this guild to use this! **If you believe this is a mistake please report to velocity7. on discord!**', flags=hikari.MessageFlag.EPHEMERAL)
 if isinstance(exception, lightbulb.CommandIsOnCooldown):
  m, s = divmod(exception.retry_after, 60)
  h, m = divmod(m, 60)
  await event.context.respond(f'Use this command after `{s:.2f}` seconds', flags=hikari.MessageFlag.EPHEMERAL)
 else:
  raise exception

bot.run()

#Coded by Velocity7