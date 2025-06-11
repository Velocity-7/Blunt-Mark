import hikari, lightbulb

plugin = lightbulb.Plugin('help')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.command('help', 'Get information on all bot commands')
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='Commands', colour='00FFFF')
 embed.add_field('**/about**', "Learn about our policies")
 embed.add_field('**/add**', 'Used to add upto 4 numbers together.')
 embed.add_field('**/clear***', 'Used to delete messages.')
 embed.add_field('**/help***', 'Used to trigger this command.')
 embed.add_field('**/clients**', 'Gives a list of all downloadable clients using the bot.')
 embed.add_field('**/invite**', 'Used to invite the bot to your server.')
 embed.add_field('**/java**', 'Used to download Java using the bot.')
 embed.add_field('**/mail**', 'Gives the official e-mail address to contact support.')
 embed.add_field('**/ping**', 'Used to check if the bot is online.')
 embed.add_field('**/server_status**', 'Used to check the minecraft server status')
 embed.add_field('**/uptime**', 'Check the bot uptime.')
 embed.add_field('**/version**', 'Used to check the bot version.')
 embed.set_footer('* Indicates Bot Owner Only Command')
 embed.set_thumbnail('https://cdn.discordapp.com/attachments/971651606204522506/1129751247776387152/Blunt_Mark-1_1.png')
 await ctx.respond(embed, flags=hikari.MessageFlag.EPHEMERAL)

#Coded by Velocity7