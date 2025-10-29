import tkinter as tk
from PIL import ImageTk, Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   #현재 실행하는 파이썬 파일이 있는 절대 경로를 구해 BASE_DIR 변수에 저장

def update_image():
    global current_index

    image_path = os.path.join(BASE_DIR, image_files[current_index])
    
    image = Image.open(image_path)  #이미지 파일 열기

    image = image.resize((400, 300))    #이미지 리사이즈
    
    photo = ImageTk.PhotoImage(image)   #리사이즈된 이미지를 tkinter에서 표시할 수 있는 객체로 변환
 
    image_label.config(image=photo)
    image_label.image = photo

    current_index = (current_index + 1) % len(image_files)  #인덱스 1증가, 끝 도달하면 0으로 돌아감
    root.after(interval, update_image)  #지정한 시간 후에 함수 다시 호출해 반복 실행

root = tk.Tk()
root.title("Image Slider")  #윈도우 제목 설정

#이미지 파일 이름 리스트
image_files = ["image1.png", "image2.png", "image3.png", "image4.png"]

interval = 2000     #시간지정
current_index = 0   #보여줄 이미지 인덱스 초기값

image_label = tk.Label(root)
image_label.pack()

update_image()  #이미지 표시 및 슬라이드 동작 시작


root.mainloop()