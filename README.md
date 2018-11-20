# 2018-2 객체지향 프로그래밍 프로젝트 - **{Leftovers}**
구성원: 2-1 연제호 | 2-1 최호영 | 2-6 장영웅

## 1. 주제
온라인 정치 게임 : 상대평가 (와글와글 던전을 베이스로 한 2차 창작 게임)

## 2. 동기
 인간관계, 그리고 정치는 생각 외로 우리 삶에서 매우 중요한 역할을 한다. 어떤 직업을 얻어서 기업에서 근무하던, 군대를 가던, 아니면 당장 지금, 고등학교에서도 인간관계와 정치는 우리 삶과 매우 밀접한 관계에 있다. 하지만 이러한 "정치"를 체험할 수 있는 것은, 역할이 지정되어 경우의 수가 한정된 마피아 게임이라던가, 쉽게 접하기 힘든 더 지니어스 류 게임들 밖에 없다. 따라서 조금 더 쉽게 정치를 체험해볼 수 있는 게임을 제작하고자 본 프로젝트를 시작하였다. 낮은 진입장벽과 자유로운 역할, 정치와 적당한 수 싸움이 포함된 게임의 형태로 제작하고자 하였다.

## 3. 프로그램 사용 대상
 프로그램 사용 대상은 특정적이지 않다. 룰이 매우 간단하여 컴퓨터만 있다면 쉽게 플레이가 가능하다. 다만 게임을 효율적으로 플레이하기 위해서는 채팅방 시스템을 통한 정치가 필수적인데, 이를 위해서는 어느 정도의 연령이 필요하다. 마피아 게임보다 쉽게 즐길 수 있으며, 이와 같은 류의 게임에 흥미가 있는 사람들이 프로그램 사용 대상이라고 볼 수 있을 것 같다.

## 4. 목적
 기본 목적은 젠가 게임을 프로그래밍을 통해 구현하는 것이다. 젠가 게임은 나무로 만든 직육면체 형태의 블록이 쌓여 만들어진 기둥에서, 여러 명의 플레이어가 순서를 번갈아가면서 기둥을 넘어뜨리지 않게 블록을 하나씩 빼는 게임이다. 이 때 기둥이 넘어지는지 여부를 결정하는 것은 크게 기둥의 무게중심과, 각 블록에 작용하는 중력과 마찰력이다. 따라서 이러한 물리적 요소를 보여줄 수 있는 프로그램을 제작하는 것을 목적으로 한다.
  우선 본 프로그램의 기본 형태는 네트워킹을 이용하여 여러 명의 플레이어가 서버에 접속한 후 동시에 젠가 게임을 플레이하는 것이다. 이 때의 젠가 기둥의 형태는 시각적으로 드러난다. 여기에 추가적으로 젠가 기둥에 영향을 주는 물리적 요소(마찰력이나 무게중심)의 상태가 동시에 출력된다.

## 5. 주요기능
{기본 게임 로직, 게임 인원 간 전체채팅 기능, 그룹채팅 시작 및 종료 기능}

## 6. 프로젝트 핵심
{점수 선택과 채팅을 위한 인터페이스 구현, 게임 인원 간 네트워킹, 게임 로직 구현, 그룹채팅 구현}

## 7. 구현에 필요한 라이브러리나 기술
{pygame, threading, socket...}
네트워킹

## 8. **분업 계획**
연제호 : 
최호영 : 
장영웅 : 

## 9. 기타
<hr>

#### readme 작성관련 참고하기 [바로가기](https://heropy.blog/2017/09/30/markdown/)

#### 예시 계획서 [[예시 1]](https://docs.google.com/document/d/1hcuGhTtmiTUxuBtr3O6ffrSMahKNhEj33woE02V-84U/edit?usp=sharing) | [[예시 2]](https://docs.google.com/document/d/1FmxTZvmrroOW4uZ34Xfyyk9ejrQNx6gtsB6k7zOvHYE/edit?usp=sharing)
