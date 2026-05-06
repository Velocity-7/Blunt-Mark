import hikari, lightbulb

loader = lightbulb.Loader()
group = lightbulb.Group("lc", "Download Lunar Client")
loader.command(group)

@group.register
class LcWindows(lightbulb.SlashCommand, name="windows", description="Download the Windows version of Lunar Client"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title='Lunar Client', description='Download Lunar Client for Windows', color='1B5B83')
        embed.add_field('Windows Version', 'Click [**here**](https://download.overwolf.com/installer/prod/1604c92c8d0fb100fb2d34275ea7be21/Lunar%20Client%20-%20Installer.exe) to start downloading :white_check_mark:')
        embed.set_thumbnail('https://cdn2.steamgriddb.com/file/sgdb-cdn/logo/681ebee67a5c1092f846f5c91c9851b2.png')
        await ctx.respond(embed) 

@group.register
class LcMacos(lightbulb.SlashCommand, name="macos", description="Download the macOS version of Lunar Client"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title='Lunar Client', description='Download Lunar Client for macOS', color='1B5B83')
        embed.add_field('macOS Version', 'Click [**here**](https://launcherupdates.lunarclientcdn.com/Lunar%20Client%20v3.6.9-ow.dmg) to start downloading :white_check_mark:')
        embed.set_thumbnail('https://cdn2.steamgriddb.com/file/sgdb-cdn/logo/681ebee67a5c1092f846f5c91c9851b2.png')
        await ctx.respond(embed) 

@group.register
class LcLinux(lightbulb.SlashCommand, name="linux", description="Download the Linux version of Lunar Client"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title='Lunar Client', description='Download Lunar Client for Linux', color='1B5B83')
        embed.add_field('Linux Version', 'Click [**here**](https://launcherupdates.lunarclientcdn.com/Lunar%20Client-3.6.9-ow.AppImage) to start downloading :white_check_mark:')
        embed.set_thumbnail('https://cdn2.steamgriddb.com/file/sgdb-cdn/logo/681ebee67a5c1092f846f5c91c9851b2.png')
        await ctx.respond(embed) 

#Coded by Velocity7