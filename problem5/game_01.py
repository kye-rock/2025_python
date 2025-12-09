from tkinter import*
import random
import time

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)  #도형 ID
        self.paddle = paddle
        self.canvas.move(self.id, 245, 100) #공의 초기 위치 지정

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)      #리스트 순서를 섞기
        self.x = starts[0]      #섞인 리스트의 첫 번째 값을 사용
        

        self.y = -3     #y 방향은 위로 -3 속도로 시작

        #캔버스 높이 저장
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    #공이 패들에 부딪혔는지 검사하는 함수
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)       #현재 공의 위치 가져오기 [x1, y1, x2, y2]
        #print(self.canvas.coords(self.id))

        if pos[1] <= 0:     #천장에 닿음 -> 아래로 방향 전환
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        if pos[0] <= 0:     #왼쪽 벽에 닿으면 -> 오른쪽으로 튕김
            self.x = 3

        if pos[2] >= self.canvas_width:     #오른쪽 벽에 닿으면 -> 왼쪽으로 튕김
            self.x = -3

        if not self.hit_bottom:
            if self.hit_paddle(pos) == True:
                self.y = -3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)      #키보드 이벤트 연결
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -4     #왼쪽으로 이동 속도

    def turn_right(self, evt):
        self.x = 4

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0

        elif pos[2] >= self.canvas_width:
            self.x = 0


tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

def restart():
    canvas.delete("all")
    run_game()

def run_game():
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')
        
    while True:
        if ball.hit_bottom == False:
            ball.draw()
            paddle.draw()
        else:
            canvas.create_text(250, 200, text = "GAME OVER", font = ("Helvetica", 30), fill = "red")

            button = Button(tk, text = "새 게임", font = 15, command = restart)
            canvas.create_window(250, 250, window = button) #글자와 버튼도 캔버스의 일부처럼 취급하게 만들기 위해"canvas.create"사용
            break

        tk.update_idletasks()   #tkinter내부 작업 처리
        tk.update()
        time.sleep(0.01)

run_game()
tk.mainloop()