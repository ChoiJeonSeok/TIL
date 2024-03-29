# 애플리케이션 개발 중에 안전하게 아이디 및 비밀번호를 관리하는 방법

## 1. 코드에 직접 삽입
- **설명**: 아이디와 비밀번호를 소스 코드 내에 직접 작성한다.
- **장점**: 개발이 간단하고 코드를 쉽게 이해할 수 있다.
- **단점**: 코드가 유출되면 모든 정보가 노출된다. 유지 보수가 어렵다.
- **적합한 상황**: 작은 개인 프로젝트나 보안이 크게 중요하지 않은 정보를 다룰 때.
- **예시**: `password = "mypassword123"`를 직접 코드에 삽입.

## 2. 외부 파일 사용
- **설명**: 아이디와 비밀번호를 별도의 파일(예: `.env` 파일)에 저장하고, 코드에서 이를 읽어 사용한다.
- **장점**: 코드와 분리되어 있어 보안성이 향상된다. 환경별로 다른 설정을 쉽게 적용할 수 있다.
- **단점**: 파일 자체의 보안을 유지해야 하며, 파일 관리가 필요하다.
- **적합한 상황**: 다양한 환경에서 다른 설정을 적용해야 할 때.
- **예시**:
  - `.env` 파일에 `DB_PASSWORD=mypassword123`를 저장.
  - 코드에서는 `dotenv` 라이브러리를 사용하여 이 값을 불러온다.
  - `.txt` 파일에 있는 경우 직접 읽어서 변수에 값을 저장한 후 사용할수 있다.

## 3. 환경 변수 사용
- **설명**: 아이디와 비밀번호를 시스템의 환경 변수에 저장하고, 코드에서 이를 불러 사용한다.
- **장점**: 코드와 완전히 분리되어 있어 가장 안전하다. 환경에 따른 유연한 설정 변경이 가능하다.
- **단점**: 초기 설정이 복잡할 수 있으며, 운영 체제나 호스팅 환경에 따라 다를 수 있다.
- **적합한 상황**: 클라우드 서비스나 컨테이너 기반 배포를 사용하는 대규모 애플리케이션.
- **예시**:
  - 리눅스에서 `export DB_PASSWORD=mypassword123`로 환경 변수를 설정.
  - 파이썬 코드에서는 `os.environ.get('DB_PASSWORD')`를 사용하여 값을 불러온다.