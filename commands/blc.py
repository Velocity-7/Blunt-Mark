import hikari, lightbulb

plugin = lightbulb.Plugin('blc')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.command('blc', 'Download Badlion Client')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def blc_group(ctx):
 pass

@blc_group.child
@lightbulb.command('windows', 'Download Badlion Client for Windows')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def blc_windows(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='Badlion Client', description='Download Badlion Client for Windows', colour='D4AF37')
 embed.add_field('Windows Version', 'Click [**here**](https://www.badlion.net/download/client/latest/windows) to start downloading :white_check_mark:')
 embed.set_thumbnail('https://assets.badlion.net/site/assets/badlion-logo.png')
 await ctx.respond(embed)

@blc_group.child
@lightbulb.command('macos', 'Download Badlion Client for macOS')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def blc_macos(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='Badlion Client', description='Download Badlion Client for macOS', colour='D4AF37')
 embed.add_field('macOS Version', 'Click [**here**](https://www.badlion.net/download/client/latest/mac) to start downloading :white_check_mark:')
 embed.set_thumbnail('https://assets.badlion.net/site/assets/badlion-logo.png')
 await ctx.respond(embed)

@blc_group.child
@lightbulb.command('linux', 'Download Badlion Client for Linux')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def blc_linux(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='Badlion Client', description='Download Badlion Client for Linux', colour='D4AF37')
 embed.add_field('Linux Version', 'Click [**here**](https://www.badlion.net/download/client/latest/linux) to start downloading :white_check_mark:')
 embed.set_thumbnail('https://assets.badlion.net/site/assets/badlion-logo.png')
 await ctx.respond(embed)

#Coded by Velocity7