import hikari, lightbulb, os, sys, commands
from  dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

load_dotenv()

class NotOwner(Exception):
    pass

bot = hikari.GatewayBot(
    token=os.environ.get('TOKEN')
)
client = lightbulb.client_from_app(
    bot,
    default_enabled_guilds=(1040951775743713350, 1497603126981693510)
)

@bot.listen(hikari.StartingEvent)
async def on_starting(event: hikari.StartingEvent) -> None:
 await client.load_extensions_from_package(commands)

@bot.listen(hikari.StartedEvent)
async def start(event: hikari.StartedEvent):
    await client.start()
    await bot.update_presence(status=hikari.Status.IDLE, activity=hikari.Activity(name='Using Stable Firmware V4.7', type=hikari.ActivityType.CUSTOM))

@client.error_handler
async def errorhandler(exc: lightbulb.exceptions.ExecutionPipelineFailedException) -> bool:
    exception = exc.__cause__ or exc
    if isinstance(exception, NotOwner):
        await exc.context.respond('You must be the owner of this guild to use this! **If you believe this is a mistake please report to defnot.velocity on discord!**', flags=hikari.MessageFlag.EPHEMERAL)
        return True
        
    await exc.context.respond(f':warning: **Something went wrong trying to execute the command.** :warning:', flags=hikari.MessageFlag.EPHEMERAL)
    return False

bot.run()

#Coded by Velocity7