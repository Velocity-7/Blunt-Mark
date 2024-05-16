import hikari, lightbulb, miru

plugin = lightbulb.Plugin('modal_command')

def load(bot):
 bot.add_plugin(plugin)
 miru.install(bot)
#If you are creating more than one modal only include the ||miru.install(bot)|| section in one command as it will not work if it is loaded in more than once

class Modal_View(miru.View):
 @miru.button(label='Button_Label', style=hikari.ButtonStyle.SECONDARY)
 async def modal_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
  modal = Modal(title='Modal_Title')
  await ctx.respond_with_modal(modal)
#Creates the modal button ^

class Modal(miru.Modal):
 your_field_1 = miru.TextInput(label='Modal_Field_Name')
 async def callback(self, ctx: miru.ModalContext) -> None:
  await ctx.respond('Modal_Response')
#Creates the modal ^

@plugin.command
@lightbulb.command('modal_command_name', 'Modal_Command_Context')
@lightbulb.implements(lightbulb.SlashCommand)
async def test(ctx):
 view = Modal_View()
 message = await ctx.respond('Message_Response_with_Modal_Button', components=view)
 await view.start(message)
#Creates the command ^

#Coded by Velocity7