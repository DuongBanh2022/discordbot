import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('Hello'):
            await message.channel.send(f'Please be normal. {message.author}')
            
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')
        
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel:
            await channel.send(f"Welcome to the server, {member.mention}!")

        
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True

intents.members = True  # <-- Required for on_member_join

client = MyClient(intents=intents)
client.run('MTM2MzAwMDU4Mjk1NjEyMjIyMg.GWMUUp.T0fx4yQm69fInVdmKmyf8GC39oSVErwI__5fec')


