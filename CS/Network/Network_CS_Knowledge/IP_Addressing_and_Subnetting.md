# IP 주소와 서브넷팅

## IP 주소 형식(IP Address Format)
- IPv4: 32비트로 구성된 4개의 옥텟(8비트)으로 표현된다. 예: 192.168.0.1
- IPv6: 128비트로 구성된 8개의 그룹(16비트)으로 표현된다. 예: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

## IP 주소 클래스(IP Address Classes)
- A 클래스: 0.0.0.0에서 127.255.255.255까지, 첫 번째 옥텟이 네트워크 식별에 사용된다.
- B 클래스: 128.0.0.0에서 191.255.255.255까지, 첫 번째 두 옥텟이 네트워크 식별에 사용된다.
- C 클래스: 192.0.0.0에서 223.255.255.255까지, 첫 번째 세 옥텟이 네트워크 식별에 사용된다.
- D 클래스: 224.0.0.0에서 239.255.255.255까지, 멀티캐스트 그룹에 할당되는 주소이다.
- E 클래스: 240.0.0.0에서 255.255.255.255까지, 예약된 주소로 사용되며 일반적인 용도에는 사용되지 않는다.

## IP 주소 할당 방법(IP Address Allocation)
- 정적 할당: 수동으로 IP 주소를 할당한다. 관리 용이성이 있으나 대규모 네트워크에서는 번거로울 수 있다.
- 동적 할당: DHCP(Dynamic Host Configuration Protocol)를 사용하여 IP 주소를 동적으로 할당한다. 자동화와 효율성을 제공한다.

## 서브넷 마스크(Subnet Mask)
- 서브넷 마스크는 IP 주소의 네트워크 부분과 호스트 부분을 구분한다.
- 32비트(IPv4) 또는 128비트(IPv6)로 표현되며, 네트워크 식별 비트를 1로, 호스트 식별 비트를 0으로 표시한다.
- 예: 255.255.255.0 (IPv4), ffff:ffff:0000:0000:0000:0000:0000 (IPv6)

## 서브넷팅(Subnetting)
- 서브넷팅은 주어진 IP 주소 범위를 여러 개의 서브넷으로 분할하는 작업이다.
- 서브넷팅을 통해 네트워크를 더 작은 서브넷으로 나누어 IP 주소를 효율적으로 할당하고 네트워크를 관리할 수 있다.
- 서브넷 마스크를 사용하여 서브넷을 구분하며, 각 서브넷은 고유한 네트워크 식별자를 갖는다.
