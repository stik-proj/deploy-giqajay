import os
import random
from datetime import datetime
from git import Repo, GitCommandError
import time

# 깃 저장소 경로
repo_path = "/Users/gilbert/workspace/staika/deploy-giqajay"

# 깃헙 개인 접근 토큰
access_token = "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"

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def generate_word():
    word = ''
    length = random.randint(4, 8)  # 단어 길이는 4~8자리로 설정
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)
    return word

while True:
    # 현재 시간을 파일 이름으로 지정
    #now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = "2023-04-10-20-18-07.txt"

    # 파일 생성
    with open(filename, "w") as f:
        f.write(generate_word())

    try:
        # 깃 저장소 객체 생성
        repo = Repo(repo_path)

        # 변경된 파일 추가
        repo.git.add(filename)

        # 변경 내용을 커밋
        commit_message = f"Added {generate_word()}"
        repo.index.commit(commit_message)

        # 깃헙으로 변경 내용을 푸시
        origin = repo.remote(name="origin")
        url = f"https://{access_token}@github.com/stik-proj/deploy-giqajay.git"
        origin.set_url(url)
        origin.push()
        print(f"{url} commit successfully.")

    except GitCommandError as e:
        print(f"An error occurred: {e}")

    # 10 대기
    time.sleep(10)
