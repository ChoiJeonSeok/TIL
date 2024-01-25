# 컨텍스트 매니저 (Context Managers) `with` 문

#### 예외 발생 시에도 리소스가 안전하게 해제되는 것을 보장하는 효과적인 방법.

## 컨텍스트 매니저의 핵심 개념
1. **`__enter__`와 `__exit__` 메소드**: 컨텍스트 매니저는 이 두 매직 메소드를 구현한다. `__enter__` 메소드는 리소스가 생성되거나 할당될 때 호출되고, `__exit__` 메소드는 리소스가 더 이상 필요하지 않을 때 호출되어 리소스를 해제한다.

2. **`with` 문의 사용**: `with` 문은 컨텍스트 매니저를 사용하여 리소스를 안전하게 관리한다. `with` 블록 내에서 리소스를 사용하고, 블록을 벗어나면 자동으로 리소스가 해제된다.

3. **다양한 용도**: 컨텍스트 매니저는 파일 처리, 데이터베이스 연결, 네트워크 세션 관리 등 다양한 리소스 관리에 활용될 수 있다.

#### 추가적인 정보: `contextlib` 모듈과 `contextmanager` 데코레이터
- **`contextlib` 모듈**: 이 모듈은 컨텍스트 매니저를 쉽게 작성할 수 있도록 도와주는 도구를 제공한다.
- **`contextmanager` 데코레이터**: 이 데코레이터를 사용하면 제너레이터를 기반으로 한 컨텍스트 매니저를 간편하게 작성할 수 있다. `yield`를 사용하여 리소스를 관리하고, `yield` 이후의 코드는 리소스 해제를 처리한다.

#### 파일 처리 예시
```python
with open('file.txt', 'r') as file:
    contents = file.read()
```
- 이 예시에서 `with` 문은 파일을 열고, 파일 객체를 컨텍스트 매니저로 사용한다. 블록이 끝나면 파일이 자동으로 닫힌다.

#### 컨텍스트 매니저 작성 예시
```python
from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwargs):
    resource = acquire_resource(*args, **kwargs)
    try:
        yield resource
    finally:
        release_resource(resource)

with managed_resource() as resource:
    # 리소스를 사용하는 코드
    ...
```
- 이 예시에서 `managed_resource` 함수는 `contextmanager` 데코레이터를 사용하여 컨텍스트 매니저로 정의된다.

