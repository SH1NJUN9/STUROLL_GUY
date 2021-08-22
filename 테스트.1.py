import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print("""내 목숨을 "MGLD"에!""".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'ㅏㅡㅑ명령어':
        await message.channel.send('ㅏㅡㅑ안녕, ㅏㅡㅑ샌즈, ㅏㅡㅑ우주최강PSG, ㅏㅡㅑ주원, ㅏㅡㅑMGLD, ㅏㅡㅑ')
    if message.content == 'ㅏㅡㅑ안녕':
        await message.channel.send('으응...(아 찐따새끼)')
    if message.content == 'ㅏㅡㅑ샌즈':
        await message.channel.send('와 샌즈! 언더테일 아시는구나! 혹시 모르시는분들에 대해 설명해드립니다 샌즈랑 언더테일의 세가지 엔딩루트중 몰살엔딩의 최종보스로 진.짜.겁.나.어.렵.습.니.다 공격은 전부다 회피하고 만피가 92인데 샌즈의 공격은 1초당 60이 다는데다가 독뎀까지 추가로 붙어있습니다.. 하지만 이러면 절대로 게임을 깰 수 가없으니 제작진이 치명적인 약점을 만들었죠. 샌즈의 치명적인 약점이 바로 지친다는것입니다. 패턴들을 다 견디고나면 지쳐서 자신의 턴을 유지한채로 잠에듭니다. 하지만 잠이들었을때 창을옮겨서 공격을 시도하고 샌즈는 1차공격은 피하지만 그 후에 바로날아오는 2차 공격을 맞고 죽습니다')
    if message.content == 'ㅏㅡㅑ주원':
        await message.channel.send('병신 아 아니...멋진 사람^^;;ㅎ')
    if message.content == 'ㅏㅡㅑ우주최강PSG':
        await message.channel.send('아 PSG아는구나 진짜 ㅈㄴ 최강이긴하지 만약 팬이 아니라면 어서 팬이 돼라!')
    if message.content == 'ㅏㅡㅑMGLD':
        await message.channel.send('위-대-한-우-리-의-***')
    if message.content == 'ㅏㅡㅑ':
        await message.channel.send('ㅏㅡㅑ')
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
