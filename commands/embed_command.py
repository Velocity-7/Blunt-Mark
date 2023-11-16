import hikari, lightbulb

plugin = lightbulb.Plugin('embed_command')

def load (bot):
    bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
  print(event.content) 

@plugin.command
@lightbulb.command('your_embed_command_name_field', 'Your_Embed_Command_Context_Field')
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command_name(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title='Your_Title', description='Your_Description')
    embed.add_field('Your_Field_Name', 'Your_Field_Context')
    embed.set_thumbnail('https://example.com/')
    embed.set_footer('Your_Footer')
    await ctx.respond(embed)
#Creates the embed ^

#Coded by Velocity7
