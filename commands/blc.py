import hikari, lightbulb

loader = lightbulb.Loader()
group = lightbulb.Group("blc", "Download Badlion Client")
loader.command(group)

@group.register
class BlcWindows(lightbulb.SlashCommand, name="windows", description="Download Badlion Client for Windows"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title='Badlion Client', description='Download Badlion Client for Windows', colour='D4AF37')
        embed.add_field('Windows Version', 'Click [**here**](https://www.badlion.net/download/client/latest/windows) to start downloading :white_check_mark:')
        embed.set_thumbnail('https://assets.badlion.net/site/assets/badlion-logo.png')
        await ctx.respond(embed)

@group.register
class BlcMacos(lightbulb.SlashCommand, name="macos", description="Download Badlion Client for macOS"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title='Badlion Client', description='Download Badlion Client for macOS', colour='D4AF37')
        embed.add_field('macOS Version', 'Click [**here**](https://www.badlion.net/download/client/latest/mac) to start downloading :white_check_mark:')
        embed.set_thumbnail('https://assets.badlion.net/site/assets/badlion-logo.png')
        await ctx.respond(embed)

@group.register
class BlcLinux(lightbulb.SlashCommand, name="linux", description="Download Badlion Client for Linux"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title='Badlion Client', description='Download Badlion Client for Linux', colour='D4AF37')
        embed.add_field('Linux Version', 'Click [**here**](https://www.badlion.net/download/client/latest/linux) to start downloading :white_check_mark:')
        embed.set_thumbnail('https://assets.badlion.net/site/assets/badlion-logo.png')
        await ctx.respond(embed)

#Coded by Velocity7