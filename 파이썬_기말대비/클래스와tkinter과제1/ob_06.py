'''노래 플레이리스트
1. Playlist 클래스 정의
- 멤버: name(노래명), tracks(리스트, 기본 빈 리스트)
- 생성자에서 이름 초기화
2. add(track)로 곡 추가
3. count()로 곡 개수 반환
4. show()로 "플리명: MyList, 곡 수: 2, 곡들: [A, B]" 형식 문자열 반환
pl = Playlist("MyList")
pl.add("Dynamite"); pl.add("Butter")
print(pl.show())  # 플리명: MyList, 곡 수: 2, 곡들: [Dynamite, Butter]
'''
class Playlist:
  def __init__(self, name):
    self.name = name        # 플레이리스트 이름
    self.tracks = []        # 곡 목록 초기화

  def add(self, track):
    self.tracks.append(track)   # 곡 추가

  def count(self):
    return len(self.tracks)     # 곡 개수 반환

  def show(self):
    return f"플리명: {self.name}, 곡 수: {self.count()}, 곡들: {self.tracks}"

pl = Playlist("MyList")
pl.add("Dynamite")
pl.add("Butter")
print(pl.show())  # 플리명: MyList, 곡 수: 2, 곡들: [Dynamite, Butter]