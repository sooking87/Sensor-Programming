def circle(radius):
    area = 3.14 * (radius ** 2)
    return area


if __name__ == "__main__":
    area = circle(2)
    print(area)

'''
회원관리 대출 관리 각각의 기능에 대해서 따로 만들어놓았ㄷ. 서로 다른 로직, 파일 구분 -> 그럴때 __main__을 사용한다. 임포트 하는 경우는 함수 및 클래스를 사용한다. 이 패키지를 테스트 하기 위해서 __main__을 사용한다. 
'''
