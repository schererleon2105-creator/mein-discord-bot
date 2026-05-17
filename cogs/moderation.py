import discord
from discord import app_commands
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="Löscht Nachrichten")
    @app_commands.describe(amount="Wie viele Nachrichten? (1-100)")
    async def clear(self, interaction: discord.Interaction, amount: int):
        if not interaction.user.guild_permissions.manage_messages:
            return await interaction.response.send_message("❌ Du hast keine Rechte dafür!", ephemeral=True)
        
        if amount < 1 or amount > 100:
            return await interaction.response.send_message("❌ Bitte eine Zahl zwischen 1 und 100 eingeben!", ephemeral=True)
        
        await interaction.channel.purge(limit=amount + 1)
        await interaction.response.send_message(f"🧹 {amount} Nachrichten gelöscht!", ephemeral=True)

    @app_commands.command(name="kick", description="Kickt einen User")
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "Kein Grund angegeben"):
        if not interaction.user.guild_permissions.kick_members:
            return await interaction.response.send_message("❌ Keine Rechte!", ephemeral=True)
        
        await member.kick(reason=reason)
        await interaction.response.send_message(f"✅ {member.mention} wurde gekickt.")

    @app_commands.command(name="ban", description="Bannt einen User")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = "Kein Grund angegeben"):
        if not interaction.user.guild_permissions.ban_members:
            return await interaction.response.send_message("❌ Keine Rechte!", ephemeral=True)
        
        await member.ban(reason=reason)
        await interaction.response.send_message(f"✅ {member.mention} wurde gebannt.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))