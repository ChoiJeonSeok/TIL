# 로컬 환경의 코드를 AWS 환경으로 마이그레이션 하는 과정

- 이 계획은 AWS 서비스를 활용하여 기존의 로컬 환경에서 실행되는 날씨 데이터 처리 및 이메일 전송 프로세스를 클라우드 기반으로 전환하는 것을 목표로 한다.

### 1. AWS 서비스 선정 및 구성
- **AWS Lambda**: 서버리스 컴퓨팅 서비스로, 날씨 데이터를 처리하고 보고서를 생성하는 Python 스크립트를 실행한다.
- **Amazon S3**: 날씨 데이터 파일, 보고서, 로그 파일을 저장하는데 사용된다.
- **Amazon SES (Simple Email Service)**: 이메일 전송에 사용된다. 서비스가 확장되기 전까지는 Gmail SMTP를 계속 사용할 예정이지만, SES를 사용한다고 가정하여 학습을 이어갈 것이다.
- **IAM (Identity and Access Management)**: Lambda, S3, SES에 대한 접근 및 실행 권한을 관리한다.

### 2. 코드 수정 및 최적화
- **Lambda 호환성**: Lambda에서 실행될 수 있도록 코드를 수정해야 한다. 예를 들어, 파일 경로, 환경 변수 등을 Lambda 환경에 맞게 조정해야 한다.
- **S3 통합**: 날씨 데이터와 보고서 파일을 S3 버킷에 저장하고 불러오도록 코드를 수정한다.
- **SES 통합**: 이메일 전송 코드를 Amazon SES를 사용하도록 변경한다.

### 3. Lambda 함수 배포
- **패키지 생성**: 필요한 모든 코드와 라이브러리를 포함하는 Lambda 배포 패키지를 생성한다.
- **함수 생성 및 설정**: AWS Lambda에서 새로운 함수를 생성하고, 트리거, 메모리, 타임아웃 등을 설정한다.

### 4. S3 버킷 설정
- **버킷 생성**: 데이터, 보고서, 로그 파일을 위한 S3 버킷을 생성한다.
- **권한 설정**: Lambda 함수가 S3 버킷에 접근할 수 있도록 IAM 역할을 설정한다.

### 5. SES 설정
- **이메일 주소 인증**: Amazon SES에서 발신자 및 수신자 이메일 주소를 인증한다.
- **Lambda와 통합**: SES를 사용하여 이메일을 전송하는 코드를 Lambda 함수에 통합한다.

### 6. IAM 역할 및 정책 설정
- **역할 생성**: Lambda 함수가 S3와 SES에 접근할 수 있도록 필요한 권한을 가진 IAM 역할을 생성한다.
- **정책 설정**: S3 버킷 접근, SES 이메일 전송 등에 필요한 정책을 역할에 연결한다.

### 7. 테스트 및 최적화
- **단위 테스트**: 개별 Lambda 함수를 테스트하여 기능이 정상적으로 작동하는지 확인한다.
- **통합 테스트**: 전체 프로세스가 예상대로 작동하는지 테스트한다.
- **성능 최적화**: 필요에 따라 메모리, 실행 시간 등을 조정한다.

### 8. 모니터링 및 유지보수
- **CloudWatch 로그**: Lambda 실행 로그 및 에러 로그를 모니터링한다.
- **유지보수**: 필요에 따라 코드를 업데이트하고 시스템을 유지보수한다.