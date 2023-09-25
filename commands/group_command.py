import hikari, lightbulb

plugin = lightbulb.Plugin('group_command')

def load (bot):
    bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
  print(event.content) 

@plugin.command
@lightbulb.command('your_group_command_field', 'Your_Group_Command_Context_Field')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def your_group_name(ctx):
  pass
#Creates the parent group ^

@your_group_name.child
@lightbulb.command('your_sub_command_field', 'Your_Sub_Command_Context_Field')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def embed_command(ctx: lightbulb.Context) -> None:
    embed = hikari.Embed(title='Your_Title', description='Your_Description')
    embed.add_field('Your_Field_Name', 'Your_Field_Context')
    embed.set_thumbnail("https:https://example.com/")
    embed.set_footer('Your_Footer')
    await ctx.respond(embed)
#Creates the child sub-command ^

@your_group_name.child
@lightbulb.command('your_sub_command_field', 'Your_Sub_Command_Context_Field')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def ping(ctx):
    await ctx.respond('Your_Response')
#Creates the child sub-command ^

#Coded by Velocity7