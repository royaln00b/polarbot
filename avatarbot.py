import discord
import asyncio
import PIL
from discord.ext.commands import Bot
from discord.ext import commands
import time
import random
from random import sample
import os
from PIL import Image



bot=commands.Bot(description="Polaris bot. This bot was brought to you by Royalnoob. Built from scratch.",command_prefix=";",pm_help=False)

bot.remove_command('help')


@bot.command(pass_context=True)
async def help(ctx,*,command=None):
	if ctx.message.author.id == "379303619545137152":
		embed=discord.Embed(title="Command List" , description= "1 . ping - Shows latency of the bot\n2. channel - Choose your channels!\n3. setmy - Set your gender and pings!\n4. 8ball - Ask the 8ball a question!\n\nRemember if you need any help with these command you can type `;help [command]` to find out more!",colour = 0x000000)
		await bot.say(embed=embed)
	elif ctx.message.author.id != "379303619545137152" and command is None:
		await bot.say("Hey "+ctx.message.author.mention+"! Use this -> <#469486865305698304>")
	elif command == "suggest":
		await bot.send_message(ctx.message.author,"`;suggest [command to be added]`")
	elif command == "avatar":
		await bot.send_message(ctx.message.author,"`;avatar [member]`")
	elif command == "8ball":
		await bot.send_message(ctx.message.author,"`;8ball [question]`")
	elif command == "channel":
		await bot.send_message(ctx.message.author,"`;channel [add/remove] [channel]`")
	elif command == "setmy":
		await bot.send_message(ctx.message.author,"`;setmy [gender/pings] [selection]`")

@bot.command(pass_context=True)
async def ping(ctx):
    chars = '0123456789ABCDEF'
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await bot.send_typing(channel)
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description='Ping: {}ms'.format(round(((t2-t1)*1000)-100)), color = discord.Colour(int('0x'+''.join(sample(chars,6)),16)))
    await bot.say(embed=embed)


	
@bot.command(pass_context=True)
async def suggest(ctx,*,description):
	await bot.add_reaction(message = ctx.message, emoji = "✅")
	await bot.send_message(discord.utils.get(ctx.message.server.members, name='Royalnoob'),ctx.message.author.display_name+" suggested a command to be added:\n\n"+description)

@bot.command(pass_context=True)   
async def avatar(ctx,*, user:discord.Member=None):
   if user == None:
        user = ctx.message.author
   embed = discord.Embed (color=0xff0000)
   embed.set_image(url=user.avatar_url)
   await bot.say(embed=embed)

@bot.event
async def on_member_join(member):
	server = member.server
	fmt = '**You can stay here {0.mention} in {1.name} as long as you dont kill anyone**!'
	await bot.send_message(bot.get_channel("467462021412290561"), fmt.format(member, server))
	await bot.add_roles(member,discord.utils.get(server.roles,name=str("Members")))
#----------------------------------------------------------------------------------------------------------
#                                              8ball
_8balllist = ["It is certain :8ball:","It is decidedly so :8ball:","Without a doubt :8ball:","You may rely on it :8ball:","As I see it, yes :8ball:","Most likely :8ball:","Outlook good :8ball:","Yes :8ball:","Signs point to yes :8ball:","Reply hazy try again :8ball:","Ask again later :8ball:","Better not tell you now :8ball:","Cannot predict now :8ball:","Concentrate and ask again :8ball:","Don't count on it :8ball:","My reply is no :8ball:","My sources say no :8ball:","Outlook not so good :8ball:","Very doubtful :8ball:", "Consider it a pass :8ball:", "It may happen to be true :8ball:", "It appears to be false :8ball:", "Go for it :8ball:", "Thats a small secret :8ball:", "Oh sorry I wasn't paying attention :c :8ball:", "You can bet it will be true :8ball:", "Definite yes :8ball:", "Don't count on that too much :8ball:"]
       
@bot.command(name="8ball",pass_context=True)
async def _8ball(ctx):
	await bot.say(random.choice(_8balllist))

