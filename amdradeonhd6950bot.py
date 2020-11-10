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
    await client.change_presence(game=discord.Game(name="도움말 = /A 입력")
@client.event
async def on_message(message):
    if message.content.startswith('/A'):
        await client.send_message(message.channel, "AMD Radeon HD 6950 Bot v7.0")  
        await client.send_message(message.channel, "명령어 목록입니다. 모든 명령어 앞에는 /를 입력하세요.")  
        await client.send_message(message.channel, "/오늘 : 오늘의 날짜를 알려드립니다.")  
        await client.send_message(message.channel, "/시간 : 지금 시간을 알려드립니다.")  
        await client.send_message(message.channel, "/숙제 : 현재 해야 할 숙제를 알려드립니다.")  
        await client.send_message(message.channel, "/날씨 : 현재 전국 날씨를 알려드립니다.")  
        await client.send_message(message.channel, "/(요일)시간표(ex. /월시간표) : 월요일 ~ 금요일까지의 시간표를 알려드립니다.")  
        await client.send_message(message.channel, "/따라하기 (적을거) : 말을 따라합니다. /따라하기 뒤에 띄어쓰기를 해야 제대로 실행됩니다.")  
        await client.send_message(message.channel, "/주사위 : 1부터 6까지 중 숫자 하나를 무작위로 뽑습니다.")  
        await client.send_message(message.channel, "/유튭 : 이 봇 제작자의 유튜브 채널 주소를 알려드립니다.")  
        await client.send_message(message.channel, "/코 : 중국산 코로나 관련 정보를 알려드립니다.")  
        await client.send_message(message.channel, "/숨목록 : 숨겨진 명령어 목록을 알려드립니다.")  
        await client.send_message(message.channel, "/역사 : 역사 시험범위 제외 부분을 알려드립니다.")  
        await client.send_message(message.channel, "이 봇에 새로 넣을 거 있으면 추천 바랍니다.")  

    if message.content.startswith('/숨목록'):
        await client.send_message(message.channel, "숨겨진 명령어 목록입니다. 여기 명령어들은 대부분 슬래쉬가 필요 없습니다.(있는 것은 슬래쉬 쳐져있음)")
        await client.send_message(message.channel, "fuck(또는 Fuck) : Lily Allen의 Fuck You 음악 뮤비 유튜브 주소를 보여드립니다.")
        await client.send_message(message.channel, "/섹온비 : 섹온비 유튜브 주소를 띄웁니다.")
        await client.send_message(message.channel, "/ijhs : Lonely Island의 I Just Had Sex 유튜브 뮤비 주소를 띄웁니다.")
        await client.send_message(message.channel, "유튜브(또는 yt) : 야스봇 제작자의 유튜브 채널 주소를 띄웁니다.")
        await client.send_message(message.channel, "//숨목록 : 궁금하면 해보세요")
        
    if message.content.startswith('//숨목록'):
        await client.send_message(message.channel, "//hub : 그 허브 주소를 알려드립니다.")
        await client.send_message(message.channel, "//x : 그 Videos 주소를 알려드립니다.")
    if message.content.startswith('a글카'):
        await client.send_message(message.channel, "가성비를 원하시면 엔비디아 대신 에이엠디로 가시는 걸 추천합니다.")
    if message.content.startswith('a4딸역'):
        await client.send_message(message.channel, "https://m.youtube.com/watch?v=fRPg0Se9sms 정말 재밌습니다!")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
