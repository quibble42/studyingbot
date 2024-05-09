from discord.ext import commands, tasks
import discord
import datetime
from dataclasses import dataclass

BOT_TOKEN= "YOURTOKENHERE"
CHANNEL_ID = GET THE CHANNEL ID FROM DISCORD VIA DEVELOPER MODE
MAX_SESSION_TIME_MINUTES = 0.01


@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
session = Session()

@bot.event
async def on_ready():
    print("Hi! Study Bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hi! Study Bot is ready!")


@tasks.loop(minutes=MAX_SESSION_TIME_MINUTES, count=10)
async def break_reminder():
    if break_reminder.current_loop == 0:
        return
    
    if break_reminder.current_loop == 10:
        await channel.send(f"**Take a break!** You've been studying for THE MAXIMUM AMOUNT OF MINUTES: {Session_Minutes} minutes.")
    
    channel = bot.get_channel(CHANNEL_ID)
    Session_Minutes = MAX_SESSION_TIME_MINUTES * break_reminder.current_loop
    await channel.send(f"**Take a break!** You've been studying for {Session_Minutes} minutes.")

@bot.command()
async def add(ctx, *arr):
    result=0
    for i in arr: 
        result += int(i)
    await ctx.send(f"{result}")

@bot.command()
async def start(ctx):
    if session.is_active:
        await ctx.send("A session is already active!")
        return
    
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")
    break_reminder.start();
    await ctx.send(f"Study session started at {human_readable_time}")
    

@bot.command()
async def stop(ctx):
    if not session.is_active:
        await ctx.send("No session is active!")
        return
    
    session.is_active = False
    stop_time = ctx.message.created_at.timestamp()
    duration = stop_time - session.start_time
    human_readable_duration = str(datetime.timedelta(seconds=duration))
    break_reminder.stop();
    await ctx.send(f"Study session ended at {human_readable_duration}")





bot.run(BOT_TOKEN)