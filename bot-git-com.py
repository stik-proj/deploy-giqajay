import os
import git
import time

# 깃허브 레포지토리의 URL과 토큰 설정
git_url = "https://github.com/stik-proj/deploy-giqajay.git"
token = "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"

# git 레포지토리
repo = git.Repo("/Users/gilbert/workspace/staika/deploy-giqajay")

# origin을 토큰을 이용한 권한으로 설정
origins = repo.remote(name='origin')
print(origins.url)

origin_url = git_url.replace("https://", f"https://{token}@")
origins.set_url(origin_url)

while True:
    try:
        # 변경 내용 추가
        repo.index.add("*")

        # 커밋 메시지 설정
        commit_message = "Auto commit at " + time.strftime('%Y-%m-%d %H:%M:%S')

        # 커밋 생성
        repo.index.commit(commit_message)

        # 깃허브 레포지토리로 push
        origin.push()
        print(f"Committed successfully at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"Commit failed at {time.strftime('%Y-%m-%d %H:%M:%S')}: {e}")

    # 5분 대기
    time.sleep(300)
