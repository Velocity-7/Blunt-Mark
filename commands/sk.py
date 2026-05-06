import hikari, lightbulb

loader = lightbulb.Loader()
group = lightbulb.Group("sk", "Download SK Launcher")
loader.command(group)

@group.register
class SkUniversal(lightbulb.SlashCommand, name="universal", description="Download the universal (macOS+Linux+Windows) version of SK Launcher"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title='SK Launcher', description='Download the universal version of SK Launcher', colour='8E3986')
        embed.add_field('Universal (**macOS+Linux+Windows**) Version', 'Click [**here**](https://skmedix.pl/binaries/skl/3.2.10/SKlauncher-3.2.10.jar) to start downloading :white_check_mark:')
        embed.set_thumbnail('https://skmedix.pl/images/logo.png')
        await ctx.respond(embed)

@group.register
class SkWindows(lightbulb.SlashCommand, name="windows", description="Download the windows version of SK Launcher"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title='SK Launcher', description='Download the Windows version of SK Launcher', colour='8E3986')
        embed.add_field('Windows Version', 'Click [**here**](https://skmedix.pl/binaries/skl/3.2.10/x64/SKlauncher-3.2.10.exe) to start downloading :white_check_mark:')
        embed.set_thumbnail('https://skmedix.pl/images/logo.png')
        await ctx.respond(embed)

#Coded by Velocity7