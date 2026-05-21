import os
from git import Repo, GitCommandError

# 1. 설정 경로
REPO_PATH = os.getcwd()
REMOTE_URL = "https://github.com/yhh2888/Jewel-Protector.git"  # 실제 URL로 변경하세요.

def get_git_user_name(repo):
    """
    현재 Git 설정(git config user.name)에서 사용자 이름을 가져옵니다.
    버전 호환성을 위해 fallback 대신 예외 처리를 사용합니다.
    """
    with repo.config_reader() as reader:
        try:
            # 'user' 섹션의 'name' 값을 가져옴
            user_name = reader.get_value("user", "name")
        except Exception:
            # 값이 설정되어 있지 않아 에러가 나면 None 처리
            user_name = None
        
    if not user_name:
        raise ValueError("Git 'user.name'이 설정되어 있지 않습니다. 터미널에 'git config --global user.name \"이름\"'을 입력해 주세요.")
    
    # 브랜치명 안전 규칙 적용 (공백을 하이픈으로 치환 및 소문자화)
    return user_name.strip().replace(" ", "-").lower()

def setup_branch_by_user_name():
    # 저장소 로드 또는 클론
    if not os.path.exists(REPO_PATH):
        print(f"저장소가 존재하지 않아 클론을 진행합니다: {REMOTE_URL}")
        repo = Repo.clone_from(REMOTE_URL, REPO_PATH)
    else:
        repo = Repo(REPO_PATH)

    # 2. Git config에서 user.name 추출
    try:
        user_name = get_git_user_name(repo)
        branch_name = f"dev/{user_name}"  # 예: dev/alice
        print(f"👤 확인된 Git 사용자: {user_name} -> 생성할 브랜치: {branch_name}")
    except Exception as e:
        print(f"설정 읽기 실패: {e}")
        return

    # 원격 최신화 및 메인 브랜치 이동
    origin = repo.remotes.origin
    origin.fetch()
    
    main_branch = 'main'
    repo.git.checkout(main_branch)
    origin.pull()

    print(f"\n--- {branch_name} 브랜치 생성 및 동기화 시작 ---")

    try:
        # 로컬에 브랜치가 이미 있는지 확인
        if branch_name in repo.heads:
            print(f"이미 로컬에 '{branch_name}' 브랜치가 존재합니다.")
            branch = repo.heads[branch_name]
        else:
            # 메인 브랜치 기반으로 새 브랜치 생성
            print(f"새 브랜치 생성 중: {branch_name}")
            branch = repo.create_head(branch_name, origin.refs[main_branch])
        
        # 브랜치로 전환
        branch.checkout()
        
        # 테스트용 파일 수정 (user.name 사용)
        dummy_file = os.path.join(REPO_PATH, f"{user_name}_workspace.txt")
        with open(dummy_file, "w", encoding="utf-8") as f:
            f.write(f"This is a private workspace for {user_name}.\n")
        
        # 변경사항 스테이징 및 커밋
        repo.index.add([dummy_file])
        if repo.is_dirty():
            repo.index.commit(f"Initialize private workspace for {user_name}")
            print("변경 사항 커밋 완료")
        
        # 원격 저장소로 푸시 및 업스트림 설정
        origin.push(refspec=f"{branch_name}:{branch_name}").raise_if_error()
        print(f"원격 저장소({branch_name}) 푸시 성공!")
        
    except GitCommandError as e:
        print(f"Git 작업 중 에러 발생: {e}")
        
    finally:
        # 안전하게 메인 브랜치로 복귀
        repo.heads[main_branch].checkout()
        print("main 브랜치로 복귀했습니다.")

if __name__ == "__main__":
    setup_branch_by_user_name()