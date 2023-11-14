import hikari, lightbulb, miru

plugin = lightbulb.Plugin('modal_command')

def load(bot):
    bot.add_plugin(plugin)
    miru.install(bot)
#If you are creating more than one modal only include the ||miru.install(bot)|| section in one command as it will not work if it is loaded in more than once

class Modal_View(miru.View):
    @miru.button(label='Your_Button_Label', style=hikari.ButtonStyle.SECONDARY)
    async def modal_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        modal = Modal(title='Your_Modal_Title')
        await ctx.respond_with_modal(modal)
#Creates the Modal Button ^

class Modal(miru.Modal):
    your_field_1 = miru.TextInput(label='Your_Field_Label')
    async def callback(self, ctx: miru.ModalContext) -> None:
        await ctx.respond('Your_Response')
#Creates the Modal ^


@plugin.command
@lightbulb.command('your_modal_name_field', 'Your_Modal_Context_Field')
@lightbulb.implements(lightbulb.SlashCommand)
async def test(ctx):
    view = Modal_View()
    message = await ctx.respond('Your_Message', components=view)
    await view.start(message)
#Creates the Command ^

#Coded by Velocity7