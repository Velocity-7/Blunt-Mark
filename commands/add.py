import hikari, lightbulb

loader = lightbulb.Loader()

@loader.command
class Add(lightbulb.SlashCommand, name="add", description="Add upto 4 numbers together"):
    num_1 = lightbulb.integer("num_1", "Number 1")
    num_2 = lightbulb.integer("num_2", "Number 2")
    num_4 = lightbulb.integer("num_4", "Number 4 (optional)", default=None)
    num_3 = lightbulb.integer("num_3", "Number 3 (optional)", default=None)

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        sum_val = self.num_1 + self.num_2
        if self.num_3 is not None:
            sum_val += self.num_3
        if self.num_4 is not None:
            sum_val += self.num_4
        await ctx.respond(f'The sum of the numbers is {sum_val}.', flags=hikari.MessageFlag.EPHEMERAL)

#Coded by Velocity7