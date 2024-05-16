import hikari, lightbulb

plugin = lightbulb.Plugin('group_command')

def load (bot):
 bot.add_plugin(plugin)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def message(event):
 print(event.content) 
#Helpful for debugging ^ 

@plugin.command
@lightbulb.command('group_command_name', 'Group_Command_Context')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def your_group_name(ctx):
 pass
#Creates the parent group ^

@your_group_name.child
@lightbulb.command('sub_command_1_name', 'Sub_Command_1_Context')
@lightbulb.implements(lightbulb.SlashSubCommand)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def your_sub_command_name_2(ctx):
 await ctx.respond('Sub_Command_1_Response')
#Creates the group child command ^

@your_group_name.child
@lightbulb.command('sub_command_2_name', 'Sub_Command_2_Context')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def your_sub_command_name_2(ctx):
 await ctx.respond('Sub_Command_2_Response')
#Creates the group child command ^

#Coded by Velocity7