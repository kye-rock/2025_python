'''문제 1.
텍스트 파일을 열고 내용을 읽어서 화면에 출력하는 프로그램을 작성하시오.
파일을 열 때 발생할 수 있는 예외(FileNotFoundError)를 처리하는 코드를 추가해 본다.
'''
def read_file(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

filename = input("텍스트 파일 이름을 입력하세요: ")
read_file(filename)