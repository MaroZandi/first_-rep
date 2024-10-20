import tkinter as tk  # tkinter 모듈 불러오기 및 이름 tk로 변경
import random  # random 모듈 불러오기

root = tk.Tk()  # tk 창 열기
root.geometry("500x500")  # 창 크기 500x500으로 조정
score = 0  # score 변수 선언
time_left = 60  # 60초 타이머 변수 선언 및 값 60으로 지정

def timer():
    global lb5, bt  # lb5,bt 전역 변수 설정
    lb5.destroy()  # 시작 메시지 레이블 삭제
    bt.destroy()  # 시작 버튼 삭제
    
    lb1 = tk.Label(root, width=10, height=2, text="3", font=("Helvetica", 48), fg="red")  # "3" 표시하는 레이블 생성
    lb1.place(x=65, y=180)  # 레이블 위치 설정
    root.after(1000, lambda: (lb1.destroy(), show_lb2()))  # 1초 후 레이블 삭제 및 show_lb2 호출

def show_lb2():
    lb2 = tk.Label(root, width=10, height=2, text="2", font=("Helvetica", 48), fg="orange")  # "2" 표시하는 레이블 생성
    lb2.place(x=65, y=180)  # 레이블 위치 설정
    root.after(1000, lambda: (lb2.destroy(), show_lb3()))  # 1초 후 레이블 삭제 및 show_lb3 호출

def show_lb3():
    lb3 = tk.Label(root, width=10, height=2, text="1", font=("Helvetica", 48), fg="yellow")  # "1" 표시하는 레이블 생성
    lb3.place(x=65, y=180)  # 레이블 위치 설정
    root.after(1000, lambda: (lb3.destroy(), show_lb4()))  # 1초 후 레이블 삭제 및 show_lb4 호출

def show_lb4():
    lb4 = tk.Label(root, width=10, height=2, text="START!", font=("Helvetica", 48), fg="black")  # "START" 표시하는 레이블 생성
    lb4.place(x=65, y=180)  # 레이블 위치 설정
    root.after(500, lambda: (lb4.destroy(), start_game()))  # 0.5초 후 레이블 삭제 및 start_game 호출

def start_game():
    global score, time_left, timer_label # score,time_left,timer_label 전역 변수 설정
    score = 0  # 게임 시작 시 점수 초기화
    time_left = 60  # 타이머 60초로 설정
    move()  # 첫 번째 버튼 이동 호출
    update_timer()  # 타이머 업데이트 시작

def update_timer():
    global time_left, timer_label # time_left, timer_label 전역 변수 설정
    if time_left > 0: # time_left가 0보다 클 경우 실행
        time_left -= 1  # 1초 감소
        timer_label.config(text=f"Time left: {time_left}s")  # 타이머 레이블 업데이트
        root.after(1000, update_timer)  # 1초 후 다시 업데이트 호출
    else: # 그렇지 않다면 실행
        end_game()  # 타이머가 0이 되면 게임 종료

def move(): 
    global score, time_left # score,time_left 전역 변수 설정
    if time_left > 0:  # 타이머가 남아 있을 때만 버튼 이동 및 점수 증가
        score += 1  # 점수 증가
        a = random.randrange(100, 400)  # x좌표 랜덤 생성
        b = random.randrange(50, 450)  # y좌표 랜덤 생성
        button.place(x=a, y=b)  # 버튼의 위치를 랜덤 좌표로 이동
        label.config(text=f"Score: {score}")  # 현재 점수 표시 레이블 업데이트

def end_game():
    button.config(state="disabled")  # 버튼 비활성화
    end_label = tk.Label(root, text=f"Game Over! Your score is {score}", font=("Helvetica", 24), fg="blue")  # 최종 점수 표시 레이블 생성
    end_label.place(x=100, y=200)  # 레이블 위치 설정

button = tk.Button(root, text="CLICK ME!", command=move, font=("Helvetica", 10), bg="cyan", fg="black")  # 클릭 시 move 함수를 호출하는 버튼 생성
button.place_forget()  # 시작 전 버튼 숨기기

lb5 = tk.Label(root, text="PRESS BUTTON TO START", font=("Helvetica", 18), fg="black")  # 시작 메시지 레이블 생성
lb5.place(x=100, y=200)  # 시작 메시지 레이블 위치 설정
bt = tk.Button(root, text="START", command=timer, font=("Helvetica", 18), bg="lightgreen", fg="black")  # 클릭 시 timer 함수를 호출하는 시작 버튼 생성
bt.place(x=200, y=250)  # 시작 버튼 위치 설정

label = tk.Label(root, text=f"Score: {score}", font=("Helvetica", 18), fg="black")  # 점수 표시 레이블 생성
label.place(x=10, y=10)  # 점수 레이블 위치 설정

timer_label = tk.Label(root, text=f"Time left: {time_left}s", font=("Helvetica", 18), fg="black")  # 타이머 표시 레이블 생성
timer_label.place(x=350, y=10)  # 타이머 레이블 위치 설정

root.mainloop()  # tkinter 이벤트 루프 시작