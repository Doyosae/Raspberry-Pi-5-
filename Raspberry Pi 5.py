from gpiozero import LED   # 라즈베리 파이 GPIO 제어를 위한 라이브러리
from time import sleep     # 시간 지연을 위한 라이브러리


# 차량용 신호등 (3색)
carLedRed = 2       # 차량용 빨강: GPIO 2
carLedYellow = 3    # 차량용 노랑: GPIO 3
carLedGreen = 4     # 차량용 초록: GPIO 4


# 보행자용 신호등 (2색)
humanLedRed = 20    # 보행자용 빨강: GPIO 20
humanLedGreen = 21  # 보행자용 초록: GPIO 21


# LED 객체 설정
carLedRed = LED(2)
carLedYellow = LED(3)
carLedGreen = LED(4)
humanLedRed = LED(20)
humanLedGreen = LED(21)


try:
    while 1:		            # 단계 1 : 차량 통행 / 보행자 정지 상태
        carLedRed.value = 0
        carLedYellow.value = 0
        carLedGreen.value = 1    # 차량 초록등 점등
        humanLedRed.value = 1    # 보행자 빨간등 점등 (대기)
        humanLedGreen.value = 0
        sleep(3.0)               # 3초간 유지

        # 단계 2 : 차량 정지 예고 (황색 신호 전환)
        carLedRed.value = 0
        carLedYellow.value = 1    # 차량 노란등 점등 (주의)
        carLedGreen.value = 0
        humanLedRed.value = 1    # 보행자 신호는 여전히 빨간등 유지
        humanLedGreen.value = 0
        sleep(1.0)               # 1초간 유지

        # 단계 3 : 차량 정지 / 보행자 통행 상태
        carLedRed.value = 1       # 차량 빨간등 점등 (정지)
        carLedYellow.value = 0
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 1   # 보행자 초록등 점등 (통행 가능)
        sleep(3.0)                # 3초간 유지


except KeyboardInterrupt:          # 사용자가 Ctrl+C로 프로그램을 종료할 때 실행되는 예외 처리
    pass



# 시스템 종료 시 안전 모드 
# 모든 LED를 소등하여 과전류를 방지하고 하드웨어를 보호함
carLedRed.value = 0
carLedYellow = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0