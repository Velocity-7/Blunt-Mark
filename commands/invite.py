import hikari, lightbulb

loader = lightbulb.Loader()

@loader.command
class Invite(lightbulb.SlashCommand, name="invite", description="Link to invite this bot to your server"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.respond('Click [**here**](https://discord.com/oauth2/authorize?client_id=1113864828424036482&scope=bot&permissions=8192) :link: to invite this bot to your server')

#Coded by Velocity7