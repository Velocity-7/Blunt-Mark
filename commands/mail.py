import hikari, lightbulb

loader = lightbulb.Loader()

@loader.command
class Mail(lightbulb.SlashCommand, name="mail", description="Get our support email address"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.respond('**Contact us for support at** `help.bluntmark@gmail.com`')

#Coded by Velocity7