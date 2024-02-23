# **BAT 파일**
- BAT 파일은 "Batch"의 약자로, 여러 명령어들을 순차적으로 실행할 수 있는 스크립트 파일이다. 
- 윈도우 운영 체제에서 사용되며, 사용자가 반복적으로 수행해야 하는 작업을 자동화하는 데 유용하다. 
- 텍스트 편집기를 사용하여 작성하고, `.bat` 확장자로 저장한다.

### **BAT 파일의 특징:**
- **간단한 구조:** 명령 프롬프트에서 실행할 수 있는 명령어들을 순서대로 나열한다.
- **자동화:** 일련의 작업을 자동으로 수행하게 할 수 있다.
- **윈도우 환경 지원:** BAT 파일은 윈도우에서만 사용할 수 있다.

**BAT 파일 작성 예시:**
- 다음은 두 개의 파이썬 스크립트를 순차적으로 실행하는 BAT 파일의 예시:

```batch
@echo off
cd C:\WORKSPACE-PYTHON\weather_test
python weather_data_processor.py
timeout /T 5 /nobreak
cd C:\WORKSPACE-PYTHON\weather_test\email
python send_email.py
pause
```

**해당 BAT 파일의 작동 방식:**
1. `@echo off`: 명령어 실행 시 출력되는 메시지를 숨긴다.
2. `cd C:\WORKSPACE-PYTHON\weather_test`: 첫 번째 파이썬 스크립트가 있는 디렉토리로 이동한다.
3. `python weather_data_processor.py`: 첫 번째 파이썬 스크립트를 실행한다.
4. `timeout /T 5 /nobreak`: 5초간 대기한다.
5. `cd C:\WORKSPACE-PYTHON\weather_test\email`: 두 번째 파이썬 스크립트가 있는 디렉토리로 이동한다.
6. `python send_email.py`: 두 번째 파이썬 스크립트를 실행한다.
7. `pause`: 스크립트 실행 후 창이 자동으로 닫히지 않도록 한다.

**BAT 파일 사용 시 유의사항:**
- BAT 파일은 강력한 자동화 도구이지만, 잘못 사용하면 시스템에 해를 끼칠 수 있다.
- 파일 경로나 명령어에 오류가 없는지 주의 깊게 확인해야 한다.
- 보안 문제가 없는지 확인 후 사용해야 한다. 