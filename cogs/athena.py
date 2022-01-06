import discord
from discord.ext import commands

class AthenaCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #ping command
    @commands.command()
    async def ping(self, ctx):
        """Sends a message with ping in ms"""
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def pog(self, ctx):
        """Sends a pog emoji"""
        await ctx.send('<:pog:804373562274217985>')

    #song command
    @commands.command()
    async def song(self, ctx):
        """Posts a random song"""
        songs = [
            "https://open.spotify.com/track/6nRJTn59VvyEw333QzxPOb?si=20c64379396e4f78",
            "https://open.spotify.com/track/1uC1sBpO2Orz049ApZNfxT?si=b73be6589f294332",
            "https://open.spotify.com/track/2SNUnuFt4eTCEUMHAEmyea?si=17de5148e9a24cb3",
            "https://open.spotify.com/track/4iUDTgkbosia5aneiGXRXc?si=2e3fad5530a74250",
            "https://open.spotify.com/track/6pmYiUWpJkTa5Q5sVrF0wi?si=1945943e6de24656",
            "https://open.spotify.com/track/0gjKbgfWl0NBqdTSblKjCg?si=c8a9bfecd5434ecc",
            "https://open.spotify.com/track/6oL7mmfbuNMw41ZjUL9whj?si=ff162d5af8fb4b06",
            "https://www.youtube.com/watch?v=Mj2HFLs-0sE",
            "https://www.youtube.com/watch?v=DaK7zVoKbl8",
            "https://open.spotify.com/track/6looCR8dNog0skCIldjlOa?si=860ab5c6d8254924",
            "https://open.spotify.com/track/1r3dIlrJgbGYmRh3mrzwNe?si=0005ea5fc5ed4d1d",
            "https://open.spotify.com/track/6zcicpr8OKns6iR7unKZNU?si=9ab80b1452d145aa",
            "https://open.spotify.com/track/59eFIMQ16qAGVt4NAF6JXH?si=48a5223127c34a10",
            "https://open.spotify.com/track/7ttt5aIgGcDCWqUPh37swz?si=2bafe22c51a84066",
            "https://open.spotify.com/track/4zvSIAk10UBilreDozjGI0?si=9c7e78bb4b04450b",
            "https://open.spotify.com/track/3x8QKvIFop2DQQ4HMdEWKs?si=b2ad0b38017d4a3b",
            "https://open.spotify.com/track/2Uer7J87AJzKkpcTP4lpGY?si=fdf5a9f5aebe4a3c",
            "https://open.spotify.com/track/53n8NkFXyiwQ8y5naIyNtq?si=ceeabc5769444e63",
            "https://open.spotify.com/track/23eNTZIykjVEktFtNUgiTh?si=f2ae0a76f8814a93",
            "https://open.spotify.com/track/6hg8bNptuX6Iv1WylVfb1W?si=792875383a5e4633",
        ]
        await ctx.send(random.sample(songs, 1)[0])

    #Vi quote command
    @commands.command()
    async def viquote(self, ctx):
        """Posts a random Vi quote"""
        quotes = [
            "Punch first. Ask questions while punching.",
            "If I want your opinion, I'll beat it out of you.",
            "They'll never know what hit 'em.",
            "Piltover's finest.",
            "If you hit a wall, hit it hard!",
            "I let my hands do the talking.",
            "Care for a spot of tea? Or maybe a spot of punch in the face!",
            "Oh, look at me...~ I'm on the case~.",
            "We can either do this the hard way or... oh wait, no, there's just the hard way.",
            "Why can't I get a straight answer? It's always just 'Oh no! Stop hitting me! Ow, my face!'",
            "Freeze! Or don't, I don't care.",
            "Vi, hah, stands for violence!",
            "Vi stands for vicious.",
            "Vi stands for vice.",
            "Nice shot, cupcake.",
            "Hey, Jayce! Power slam!",
            "Aww, was that supposed to hurt, Cait?",
            "Piltover enforcer, on the scene!",
            "Vi, stands for victory!",
            "I'll chat with cupcake later.",
            "Ahahah. Cait's still got a sweet tooth for bad cops?",
            "Piltover enforcer, on the scene!",
        ]
        await ctx.send(random.sample(quotes, 1)[0])

def setup(bot: commands.Bot):
    cog = AthenaCommands(bot)
    bot.add_cog(cog)