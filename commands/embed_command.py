import hikari, lightbulb

plugin = lightbulb.Plugin('embed_command')

def load (bot):
 bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
 print(event.content) 
#Helpful for debugging ^ 

@plugin.command
@lightbulb.command('embed_command_name', 'Embed_Command_Context')
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command_name(ctx: lightbulb.Context) -> None:
 embed = hikari.Embed(title='Embed_Title', description='Embed_Description')
 embed.add_field('Embed_Field_Name', 'Embed_Field_Context')
 embed.set_thumbnail('https://example.com/')
 embed.set_footer('Embed_Footer')
 await ctx.respond(embed)
#Creates the embed ^

#Coded by Velocity7