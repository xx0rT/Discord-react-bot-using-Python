import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("!roleadd"):
        args = message.content.split(" ")
        user = message.author
        if user.guild_permissions.manage_roles:
            role_name = args[1]
            role = discord.utils.get(message.guild.roles, name=role_name)
            if role:
                await user.add_roles(role)
                await message.channel.send("Role přidána!")
            else:
                await message.channel.send("Tato role neexistuje.")
        else:
            await message.channel.send("Na tuto roly nemáš permise.")

client.run("MTA0Mjg1NDE2Mjc3OTYwMjk4NQ.GRAhA8.0L-xbtVsq6uL-Ey4q2ZmMEsOtBisIzCI1Yfi0k")