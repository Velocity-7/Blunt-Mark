import datetime, hikari, lightbulb

record_time = datetime.datetime.utcnow()
loader = lightbulb.Loader()

@loader.command
class Uptime(lightbulb.SlashCommand, name="uptime", description="Check the bot uptime"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        current_time = datetime.datetime.utcnow()
        uptime = current_time - record_time
        days = uptime.days
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        await ctx.respond(f'Bot has been online for: `{days}` days, `{hours}` hours, `{minutes}` minutes, `{seconds}` seconds.')

#Coded by Velocity7
