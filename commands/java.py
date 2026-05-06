import hikari, lightbulb

loader = lightbulb.Loader()

@loader.command
class Java(lightbulb.SlashCommand, name="java", description="Download Java"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title='Java', description='Click [**here**](https://www.java.com/download/) to start downloading :white_check_mark:', colour='#FFFFFF')
        embed.set_thumbnail('https://cdn.icon-icons.com/icons2/2415/PNG/512/java_original_wordmark_logo_icon_146459.png')
        await ctx.respond(embed)

#Coded by Velocity7