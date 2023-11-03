# 환경 확인
- 이미 설치된 CUDA, 가상환경 등을 점검.
- 설치하려고 하는 버전보다 최신 버전이 설치되어 있으면 삭제.
- 가상환경이 이미 조성되어 있다면 살펴보고, 시도해본 뒤 새로 만들지 결정.

# CUDA 설치
- [텐서플로우 버전 확인](https://www.tensorflow.org/install/source_windows?hl=ko)
- 위 사이트에서 필요한 버전을 확인한다.
- tensorflow_gpu는 2.5.0부터 2.10.0까지 cuDNN 8.1버전, CUDA 11.2버전을 사용한다.
- [CUDA 11.2](https://developer.nvidia.com/cuda-11.2.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork)
- Windows -> x86_64 -> 10 -> exe(network or local)
  - 인터넷이 되지 않는 장비로 이동해서 설치할 것 아니면 network가 편하다.

# cuDNN
- [cuDNN 모음](https://developer.nvidia.com/rdp/cudnn-archive)
- Download cuDNN v8.1.1 (Feburary 26th, 2021), for CUDA 11.0,11.1 and 11.2 
- cuDNN Library for Windows (x86) 설치

# 중간 점검
- CUDA 11.2 버전을 설치하였는가?
- cudnn-11.2-windows-x64-v8.1.1.33.zip 파일을 확인하였는가?
- ANACONDA.NAVIGATOR가 있는가?
- 모두 확인했다면 설치된 CUDA를 시스템에 적용하기 위해 재부팅한다.

# 적용 단계
- cudnn-11.2-windows-x64-v8.1.1.33.zip의 압축을 푼다.
- CUDA 폴더에 붙여넣는다. 
- bin include lib을 환경변수에 등록한다.
- Anaconda navigator에서 tensorflow-gpu를 받는다. 2.6.0 버전.
  

![완성](https://user-images.githubusercontent.com/82266289/234044575-a4c9c559-925e-4982-b620-09637d872e44.png)
