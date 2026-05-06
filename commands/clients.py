import hikari, lightbulb

loader = lightbulb.Loader()

@loader.command
class Clients(lightbulb.SlashCommand, name="clients", description="Download minecraft clients"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title='Clients', description='Download Minecraft Clients', colour='00FFFF')
        embed.add_field('SK Launcher (Cracked and Premium)', 'Use **/sk**')
        embed.add_field('Lunar Client (Premium Only)', 'Use **/lc**')
        embed.set_thumbnail('https://cdn.discordapp.com/attachments/971651606204522506/1129751247776387152/Blunt_Mark-1_1.png')
        await ctx.respond(embed)

#Coded by Velocity7