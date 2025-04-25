# Downloader
유튜브 영상을 빠르게 다운로드

## 시작하기 전
- Python 3+
- [ffmpeg](https://ffmpeg.org/)

### 파이썬 세팅
```bat
pip install yt-dlp
pip install termcolor
```

위 두 명령어를 실행하지 않으면 당연하게도 오류가 발생합니다.

### ffmpeg
`C:\ffmpeg`에 다운로드 받은 모든 파일을 옮기고, 시스템 환경변수 `Path`에 `C:\ffmpeg\bin` 을 추가하세요.

## 실행하기
```bat
py downloader.py
```

이 명령어를 입력한 이후 파일에서 시키는대로 입력하기만 하면 됩니다.

## 화질
- 144p
- 240p
- 360p
- 480p
- 720p
- 1080p
- 1440p
- 4K
- 8K

위 4개화질을 지원합니다.

## 다운로드되는 비디오/오디오
- 비디오+오디오 통합(영상 전체)
- 비디오 한정
- 오디오 한정

@ 주의사항 : 자막은 다운로드되지 않습니다. @
