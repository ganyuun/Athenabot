import os
import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx):
        """Reloads the bot's cogs"""
        for cog in tuple(self.bot.extensions.keys()):
            self.bot.reload_extension(cog)
        await ctx.message.add_reaction('✅')

    @commands.command()
    @commands.is_owner()
    async def update(self, ctx):
        """Updates the bot then reloads the cogs"""
        # Update files from github
        stream = os.popen('git pull')
        output = stream.read()
        if 'Already up to date' in output:
            output = ""
        cogs = tuple(self.bot.extensions.keys())
        # Existing cogs
        for cog in cogs:
            try:
                self.bot.reload_extension(cog)
            except commands.ExtensionFailed as e:
                output += f'\n\n{e}'
        # New cogs
        for filename in os.listdir('./cogs'):
            newcog = f'cogs.{filename[:-3]}'
            if filename.endswith('.py') and newcog not in cogs:
                try:
                    self.bot.load_extension(newcog)
                except commands.NoEntryPointError:
                    pass
                except commands.ExtensionFailed as e:
                    output += f'\n\n{e}'
        if output:
            await ctx.send(f'```{output}```')
        else:
            await ctx.message.add_reaction('✅')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error: commands.CommandError):
        if isinstance(error, commands.NotOwner):
            await ctx.message.add_reaction('❌')
        else:
            print(error)


class EmbedHelpCommand(commands.HelpCommand):
    COLOR = discord.Color(int('AD2747', 16))

    def get_command_signature(self, command):
        return f'{command.qualified_name} {command.signature}'

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title='AthenaBot Commands', colour=self.COLOR)
        for cog, cmds in mapping.items():
            name = 'No Category' if cog is None else cog.qualified_name
            filtered = await self.filter_commands(cmds, sort=True)
            if filtered:
                value = '\n'.join(f'`{c.name}` - {c.short_doc}' for c in filtered)
                embed.add_field(name=name, value=value, inline=False)

        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title=f'{cog.qualified_name} Commands', colour=self.COLOR,
                              description=cog.description)
        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.add_field(name=self.get_command_signature(command),
                            value=command.short_doc or '...', inline=False)
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, cmd: commands.Command):
        embed = discord.Embed(title=cmd.qualified_name, colour=self.COLOR, description="")
        if cmd.help:
            embed.description += cmd.help
        if cmd.aliases:
            embed.add_field(name="Aliases", value=','.join(f'`{c}`' for c in cmd.aliases))
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(title=group.qualified_name, colour=self.COLOR, description="")
        if group.help:
            embed.description += group.help
        filtered = await self.filter_commands(group.commands, sort=True)
        for command in filtered:
            embed.add_field(name=self.get_command_signature(command), value=command.short_doc or '...',
                            inline=False)
        await self.get_destination().send(embed=embed)


def setup(bot: commands.Bot):
    cog = Admin(bot)
    bot.add_cog(cog)
    bot.help_command = EmbedHelpCommand()
    bot.help_command.cog = cog