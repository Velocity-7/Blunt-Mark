import hikari, lightbulb

plugin = lightbulb.Plugin('group_command')

def load (bot):
    bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
  print(event.content) 

@plugin.command
@lightbulb.command('your_group_name_field', 'Your_Group_Context_Field')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def your_group_name(ctx):
  pass
#Creates the parent group ^

@your_group_name.child
@lightbulb.command('your_sub_command_name_field_1', 'Your_Sub_Command_Context_Field')
@lightbulb.implements(lightbulb.SlashSubCommand)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def your_sub_command_name_2(ctx):
    await ctx.respond('Your_Response_2')
#Creates the child sub-command ^

@your_group_name.child
@lightbulb.command('your_sub_command_name_field_2', 'Your_Sub_Command_Context_Field')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def your_sub_command_name_2(ctx):
    await ctx.respond('Your_Response')
#Creates the child sub-command ^

#Coded by Velocity7
