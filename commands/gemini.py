import hikari, lightbulb, google.generativeai

google.generativeai.configure(api_key='AIzaSyAmORUF820NIvNyFQMJoMD_fA0ZqCQ7fRM')
model = google.generativeai.GenerativeModel('gemini-3.1-flash-lite-preview')
loader = lightbulb.Loader()


@loader.command
class Gemini(lightbulb.SlashCommand, name="gemini", description="Interact with Gemini"):
    prompt = lightbulb.string("prompt", "Enter a prompt")

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        prompt_str = str(self.prompt)
        response = model.generate_content(f'Without using any bullet points or other formatting options strictly answer this keep it under 150 words: {prompt_str}')
        await ctx.respond(response.text,  flags=hikari.MessageFlag.EPHEMERAL)

#Coded by Velocity7