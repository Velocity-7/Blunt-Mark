import hikari, lightbulb

plugin = lightbulb.Plugin('lc')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.command('lc', 'Download Lunar Client')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def lc_group(ctx):
 pass

@lc_group.child
@lightbulb.command('windows', 'Download the Windows version of Lunar Client')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def lc_windows(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='Lunar Client', description='Download Lunar Client for Windows', color='1B5B83')
 embed.add_field('Windows Version', 'Click [**here**](https://download.overwolf.com/installer/prod/3568b3a295e6576da49827711e489a4d/Lunar%20Client%20-%20Installer.exe) to start downloading :white_check_mark:')
 embed.set_thumbnail('https://cdn2.steamgriddb.com/file/sgdb-cdn/logo/681ebee67a5c1092f846f5c91c9851b2.png')
 await ctx.respond(embed) 

@lc_group.child
@lightbulb.command('macos', 'Download the macOS version of Lunar Client')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def lc_macos(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='Lunar Client', description='Download Lunar Client for macOS', color='1B5B83')
 embed.add_field('macOS Version', 'Click [**here**](https://launcherupdates.lunarclientcdn.com/Lunar%20Client%20v3.3.2-ow.dmg) to start downloading :white_check_mark:')
 embed.set_thumbnail('https://cdn2.steamgriddb.com/file/sgdb-cdn/logo/681ebee67a5c1092f846f5c91c9851b2.png')
 await ctx.respond(embed) 

@lc_group.child
@lightbulb.command('linux', 'Download the Linux version of Lunar Client')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def lc_linux(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='Lunar Client', description='Download Lunar Client for Linux', color='1B5B83')
 embed.add_field('Linux Version', 'Click [**here**](https://launcherupdates.lunarclientcdn.com/Lunar%20Client-3.3.2-ow.AppImage) to start downloading :white_check_mark:')
 embed.set_thumbnail('https://cdn2.steamgriddb.com/file/sgdb-cdn/logo/681ebee67a5c1092f846f5c91c9851b2.png')
 await ctx.respond(embed) 

#Coded by Velocity7