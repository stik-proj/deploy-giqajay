import git
from github import Github
from datetime import datetime, timedelta
import time

# 깃허브 엑세스 토큰
access_token = "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"

# 깃허브 레포지토리 정보
repo_owner = "stik-proj"
repo_name = "deploy-giqajay"

# 레포지토리 클론
local_repo_path = "/Users/gilbert/workspace/staika/deploy-test"
git.Repo.clone_from(f"https://github.com/{repo_owner}/{repo_name}.git", local_repo_path)

# 깃허브 API 인증
g = Github(access_token)

# 레포지토리 객체 생성
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# 5분마다 커밋
while True:
    # 파일 수정
    with open(f"{local_repo_path}/example.txt", "a") as f:
        f.write("Committing every 5 minutes\n")

    # 커밋
    repo.git.add(".")
    repo.git.commit("-m", "Automatic commit by Python script")
    origin = repo.remote(name="origin")
    origin.push()

    # 5분 대기
    time.sleep(300)
