import discord
from discord import app_commands
from discord.ext import commands

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="level", description="Zeigt dein Level")
    async def level(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user
        embed = discord.Embed(title=f"📊 Level von {member.name}", color=0x00ffff)
        embed.add_field(name="Level", value="1 (Demo)", inline=True)
        embed.add_field(name="XP", value="0/50", inline=True)
        embed.set_thumbnail(url=member.display_avatar.url)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Levels(bot))