import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    print("Login")
    print(client.user.name)
    print(client.user.id)
    print("--------------------")
    await client.change_presence(game=discord.Game(name='', type=1))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('za'):
        await client.send_message(message.channel, "AMD Radeon HD 6950 Bot v7.0")  
        await client.send_message(message.channel, "명령어 목록입니다. 모든 명령어 앞에는 z를 입력하세요.")  
        await client.send_message(message.channel, "z오늘 : 오늘의 날짜를 알려드립니다.")  
        await client.send_message(message.channel, "z시간 : 지금 시간을 알려드립니다.")  
        await client.send_message(message.channel, "z숙제 : 현재 해야 할 숙제를 알려드립니다.")  
        await client.send_message(message.channel, "z날씨 : 현재 전국 날씨를 알려드립니다.")  
        await client.send_message(message.channel, "z(요일)시간표(ex. /월시간표) : 월요일 ~ 금요일까지의 시간표를 알려드립니다.")  
        await client.send_message(message.channel, "z따라하기 (적을거) : 말을 따라합니다. /따라하기 뒤에 띄어쓰기를 해야 제대로 실행됩니다.")  
        await client.send_message(message.channel, "z주사위 : 1부터 6까지 중 숫자 하나를 무작위로 뽑습니다.")  
        await client.send_message(message.channel, "z유튭 : 이 봇 제작자의 유튜브 채널 주소를 알려드립니다.")  
        await client.send_message(message.channel, "z코 : 중국산 코로나 관련 정보를 알려드립니다.")  
        await client.send_message(message.channel, "z숨목록 : 숨겨진 명령어 목록을 알려드립니다.")  
        await client.send_message(message.channel, "z역사 : 역사 시험범위 제외 부분을 알려드립니다.")  
        await client.send_message(message.channel, "이 봇에 새로 넣을 거 있으면 추천 바랍니다.")  

    elif message.content.startswith('z숨목록'):
        await client.send_message(message.channel, "숨겨진 명령어 목록입니다. 여기 명령어들은 대부분 슬래쉬가 필요 없습니다.(있는 것은 슬래쉬 쳐져있음)")
        await client.send_message(message.channel, "fuck(또는 Fuck) : Lily Allen의 Fuck You 음악 뮤비 유튜브 주소를 보여드립니다.")
        await client.send_message(message.channel, "z섹온비 : 섹온비 유튜브 주소를 띄웁니다.")
        await client.send_message(message.channel, "zijhs : Lonely Island의 I Just Had Sex 유튜브 뮤비 주소를 띄웁니다.")
        await client.send_message(m
