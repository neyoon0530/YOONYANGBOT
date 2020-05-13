from random import random, randint

import discord
import datetime

import openpyxl as openpyxl

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print ("윤냥봇 출동 준비 완료했다냥!")
    game = discord.Game("5개의 서버에서 집사들 부리기")
    await client.change_presence(status=discord.Status.online, activity=game)

prefix = ("윤냥아 ")

@client.event
async def on_message(message):
    if message.content.startswith(prefix + "안녕"):
        await message.channel.send("하위! 윤냥이다냥!")
    if message.content.startswith(prefix + "반가워"):
        await message.channel.send("반갑다냥!")
    if message.content.startswith(prefix + "엔트리"):
        await message.channel.send("엔트리와 함께 건강한 소프트웨어 교육 생태계를 조성하자냥!")
    if message.content.startswith(prefix + "네윤"):
        await message.channel.send("내 개인 비서다냥!")
    if message.content.startswith(prefix + "디스코드"):
        await message.channel.send("내 집이다냥!")
    if message.content.startswith(prefix + "돈줘"):
        await message.channel.send("이 윤냥이한테 뭘 바라는거냥?! 난 디토봇이 아니다냥!")
    if message.content.startswith(prefix + "디엘"):
        await message.channel.send("디엘은 만나면 물거다냥! 엘이를 시켜 내 개인 비서를 물게 하다니! (갸루룽)")
    if message.content.startswith(prefix + "엘"):
        await message.channel.send("엘이는 만나면 물거다냥! 내 개인 비서를 물다니! (갸루룽)")
    if message.content.startswith(prefix + "심심해"):
        await message.channel.send("확률 게임 하라냥")
    if message.content.startswith(prefix + "졸려"):
        await message.channel.send("졸릴 땐 자는 게 최고다냥😴")
    if message.content.startswith(prefix + "졸리다"):
        await message.channel.send("졸릴 땐 자는 게 최고다냥😴")
    if message.content.startswith(prefix + "놀자"):
        await message.channel.send(message.author.name + "! 집사로써 충성을 다 하진 못 할 망정 농땡이를 부리냥? " + message.author.name + " 집사는 월급 삭감하겠다냥!")
    if message.content.startswith(prefix + "도트"):
        await message.channel.send("도트 집사는 코딩을 잘하는 집사라고 들었다냥! 근데 코딩이 뭐지...")
    if message.content.startswith(prefix + "캉"):
        await message.channel.send("캉 집사는 내 동족을 데리고 다닌다냥!")
    if message.content.startswith(prefix + "설빙"):
        await message.channel.send("설빙 집사를 보면 어째 시원해지는 것 같다냥!")
    if message.content.startswith(prefix + "베이지"):
        await message.channel.send("자신만의 그림체가 있는 집사다냥! 나도 그려주면 좋겠다냥...")
    if message.content.startswith(prefix + "작순"):
        await message.channel.send("그림을 끝내주게 잘 그리는 집사다냥! 나도 그려주면 좋겠다냥...")
    if message.content.startswith(prefix + "티라미수"):
        await message.channel.send("티라미수 집사 그림체는 정말 귀엽다냥! 나도 그려주면 좋겠다냥...")
    if message.content.startswith(prefix + "사캐"):
        await message.channel.send("사캐 집사는 뭔가 내가 아는 다른 집사들이랑 다르다냥. 하지만 좋은 집사다냥!")
    if message.content.startswith(prefix + "꿀벌"):
        await message.channel.send("꿀벌 집사는 침이 있지만 하나도 안 무섭다냥. 좋은 집사다냥!")
    if message.content.startswith(prefix + "큐브"):
        await message.channel.send("큐브 집사는 아직 잘 모른다냥. 하지만 좋은 집사일 것 같다냥.")
    if message.content.startswith(prefix + "뭐 해") or message.content.startswith(prefix + "뭐해"):
        await message.channel.send(message.author.name + " 집사랑 대화하고 있다냥!")
    if message.content.startswith(prefix + "끝말잇기"):
        await message.channel.send("끝말잇기는 크시랑 하라냥")
    if message.content.startswith(prefix + "끝말잇기 하자"):
        await message.channel.send("귀찮다냥")
    if message.content.startswith(prefix + "윤냥"):
        await message.channel.send("내 이름이다냥!")
    if message.content.startswith(prefix + "라면"):
        await message.channel.send("라면 먹냥?! 나도 한 입 줘라냥!🍜")
    if message.content.startswith(prefix + "뭐하지"):
        await message.channel.send("내 털이나 빗어주라냥. (갸루룽)")
    if message.content.startswith(prefix + "이름이 뭐야"):
        await message.channel.send(message.author.name + " 집사, 내 이름도 모르냥?! 실망이다냥!")
    if message.content.startswith(prefix + "내 이름"):
        await message.channel.send(message.author.name + " 집사다냥!")
    if message.content.startswith(prefix + "그릭"):
        await message.channel.send("그릭 집사? 그릭그릭그릭")
    if message.content.startswith(prefix + "꾸릭"):
        await message.channel.send("꾸릭꾸릭꾸릭꾸릭꾸릭꾸릭")
    if message.content.startswith(prefix + "할퀴기"):
        await message.channel.send("갸루룽!")
        await message.channel.send("(스이이이잉)")
    if message.content.startswith(prefix + "내려찍기"):
        await message.channel.send("(콰아아아앙!)")
    if message.content.startswith(prefix + "꾹꾹이"):
        await message.channel.send("(꾹꾹)")
        await message.channel.send("이 꾹꾹이는 공격 기술이다냥. 절대 안마 기능이 아니라냥.")
        await message.channel.send("...진짜다냥")
    if message.content.startswith(prefix + "짖어") or message.content.startswith(prefix + "울어"):
        await message.channel.send("내가 그깟 집사 말을 들을 것 같냥?!")
        await message.author.send("...야옹")
    if message.content.startswith(prefix + "넌 왜 이름이 윤냥이야"):
        await message.channel.send("내 개인 비서인 네윤의 윤과 냥을 합쳐서 윤냥이다냥!")
    if message.content.startswith(prefix + "너는 왜 이름이 윤냥이야"):
        await message.channel.send("내 개인 비서인 네윤의 윤과 냥을 합쳐서 윤냥이다냥!")
    if message.content.startswith(prefix + "귀여워"):
        await message.channel.send("갸루룽! 기분 좋다냥!")
    if message.content.startswith(prefix + "커여워"):
        await message.channel.send("갸루룽! 기분 좋다냥!")
    if message.content.startswith(prefix + "젤리돌이"):
        await message.channel.send("나를 땅속으로 묻어버리려고 했던 놈이다! 이런 나쁜 놈!")
    if message.content.startswith(prefix + "지니어스"):
        await message.channel.send("나를 아껴주는 집사다냥! 갸루룽!")
    if message.content.startswith(prefix + "바보서진"):
        await message.channel.send("내 비서의 흑역사를 판 나쁜 집사다냥!")
    if message.content.startswith(prefix + "빈센트"):
        await message.channel.send("독보적인 그림체의 소유자인 집사다냥! 나도 그려주면 좋겠다냥...")
    if message.content.startswith(prefix + "주인"):
        await message.channel.send("주인 따윈 없다냥! 단지 개인 비서 네윤이 있을 뿐이다냥!")
    if message.content.startswith(prefix + "야옹"):
        await message.channel.send("내가 그깟 집사 말을 들을 것 같냥?!")
        await message.author.send("...야옹")
    if message.content.startswith(prefix + "잠냥"):
        await message.channel.send("내 친구다냥! 활기찬 성격이 좋다냥!")
    if message.content.startswith(prefix + "고양이"):
        await message.channel.send("내 종족이다냥!")
    if message.content.startswith(prefix + "내온"):
        await message.channel.send("내온이 누구냥?")
    if message.content.startswith(prefix + "내운"):
        await message.channel.send("내 친구 운냥이의 개인 비서다냥!")
    if message.content.startswith(prefix + "운냥"):
        await message.channel.send("내 친구다냥!")
    if message.content.startswith(prefix + "탕"):
        await message.channel.send("꽥! 나를 쏘다니... " + message.author.name + " 집사, 넌 이번 달 월급은 없다!!")
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="나를 쏘다니... ", value="윤냥: 감히 내게...", inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith(prefix + "장르"):
        await message.channel.send("현재 있는 장르다냥!")
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="장르", value="``팝송: 4개`` ``발라드: 3개`` ``힙합: 2개``", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "서버"):
        i = client.guilds
        await message.channel.send(i)

    if message.content.startswith(prefix + "바보"):
        if len(message.content) == 6:
            await message.channel.send("바보라고 말하는 " + message.author.name + " 집사가 바보다냥!")

    if message.content.startswith("샌즈"):
        sanseasteregg = (message.author.name + " 집사, 이스터에그:egg: 를 찾았다냥! 축하한다냥🐾!")
        await message.channel.send(":skull: 샌즈냥! " + message.author.name + " 집사도 아는구냥.")
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="와! 샌즈! ", value=sanseasteregg, inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith("ㅅㅈㅅㄱ"):
        aliveeasteregg = (message.author.name + " 집사, 이스터에그:egg: 를 찾았다냥! 축하한다냥🐾!")
        await message.channel.send(":heart_decoration: ㅅㅈㅅㄱ! " + message.author.name + " 집사, 살아있구냥.")
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="나 살아있어요 ", value=aliveeasteregg, inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith("와! 샌즈!"):
        sanseasteregg = (message.author.name + " 집사, 이스터에그:egg: 를 찾았다냥! 축하한다냥🐾!")
        await message.channel.send(":skull: 샌즈냥! " + message.author.name + " 집사도 아는구냥.")
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="와! 샌즈! ", value=sanseasteregg, inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith("와 샌즈"):
        sanseasteregg = (message.author.name + " 집사, 이스터에그:egg: 를 찾았다냥! 축하한다냥🐾!")
        await message.channel.send(":skull: 샌즈냥! " + message.author.name + " 집사도 아는구냥.")
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="와! 샌즈! ", value=sanseasteregg, inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith("와샌즈"):
        sanseasteregg = (message.author.name + " 집사, 이스터에그:egg: 를 찾았다냥! 축하한다냥🐾!")
        await message.channel.send(":skull: 샌즈냥! " + message.author.name + " 집사도 아는구냥.")
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="와! 샌즈! ", value=sanseasteregg, inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith(prefix + "공격"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="공격 기술은 이런 게 있다냥! ", value="```할퀴기, 내려찍기, 꾹꾹이```", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "채널메시지"):
        if message.author.id == 621555325862150164 or message.channel.permissions_for(message.author).administrator:
            channel = message.content[10:28]
            msg = message.content[29:]
            if channel != 706470473453535293 or channel != 707039177060909056:
                await message.channel.send("해당 채널에는 채널메시지를 보낼 수 없다냥!")
            else:
                await client.get_channel(int(channel)).send(msg)
                await message.channel.send("'" + msg + "'(이)라고 채널메시지를 보냈다냥!")
        else:
            await message.channel.send("채널메시지 기능은 내 개인 비서인 네윤이나 서버의 관리자만 사용할 수 있다냥!")

    if message.content.startswith(prefix + "정보"):
        await message.channel.send(message.author.name + " 집사의 정보다냥!")
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color = 0x00ff00)
        embed.add_field(name="이름:white_check_mark: ", value=message.author.name, inline=False)
        embed.add_field(name="디스플레이 닉네임:grinning:  ", value=message.author.display_name, inline=False)
        embed.add_field(name="가입일:calendar: ", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일 ", inline=False)
        embed.add_field(name="아이디::regional_indicator_i: :regional_indicator_d: ", value=message.author.id, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "도움"):
        embed = discord.Embed(colour = 0x00ff00)
        await message.channel.send("도움말이다냥! " + message.author.name + " 집사, 잘 기억해두라냥!")
        embed.add_field(name = '기본 대화법', value = "``나에게 하고 싶은 말 앞에 '윤냥아'를 붙이라냥! 띄어쓰기 잘 지키라냥!``", inline = False)
        embed.add_field(name="대화 :smile:  ", value="``윤냥아 안녕`` ``윤냥아 반가워`` ``윤냥아 졸려`` ``윤냥아 짖어`` 등등", inline=False)
        embed.add_field(name="채널메시지 :signal_strength:   (이 기능은 서버의 관리자만 쓸 수 있다냥.)", value="``윤냥아 채널메시지 (채널 아이디) (할 말)``", inline=False)
        embed.add_field(name="디엠 :regional_indicator_d: :regional_indicator_m: (디엠의 경우 " + message.author.name + " 집사가 보낸 디엠이라는 것이 뜬다냥.)", value="``윤냥아 디엠 (유저 아이디) (할 말)``", inline=False)
        embed.add_field(name="놀이 :four_leaf_clover:   ", value="``윤냥아 굴려`` ``윤냥아 확률``", inline=False)
        embed.add_field(name="정보 :detective:    ", value="``윤냥아 정보``", inline=False)
        embed.add_field(name="음악 :musical_note:    ", value="``윤냥아 선곡 (장르)`` ``윤냥아 장르``", inline=False)
        await message.channel.send(embed=embed)
        await message.channel.send("각각의 세부설명은 ``윤냥아 설명 (원하는 항목)`` 의 형식으로 입력하면 디엠으로 설명해주겠다냥 ")

    if message.content.startswith(prefix + "설명 대화"):
        embed = discord.Embed(colour = 0x00ff00)
        embed.add_field(name='대화법 :smile:  ', value="`나와 대화할 수 있는 기능이다냥!`` 앞에 '윤냥아'라고 붙이고 입력하면 된다냥!", inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith(prefix + "설명 채널메시지"):
        embed = discord.Embed(colour = 0x00ff00)
        embed.add_field(name='채널메시지 :signal_strength:  ', value="``원하는 채널에 나를 시켜 메시지를 보낼 수 있다냥! ``윤냥아 채널메시지 (채널 아이디) (할 말) 순으로 입력하면 된다냥!``", inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith(prefix + "설명 디엠"):
        embed = discord.Embed(colour = 0x00ff00)
        embed.add_field(name='디엠 :regional_indicator_d: :regional_indicator_m: ', value="원하는 유저한테 디엠을 보내게 시키는 기능이다냥! ``윤냥아 디엠 (유저 아이디) (할 말) 순으로 입력``하면 되고, 디엠을 보내면 받는 유저에게 " + message.author.name + " 집사가 보낸 디엠이라는 것이 뜬다냥!", inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith(prefix + "설명 놀이"):
        embed = discord.Embed(colour = 0x00ff00)
        embed.add_field(name='놀이 :four_leaf_clover: ', value="오락 기능이다냥! 자세한 설명은 밑을 봐라냥!", inline=False)
        embed.add_field(name='주사위', value="``윤냥아 주사위`` 로 실행시킬 수 있으며, 1~6까지의 수를 뽑아준다냥!", inline=True)
        embed.add_field(name='확률', value="``윤냥아 확률`` 로 실행시킬 수 있으며, 내가 1~100까지의 수를 뽑아주는데, 77이 뽑히면 당첨이다냥!", inline=True)
        await message.author.send(embed=embed)

    if message.content.startswith(prefix + "설명 정보"):
        embed = discord.Embed(colour=0x00ff00)
        embed.add_field(name='정보 :detective: ', value="``윤냥아 정보``로 실행시킬 수 있으며, 이름과 디스플레이 닉네임, 가입일, 아이디와 프로필을 알려준다냥!", inline=False)
        await message.author.send(embed=embed)

    if message.content.startswith(prefix + "설명 음악"):
        embed = discord.Embed(colour=0x00ff00)
        embed.add_field(name='음악 :musical_note: ', value="음악 선곡 기능이다냥! 자세한 설명은 밑을 봐라냥!", inline=False)
        embed.add_field(name='선곡', value="``윤냥아 선곡 (장르)`` 로 실행시킬 수 있으며, 선택한 장르의 랜덤한 곡을 하나 선곡해준다냥!", inline=True)
        embed.add_field(name='장르 확인', value="``윤냥아 장르`` 로 실행시킬 수 있으며, 현재 나에게 있는 곡들의 장르의 종류들을 준다냥!", inline=True)
        await message.author.send(embed=embed)

    if message.content.startswith(prefix + "설명"):
        length = message.content
        length = len(length)
        if length < 9:
            await message.channel.send("``윤냥아 설명 (원하는 항목)`` 의 형식으로 입력하라냥!")

    if message.content.startswith(prefix + "확률"):
        percent_value = randint(1, 100)
        embed = discord.Embed(colour=0x00ff00)
        await message.channel.send("77이 뽑히면 잭팟이다냥!")
        embed.add_field(name='1%의 확률!', value=percent_value, inline=False)
        await message.channel.send(embed=embed)
        if percent_value == 77:
            await message.channel.send(message.author.name + " 집사, 대단하다냥! 잭팟이다냥!:moneybag: ")
            luckyguy = (message.author.name + " 집사, 1%의 확률을 뚫다니, 대단하다냥! 이번 달 월급을 올려주겠다냥!")
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name="1%의 확룔!:four_leaf_clover: ", value=luckyguy, inline=False)
            await message.author.send(embed=embed)
        else:
            await message.channel.send(message.author.name + " 집사, 아쉽게도 1%의 확률을 뚫지 못 했다냥...")


    if message.content.startswith(prefix + "굴려"):
        dice_value = randint(1, 6)
        await message.channel.send("주사위를 굴린다냥!")
        if dice_value == 1:
            pic = ("https://discord.com/channels/707757183407751281/707757183852478527/707757358369210391")
        if dice_value == 2:
            pic = ("https://discord.com/channels/707757183407751281/707757183852478527/707757361929912382")
        if dice_value == 3:
            pic = ("https://discord.com/channels/707757183407751281/707757183852478527/707757363800834049")
        if dice_value == 4:
            pic = ("https://discord.com/channels/707757183407751281/707757183852478527/707757368565301248")
        if dice_value == 5:
            pic = ("https://discord.com/channels/707757183407751281/707757183852478527/707757375079055473")
        if dice_value == 6:
            pic = ("https://discord.com/channels/707757183407751281/707757183852478527/707757349468766268")
        embed = discord.Embed(colour=0x00ff00)
        embed.add_field(name='주사위', value=dice_value, inline=False)
        embed.set_thumbnail(url="https://discord.com/channels/707587767130914818/707762913556955216/707762960394878986")
        await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "디엠"):
        author = message.guild.get_member(int(message.content[7:25]))
        msg = message.content[26:]
        await message.channel.send("``" + msg + "``(이)라고 디엠을 보냈다냥!")
        await author.send(message.author.name + " 집사가 보낸 디엠이다냥: " + msg)

    if message.content.startswith(prefix + "선곡"):
        length = message.content
        length = len(length)
        if length < 8:
            await message.channel.send("``윤냥아 선곡 (장르)`` 꼴로 입력하라냥!")
        else:
            if message.content[7:] == ("팝송") or message.content[7:] == ("발라드") or message.content[7:] == ("힙합"):
                if message.content[7:] == ("팝송"):
                    music = randint(1, 4)
                    if music == 1:
                        embed = discord.Embed(colour = 0x00ff00)
                        embed.add_field(name='Artist:paintbrush: ', value="Panic! At The Disco", inline=False)
                        embed.add_field(name='Music:musical_note: ', value="High hopes", inline=False)
                        await message.channel.send(embed=embed)
                        await message.channel.send("https://www.youtube.com/watch?v=IPXIgEAGe4U")
                    if music == 2:
                        embed = discord.Embed(colour = 0x00ff00)
                        embed.add_field(name='Artist:paintbrush: ', value="Lauv", inline=False)
                        embed.add_field(name='Music:musical_note: ', value="Paris in the Rain", inline=False)
                        await message.channel.send(embed=embed)
                        await message.channel.send("https://www.youtube.com/watch?v=kOCkne-Bku4")
                    if music == 3:
                        embed = discord.Embed(colour = 0x00ff00)
                        embed.add_field(name='Artist:paintbrush: ', value="The Strumbellas", inline=False)
                        embed.add_field(name='Music:musical_note: ', value="Spirits", inline=False)
                        await message.channel.send(embed=embed)
                        await message.channel.send("https://www.youtube.com/watch?v=F9kXstb9FF4")
                    if music == 4:
                        embed = discord.Embed(colour = 0x00ff00)
                        embed.add_field(name='Artist:paintbrush: ', value="Loving Caliber", inline=False)
                        embed.add_field(name='Music:musical_note: ', value="I want you now", inline=False)
                        await message.channel.send(embed=embed)
                        await message.channel.send("https://www.youtube.com/watch?v=fuogdUt12Bw")
                if message.content[7:] == ("발라드"):
                    music = randint(1, 3)
                    if music == 1:
                        embed = discord.Embed(colour = 0x00ff00)
                        embed.add_field(name='Artist:paintbrush: ', value="황인욱", inline=False)
                        embed.add_field(name='Music:musical_note: ', value="포장마차", inline=False)
                        await message.channel.send(embed=embed)
                        await message.channel.send("https://www.youtube.com/watch?v=Hi0skksGeRk")
                    if music == 2:
                        embed = discord.Embed(colour = 0x00ff00)
                        embed.add_field(name='Artist:paintbrush: ', value="폴킴", inline=False)
                        embed.add_field(name='Music:musical_note: ', value="안녕 (호텔 델루나 OST)", inline=False)
                        await message.channel.send(embed=embed)
                        await message.channel.send("https://www.youtube.com/watch?v=_niSIiVMEos")
                    if music == 3:
                        embed = discord.Embed(colour = 0x00ff00)
                        embed.add_field(name='Artist:paintbrush: ', value="십센치(10cm)", inline=False)
                        embed.add_field(name='Music:musical_note: ', value="스토커", inline=False)
                        await message.channel.send(embed=embed)
                        await message.channel.send("https://www.youtube.com/watch?v=Iu-NVopNDKU")
                if message.content[7:] == ("힙합"):
                     music = randint(1, 2)
                     if music == 1:
                        embed = discord.Embed(colour=0x00ff00)
                        embed.add_field(name='Artist:paintbrush: ', value="김하온", inline=False)
                        embed.add_field(name='Music:musical_note: ', value="꽃", inline=False)
                        await message.channel.send(embed=embed)
                        await message.channel.send("https://www.youtube.com/watch?v=i5ipWolnryQ")
                     if music == 2:
                        embed = discord.Embed(colour=0x00ff00)
                        embed.add_field(name='Artist:paintbrush: ', value="빈첸", inline=False)
                        embed.add_field(name='Music:musical_note: ', value="텅", inline=False)
                        await message.channel.send(embed=embed)
                        await message.channel.send("https://www.youtube.com/watch?v=Z-6yEiarxbQ")

            else:
                nogenre = message.content[7:]
                await message.channel.send("``" + nogenre + "`` (이)라는 장르는 없다냥!")



client.run("NzA4MTY3MjM1NDE5NTA0NjYw.XrplNQ.dN3eSp2opW6E1fiTkGzIUp44Zao")