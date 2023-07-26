## 코드의 가독성

1. **적절한 들여쓰기와 라인 브레이크**: 코드가 한 줄에 너무 많은 정보를 담고 있으면 이해하기 어렵다. Python에서는 4 spaces(tab) 들여쓰기를 기본으로 권장하며, 한 줄의 길이는 79자를 넘지 않도록 하는 것이 일반적이라고 한다.

2. **명확한 변수명**: 변수의 이름은 해당 변수가 담고 있는 정보를 잘 설명할 수 있어야 한다. 예를 들어, `list1` 보다는 `student_names`와 같이 의미 있는 이름을 사용하는 것이 좋다.

3. **함수와 클래스에 대한 문서화**: 함수와 클래스 정의 바로 아래에 독스트링(docstring)을 작성하여 해당 함수나 클래스의 역할, 인자, 반환 값 등을 설명하는 것이 중요하다.
    <details> 
    <summary>Docstring 예시</summary>

    Python에서의 독스트링(docstring)은 함수, 클래스, 모듈 등에 대한 설명을 작성하는 데 사용되는 문자열이다. 여기에는 해당 객체의 기능, 인자, 반환 값 등에 대한 정보를 담는다.

    Python의 독스트링은 함수나 클래스의 바로 아래에 작성하며, 작성 방식은 다음과 같다:

    ```python
    def add_numbers(a, b):
        """
        두 숫자를 더하는 함수

        Parameters:
        a (int or float): 첫 번째 숫자
        b (int or float): 두 번째 숫자

        Returns:
        int or float: 두 숫자의 합
        """
        return a + b
    ```
    </details><br>

  
4. **코드에 주석 달기**: 코드의 주요 부분에는 해당 코드가 어떤 역할을 하는지 설명하는 주석을 달아야 한다. 하지만 주석은 최소화하는 것이 좋으며, 주석이 필요 없을 만큼 코드 자체가 명확하게 작성되는 것이 최선이다.

5. **코드의 일관성 유지**: 같은 종류의 작업은 가능한 한 일관된 방식으로 수행되어야 한다. 이는 코드의 패턴을 이해하는 데 도움이 되며, 일관적이지 않은 코드는 이해하기에 시간이 많이 든다.

6. **복잡한 표현식은 피하라**: 너무 복잡한 한 줄 코드는 피하는 것이 좋다. 가독성이 떨어지며, 이해하기 어렵다. 복잡한 표현식은 여러 줄로 나누거나, 적절한 변수명을 사용하여 설명하는 것이 좋다.

    <details>
    <summary>Avoid Complex Expressions</summary>

    ```python
    squared_evens = [n**2 for n in range(100) if n % 2 == 0]
    ```

    ```python
    squared_evens = []
    for n in range(100):
        if n % 2 == 0:
            squared_evens.append(n**2)
    ```
    위 처럼 한 줄로 작성한 것과 아래 4줄은 같다. 간단한 건 리스트 컴프리헨션을 사용하는 것이 좋다고 생각한다. <br>그러나 너무 길게 이어쓰면 직관적으로 이해하기 힘들다. 경우에 따라 맞게 쓰도록 하자.  
    <br>잘못된 리스트 컴프리헨션. 바로 이해하기 어려워 오히려 가독성을 떨어뜨린다.
    ```python
    result = [x * y for x in range(5) for y in range(5) if x * y > 10]
    ```
    </details>
<br>

7. **PEP 8 스타일 가이드를 따르자**: Python의 공식 스타일 가이드로, 코드의 일관성을 유지하고 가독성을 높이는 데 도움이 된다.

    [PEP 8 스타일 가이드](https://github.com/ChoiJeonSeok/TIL/blob/master/etc/Coming_Soon.md)

8. **에러 처리**: 에러가 발생할 확률은 항상 있다고 생각하고, 어떤 에러가 있을 수 있는지 고민해야 한다. Python에서는 try-except 구문을 이용하여 예외를 처리할 수 있다. 
   1. try 블록에서 에러가 발생할 가능성이 있는 코드를 작성한다.
   2. except 블록에서 해당 에러를 어떻게 처리할지를 작성한다. 
   3. 에러 메시지가 예상된다면 `except ZeroDivisionError:` 처럼 직접 적어주면 된다.
   4. 어떤 종류의 에러가 나올지 모른다면 이렇게 적어주면 에러의 내용을 출력한다.
    ```python
    except Exception as e: 
        print("오류가 발생했습니다. : ", e)
    ```
   5. 모든 종류의 에러를 한번에 처리하려고 하지 말고 에러의 종류에 따른 대응을 각기 다르게 하자.

9. **Pythonic한 코드를 작성해보자.**: 다른 언어에서는 하기 어려운 표현들을 Python에서는 할 수 있다. Python의 고유한 기능이니 잘 활용하면 간결하고 가독성 높은 코드를 작성할 수 있다.

    [Pythonic한 코드 작성법](https://github.com/ChoiJeonSeok/TIL/blob/master/Python/Pythonic.md)

10. **코드 리팩토링**: 처음부터 완벽한 코드를 작성하기는 어렵다. 우선 목적에 맞게 코드를 작성한 후 검토하면서 각 부분을 수정하거나 개선하는 것이 좋은 코드를 작성하는 지름길이다. 
    
    [코드 리팩토링 체크리스트](https://github.com/ChoiJeonSeok/TIL/tree/master/etc/Coming_Soon.md)
