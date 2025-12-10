'''
문제 5. 텍스트 파일의 스페이스·대문자·소문자 개수 세기 (파일 다이얼로그 + Tkinter)
1. 기능 / 함수 구조
- count_stats(filename) 함수
- 파일을 한 줄씩 읽으면서 스페이스 ' ' 의 개수(space_cnt), 영문 대문자 개수(upper_cnt), 영문 소문자 개수(lower_cnt)를 센 뒤 (space_cnt, upper_cnt, lower_cnt) 튜플로 반환한다.
- ch == ' ' → 스페이스, ch.isupper() → 대문자, ch.islower() → 소문자
2. 파일 선택 및 예외 처리 요구
- select_file() 함수: filedialog.askopenfilename()를 사용하여 텍스트 파일을 하나 선택한다.
- 사용자가 취소한 경우(경로가 빈 문자열) 함수는 바로 종료한다.
- 선택된 파일 경로를 count_stats()에 전달하여 스페이스 수, 대문자 수, 소문자 수를 받아온다.
- 정상 처리 시 상단 라벨에 선택된 파일과 화면처럼 처리한다.
- 파일 처리 중 오류가 발생할 경우 에러 메시지를 팝업창에 표시한다.
3. Tkinter UI 구성
- 창 제목: "문제5"
- 창 크기: 520×220
- 화면을 참고하여 UI를 구성한다.
4. 학습 포인트
- tkinter.filedialog.askopenfilename()를 이용한 파일 선택 방법.
- 텍스트 파일을 한 줄씩 읽으며 문자 단위로 순회하는 방법(for line in f, for ch in line).
- 문자열 메서드 isupper(), islower()를 활용한 문자 분류.
- Label의 config(text=...)를 사용해 GUI에서 결과를 동적으로 갱신하는 방법.
- try-except와 messagebox.showerror()를 이용해 파일 처리 예외를 사용자에게 알리는 방법.
'''
from tkinter import *
from tkinter import filedialog, messagebox

# 1. 스페이스 / 대문자 / 소문자 개수 세기
def count_stats(filename):
    space_cnt = 0
    upper_cnt = 0
    lower_cnt = 0

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            for ch in line:
                if ch == ' ':
                    space_cnt += 1
                elif ch.isupper():
                    upper_cnt += 1
                elif ch.islower():
                    lower_cnt += 1
    return space_cnt, upper_cnt, lower_cnt

# 2. 파일 선택 버튼 이벤트
def select_file():
    filepath = filedialog.askopenfilename(
        title="파일을 선택하세요",
        filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
    )
    if not filepath:   # 사용자가 취소하면 종료
        return
    try:
        space_cnt, upper_cnt, lower_cnt = count_stats(filepath)

        file_label.config(text=f"선택된 파일: {filepath}")
        result_label.config(text=f"스페이스: {space_cnt}, 대문자: {upper_cnt}, 소문자: {lower_cnt}")
    except Exception as e:
        messagebox.showerror("에러", f"파일을 처리하는 중 오류가 발생했습니다.\n{e}")

# 3. Tkinter GUI
root = Tk()
root.title("문제5")
root.geometry("520x220")

Label(root, text="텍스트 파일을 선택하여 스페이스, 대문자, 소문자 개수를 세어보세요.").pack(pady=10)

Button(root, text="파일 선택", command=select_file).pack(pady=5)

file_label = Label(root, text="선택된 파일: (없음)")
file_label.pack(pady=5)

result_label = Label(root, text="스페이스: 0, 대문자: 0, 소문자: 0")
result_label.pack(pady=10)

root.mainloop()