#----------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------
#                                              AUTO ASSIGN ROLES CODE
_channels = ["chat","hangout","memes","toxic","fanstalk","gaming","trading","sports"]
@bot.command(pass_context=True)
async def channel(ctx,action,*,channel):
	failembed=discord.Embed(title="ERROR",description="`"+action+"` or "+"`"+channel+"` Could not be found. Please try again.",colour=0xFF0000)
	addembed=discord.Embed(title="Success!",description="You have been added to the "+channel+" channels! Have fun!",colour=0x00FF00)
	removeembed=discord.Embed(title="Success!",description="You have been removed from the "+channel+" channels! Have fun!",colour=0xBDB76B)
	if action == "remove":
		actions = "removed from"
		if channel in _channels:
			await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name=str(channel)))
			await bot.say(embed = removeembed)
		else:
			await bot.say(embed = failembed)
	elif action == "add":
		actions = "added to"
		if channel in _channels:
			await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name=str(channel)))
			await bot.say(embed = addembed)
		else:
			await bot.say(embed = failembed)
	elif action != "remove":
		if action != "add":
			await bot.say(embed = failembed)
#					       AUTO ASSIGN GENDER AND PINGS
_gender = ["male","female","transgender","not specified"]
_pinglist = ["all","non","important"]
@bot.command(pass_context=True)
async def setmy(ctx,action,*,selection):
	failembed=discord.Embed(title="ERROR",description="`"+action+"` or "+"`"+selection+"` Could not be found. Please try again.",colour=0xFF0000)
	if action == "gender":
		if selection.lower() in _gender:
			if "male" in [y.name.lower() for y in ctx.message.author.roles]:
				await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name="male"))
			if "female" in [y.name.lower() for y in ctx.message.author.roles]:
				await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name="female"))
			if "transgender" in [y.name.lower() for y in ctx.message.author.roles]:
				await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name="transgender"))
			if "not specified" in [y.name.lower() for y in ctx.message.author.roles]:
				await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name="not specified"))
			await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name=str(selection.lower())))
			await bot.add_reaction(message = ctx.message, emoji = "✅")
		else:
			await bot.say(embed=failembed)
	elif action == "pings":
		if selection.lower() in _pinglist:
			if "all" in [y.name.lower() for y in ctx.message.author.roles]:
				await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name="all"))
			if "important" in [y.name.lower() for y in ctx.message.author.roles]:
				await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name="important"))
			if selection.lower() == "all":
				await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name=str(selection.lower())))
				await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name="important"))
				await bot.add_reaction(message = ctx.message, emoji = "✅")
			elif selection.lower() == "important":
				await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name=str(selection.lower())))
				await bot.add_reaction(message = ctx.message, emoji = "✅")
			elif selection.lower() == "non":
				if "all" in [y.name.lower() for y in ctx.message.author.roles]:
					await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name="all"))
				if "important" in [y.name.lower() for y in ctx.message.author.roles]:
					await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name="important"))
				await bot.add_reaction(message = ctx.message, emoji = "✅")
				
		else:
			await bot.say(embed=failembed)
				
	
	else:
		await bot.say(embed=failembed)


#                                              LIST OF ALL CHANNELS THAT CAN BE ASSIGNED

_channels2 = ["Chat","Hangout","Memes","Toxic","Fanstalk","Gaming","Trading","Sports"]
@bot.command(pass_context=True)
async def channels(ctx):
	if ctx.message.author.id == "379303619545137152":
		embed = discord.Embed(title="Channels",description="**Here you can find all of the channels available for you to access:**\n"+"\n\n".join(_channels2)+" ",colour=0x000000)
		await bot.say(embed=embed)
	

#----------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------
#                                              ADMIN COMMANDS

# PURGE
@bot.command(pass_context=True)
async def purge(ctx,num: int):
	if "manager" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.purge_from(ctx.message.channel,limit=num)
	else:
		await bot.say("No")
# RULE ADDING




#----------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------
#                                              TESTING PILLOW



#----------------------------------------------------------------------------------------------------------


@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(type=0, name=';help'))

token = os.getenv('TOKEN')
bot.run(token)
