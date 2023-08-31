import hikari, lightbulb

plugin = lightbulb.Plugin('embed')

def load (bot):
    bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
  print(event.content) 

@plugin.command
@lightbulb.command('Your_Command_Field', 'Your_Context_Field')
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title='Your_Title', description='Your_Description')
    embed.add_field('Your_Field_Name', 'Your_Field_Context')
    embed.set_thumbnail("https:https://example.com/")
    embed.set_footer('Your_Footer')
    await ctx.respond(embed)

#Coded by Velocity7