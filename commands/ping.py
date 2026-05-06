import hikari, lightbulb

loader = lightbulb.Loader()

@loader.command
class Ping(lightbulb.SlashCommand, name="ping", description="Command to test if the bot is online"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.respond('https://cdn.discordapp.com/emojis/657823874003763201.gif?size=48&name=yes&quality=lossless')

#Coded by Velocity7