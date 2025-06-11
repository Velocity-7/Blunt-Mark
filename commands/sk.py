import hikari, lightbulb

plugin = lightbulb.Plugin('sk')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.command('sk', 'Download SK Launcher')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def sk_group(ctx):
 pass

@sk_group.child
@lightbulb.command('universal', 'Download the universal (macOS+Linux+Windows) version of SK Launcher')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def sk_universal(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='SK Launcher', description='Download the universal version of SK Launcher', colour='8E3986')
 embed.add_field('Universal (**macOS+Linux+Windows**) Version', 'Click [**here**](https://skmedix.pl/binaries/skl/3.2.10/SKlauncher-3.2.10.jar) to start downloading :white_check_mark:')
 embed.set_thumbnail('https://skmedix.pl/images/logo.png')
 await ctx.respond(embed)

@sk_group.child
@lightbulb.command('windows', 'Download the windows version of SK Launcher')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def sk_windows(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='SK Launcher', description='Download the Windows version of SK Launcher', colour='8E3986')
 embed.add_field('Windows Version', 'Click [**here**](https://skmedix.pl/binaries/skl/3.2.10/x64/SKlauncher-3.2.10.exe) to start downloading :white_check_mark:')
 embed.set_thumbnail('https://skmedix.pl/images/logo.png')
 await ctx.respond(embed)

#Coded by Velocity7