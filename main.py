# discord 라이브러리 사용 선언
import discord
import re
import random

member = ['구경꾼', '인천막걸뤼', '초보반선생님']
ready_match = False

class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, Activity
        game = discord.Game("랜덤 매칭 봇")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        global ready_match
        text = ''
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        # message.author.bot = message의 author가 bot이냐 아니냐를 질의하여 True or False로 표시
        # 즉, if는 True일 때 : 밑에 들여쓰기 된 내용을 시행하므로, author가 Bot일 경우 아래의 코드를 실행
        if message.author.bot:
            return None

        # message.content = message의 내용
        # == "!바보" = 왼쪽의 값이 "!바보"와 완벽 일치하면 True, 아니면 False를 리턴

        if ready_match == True:
            channel = message.channel
            # 팀원 string 입력 ( 정규식 사용, ',' 자르기 )
            member_list = re.split(',', message.content)
            random.shuffle(member_list)
            num_member = len(member_list)

            text += f'참가인원 수 : {num_member}명\n A팀\t\tB팀\n'

            for i in range(int(num_member/2)):
                text += f'{member_list[i*2]}\t\t{member_list[(i*2)+1]}\n'

            await channel.send(text)
            ready_match = False

        if message.content == "!매치":
            channel = message.channel
            await channel.send("팀원입력을 입력하세요")
            ready_match = True

            return None

# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 클래스 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run("Nzk4NTU3ODU3MjIwOTE5Mjk2.X_2w9Q.h8VPTWhLJlUaostl4KSFT1lm1ew")