# boto3

- boto3는 AWS(Amazon Web Services) 서비스를 Python으로 작업할 수 있게 해주는 AWS SDK(Software Development Kit)이다. 
- SDK는 AWS 리소스와 상호작용하는 데 필요한 다양한 기능들을 제공한다. 
- boto3를 사용하면 S3, Lambda, DynamoDB 등과 같은 AWS 서비스를 프로그래매틱하게 제어할 수 있다.

### boto3의 핵심 구성요소

1. **클라이언트(Client)**와 **리소스(Resource)**: 
   - boto3는 클라이언트와 리소스 두 가지 형태의 서비스 액세스를 제공한다. 
   - 클라이언트는 저수준의 서비스 액세스를 제공하며, 리소스는 더 높은 수준의 객체 지향적 서비스 액세스를 제공한다. 
   - 리소스는 클라이언트를 내부적으로 사용하지만, 더 추상화된 방식으로 서비스와 상호작용합니다.

2. **세션(Session)**: 
   - AWS의 자격증명과 설정을 관리하고 AWS 서비스에 연결한다.

### S3와의 상호작용
- Amazon S3는 스케일링이 가능한 객체 스토리지 서비스.
- boto3를 사용하여 S3 버킷을 생성, 조회, 삭제하는 것이 가능하다. 
- 예를 들면 파일을 업로드하거나 다운로드, 버킷 내 객체 리스트를 조회하는 것 등.

### AWS Lambda와의 상호작용
- AWS Lambda는 서버리스 컴퓨팅 서비스로, 서버 관리 없이 코드를 실행할 수 있게 해준다. 
- boto3를 이용하여 Lambda 함수를 생성하고 관리할 수 있다. 
- 예를 들면 새로운 Lambda 함수를 생성하거나 기존 함수를 업데이트하는 등의 작업을 할 수 있다.

### boto3 설치 및 사용에는 Python 3.8 이상 필요.

### 예제: S3 버킷 생성
- 버킷 이름은 전 세계적으로 유일해야 하며, 특정 리전을 명시적으로 정의할 필요가 있다. 


```python
import boto3
import uuid

def create_bucket_name(bucket_prefix):
    # 버킷 이름 생성
    return ''.join([bucket_prefix, str(uuid.uuid4())])

s3_resource = boto3.resource('s3')
bucket_name = create_bucket_name('my-bucket-prefix')
region = 'ap-northeast-2'  # 예시 리전

# 버킷 생성
s3_resource.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': region}
)
```

- 이 코드는 고유한 버킷 이름을 생성하고, 지정된 리전에 버킷을 생성한다. 
- 여기서 `uuid` 라이브러리는 고유한 이름을 생성하는 데 사용된다.

### boto3 사용 시 주의사항
- **보안**: AWS 자격증명을 안전하게 관리해야 한다. 적절한 권한을 가진 IAM 사용자 또는 역할을 생성하고, 그 자격증명을 사용하는 것이 중요하다.
- **비용**: AWS 서비스 사용에는 비용이 발생할 수 있다. 