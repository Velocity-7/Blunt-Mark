import hikari, lightbulb

loader = lightbulb.Loader()

footer_icon_url = 'https://cdn.discordapp.com/attachments/971651606204522506/1177929748060590101/Blue_Loading.gif?ex=65744b90&is=6561d690&hm=12ea445896f3a5ab6089db3945f4c0e503e1386a67964ddae5513d6e3176ee6c&'
footer_icon_url_2 = 'https://cdn.discordapp.com/emojis/746443446331375646.gif?size=48&name=redloading&quality=lossless'

@loader.command
class Version(lightbulb.SlashCommand, name="version", description="Check the bot version"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        embed = hikari.Embed(title='Version', colour='00FFFF')
        embed.add_field('Currently running firmware', '╰-------------------------> `Beta V4.7`')
        embed.set_thumbnail('https://cdn.discordapp.com/attachments/971651606204522506/1129751247776387152/Blunt_Mark-1_1.png')
        embed.set_footer(text='‎', icon=footer_icon_url_2)
        await ctx.respond(embed)

#Coded by Velocity7