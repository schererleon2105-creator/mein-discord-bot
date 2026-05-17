import discord
from discord import app_commands
from discord.ext import commands

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reaction_roles = {}  # Speichert Message-ID → Emoji:Role

    @app_commands.command(name="reactionrole", description="Erstellt eine Reaction-Role Nachricht")
    @app_commands.describe(title="Titel", beschreibung="Beschreibung der Nachricht")
    async def create(self, interaction: discord.Interaction, title: str, beschreibung: str):
        if not interaction.user.guild_permissions.manage_roles:
            return await interaction.response.send_message("❌ Du brauchst Rechte zum Verwalten von Rollen!", ephemeral=True)

        embed = discord.Embed(title=title, description=beschreibung + "\n\nReagiere mit den Emojis unten!", color=0x00ff00)
        await interaction.response.send_message(embed=embed)
        message = await interaction.original_response()

        # Beispiel-Reaktionen
        await message.add_reaction("🔴")
        await message.add_reaction("🟢")
        await message.add_reaction("🔵")

        # Speichern für später (Message ID)
        self.reaction_roles[message.id] = {
            "🔴": None,   # Hier später Rollen-ID eintragen
            "🟢": None,
            "🔵": None
        }
        await interaction.followup.send("✅ Reaction Role Nachricht erstellt!", ephemeral=True)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id not in self.reaction_roles:
            return
        if payload.user_id == self.bot.user.id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        if not member:
            return

        emoji = str(payload.emoji)
        role_id = self.reaction_roles[payload.message_id].get(emoji)

        if role_id:
            role = guild.get_role(role_id)
            if role:
                await member.add_roles(role)

async def setup(bot):
    await bot.add_cog(ReactionRoles(bot))