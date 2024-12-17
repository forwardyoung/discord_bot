import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # 멤버 관련 이벤트를 받기 위해 필요
intents.guilds = True  # 서버/채널 정보 접근에 필요

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
    print(member, '멤버')
    try:
        welcome_channel = bot.get_channel(WELCOME_CHANNEL_ID)
        if welcome_channel:
            welcome_message = f"""
{member.mention} 안녕하세요.
PyLadies Seoul에 오신 것을 환영합니다.
이 채널에 간단한 소개와 인사를 해볼까요?
Python에 관심 많은 여성들이 모여 안정감을 주고 더 큰 세계로 나아갈 수 있도록 해요!\n
[PyLadies Seoul의 목표](https://tasty-shift-3a9.notion.site/PyLadies-Seoul-1989df32cf9941c8981c0acead05eecc)   

Hello {member.mention}!
Welcome to PyLadies Seoul!
Would you like to introduce yourself and say hello in this channel?
We're a community of women interested in Python, coming together to create a supportive environment and explore greater possibilities!\n
Learn more about [PyLadies Seoul's mission](https://tasty-shift-3a9.notion.site/PyLadies-Seoul-1989df32cf9941c8981c0acead05eecc)
"""
            await welcome_channel.send(welcome_message)
        else:
            print(f"환영 채널을 찾을 수 없습니다. ID: {WELCOME_CHANNEL_ID}")
    except Exception as e:
        print(f"멤버 입장 처리 중 오류 발생: {e}")


bot.run(os.getenv('DISCORD_TOKEN'))
