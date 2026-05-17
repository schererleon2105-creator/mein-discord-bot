import discord
from discord import app_commands
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="meme", description="Sendet ein zufälliges Meme")
    async def meme(self, interaction: discord.Interaction):
        memes = ["https://i.imgur.com/4z3kJ0L.jpg", "https://i.imgur.com/2Y8v9fG.jpg", "https://i.imgur.com/5z2kJ9P.jpg"]
        await interaction.response.send_message(random.choice(memes))

    @app_commands.command(name="8ball", description="Stelle eine Ja/Nein Frage")
    @app_commands.describe(frage="Deine Frage")
    async def eightball(self, interaction: discord.Interaction, frage: str):
        answers = ["Ja definitiv!", "Nein.", "Vielleicht...", "Sieht gut aus.", "Frag später nochmal."]
        await interaction.response.send_message(f"🎱 **Frage:** {frage}\n**Antwort:** {random.choice(answers)}")

    @app_commands.command(name="hug", description="Umarmt jemanden")
    @app_commands.describe(member="Wen willst du umarmen?")
    async def hug(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(f"{interaction.user.mention} umarmt {member.mention}! 🤗")

async def setup(bot):
    await bot.add_cog(Fun(bot))