import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='!')

'''
봇이 반응을 해야하는 명령어인지 구분하기 위해 메세지 앞에 붙이는 접두사(prefix)를 설정합니다. 현재 !로 
설정되어있습니다. 이곳을 변경시 해당 문자로 명령어를 시작해야합니다. ext에선 discord.Client() 클래스 처럼 
str.startswith 메서드를 사용할 필요가 없습니다.
'''

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name) # 토큰으로 로그인 된 bot 객체에서 discord.User 클래스를 가져온 뒤 name 프로퍼티를 출력
    print(bot.user.id) # 위와 같은 클래스에서 id 프로퍼티 출력
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name="1234")
async def _1234(ctx):
    await ctx.send("5678")
#파이썬 문법에 따라 함수를 만들 때에는 첫글자엔 숫자를 넣을 수 없는데, 숫자를 사용하고싶다면 함수 이름 자리는 다른 아무것으로 대체하고 괄호 안에 name=""을 사용하여 명령어를 수행할 수 있다.

bot.run('token')
