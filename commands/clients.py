import hikari, lightbulb

plugin = lightbulb.Plugin('clients')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.add_cooldown(60, 1, lightbulb.UserBucket)
@lightbulb.command('clients', 'Download minecraft clients')
@lightbulb.implements(lightbulb.SlashCommand)
async def clients(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='Clients', description='Download Minecraft Clients', colour='00FFFF')
 embed.add_field('SK Launcher (Cracked and Premium)', 'Use **/sk**')
 embed.add_field('Lunar Client (Premium Only)', 'Use **/lc**')
 embed.add_field('Badlion Client (Premium Only)', 'Use **/blc**')
 embed.add_field('Feather Client (Premium Only)', 'Use **/feather_client**')
 embed.set_thumbnail('https://cdn.discordapp.com/attachments/971651606204522506/1129751247776387152/Blunt_Mark-1_1.png')
 await ctx.respond(embed)

#Coded by Velocity7