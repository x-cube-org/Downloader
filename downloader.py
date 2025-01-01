import os;
import yt_dlp;
from termcolor import cprint

def main():
    print("-----------------------------------------------------")
    print("                X-Cube Video Downloader")
    print()
    print("   1   -   오디오 + 비디오 다운로드")
    print("   2   -   오디오만 다운로드")
    print("   3   -   비디오만 다운로드")
    print("   4   -   나가기")
    print()
    print("--------------------------------------------------")
    print()
    mode = input("원하시는 기능에 맞는 숫자를 입력하십시오:       -        ");

    if mode == "1":
        download_av();
    elif mode == "2":
        download_audio();
    elif mode == "3":
        download_video();
    elif mode == "4":
        print("프로그램 종료...");

def download_video():
    cls();
    print("-----------------------------------------------------")
    print("                X-Cube Video Downloader")
    print("                사용해주셔서 감사합니다.")
    print("")
    print("               영상 링크를 입력해주세요.")
    print("--------------------------------------------------")
    print()
    url = input("링크:       -        ");
    resolution_video(url);

def download_audio():
    cls();
    print("-----------------------------------------------------")
    print("                X-Cube Video Downloader")
    print("                사용해주셔서 감사합니다.")
    print("")
    print("               영상 링크를 입력해주세요.")
    print("--------------------------------------------------")
    print()
    url = input("링크:       -        ");
    output_path = "downloads"
    try:
        # 다운로드 폴더 생성
        os.makedirs(output_path, exist_ok=True)
        
        # yt-dlp 옵션 설정 (오디오만 다운로드 -> MP3로 추출)
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  
            'format': 'bestaudio/best',   # 최고 음질 오디오 스트림
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',    # FFmpeg로 오디오 추출
                    'preferredcodec': 'mp3',        # MP3 코덱으로 변환
                    'preferredquality': '192',      # 192kbps
                },
            ],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("오디오(MP3) 다운로드가 완료되었습니다.")
            input("메인 화면으로 이동하려면 엔터를 누르세요.")
            main()

    except Exception as e:
        print(f"오류 발생: {e}")
        input("메인 화면으로 이동하려면 엔터를 누르세요.")
        main()

def resolution_video(url):
    cls();
    print("-----------------------------------------------------")
    print("                X-Cube Video Downloader")
    print("    영상 링크 - " + url)
    print("")
    print("    1   -   144p")
    print("    2   -   240p")
    print("    3   -   360p")
    print("    4   -   480p")
    print("")
    print("")
    print("")
    print("")
    cprint("주의사항    |     영상에 해당 화질이 없다면 프로그램이 자동으로 메인화면으로 가지게됩니다.", "red")
    print("")
    print("--------------------------------------------------")
    resolution = input("화질에 맞는 번호 선택      -     ");

    download_videoonly(url, resolution);

def download_videoonly(url, resolution):
    output_path = "downloads"
    try:
        # 다운로드 폴더 생성
        os.makedirs(output_path, exist_ok=True)

        real_resolution = convert_resolution(resolution)
        
        # yt-dlp 옵션 설정 (비디오만 다운로드)
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s', 
            'format': f"bestvideo[height={real_resolution}]",  # 오직 비디오 스트림만
            'merge_output_format': 'mp4',                       # 최종 파일을 mp4로 저장
            # FFmpeg 인자 설정 (비디오는 그대로 복사, 오디오는 없음)
            'postprocessor_args': [
                '-c:v', 'copy'  # 비디오 재인코딩 없이 그대로 복사
            ],
            'postprocessors': [
                {
                    'key': 'FFmpegVideoRemuxer',
                    'preferedformat': 'mp4',  # mp4 컨테이너로 remux
                },
            ],
        }
        
        # yt-dlp 실행
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("비디오(영상만) 다운로드가 완료되었습니다.")
            input("메인 화면으로 이동하려면 엔터를 누르세요.")
            main()

    except Exception as e:
        print(f"오류 발생: {e}")
        input("메인 화면으로 이동하려면 엔터를 누르세요.")
        main()

def download_av():
    cls();
    print("-----------------------------------------------------")
    print("                X-Cube Video Downloader")
    print("                사용해주셔서 감사합니다.")
    print("")
    print("               영상 링크를 입력해주세요.")
    print("--------------------------------------------------")
    print()
    url = input("링크:       -        ");
    resolution_av(url);

def resolution_av(url):
    cls();
    print("-----------------------------------------------------")
    print("                X-Cube Video Downloader")
    print("    영상 링크 - " + url)
    print("")
    print("    1   -   144p")
    print("    2   -   240p")
    print("    3   -   360p")
    print("    4   -   480p")
    print("")
    print("")
    print("")
    print("")
    cprint("주의사항    |     영상에 해당 화질이 없다면 프로그램이 자동으로 메인화면으로 가지게됩니다.", "red")
    print("")
    print("--------------------------------------------------")
    resolution = input("화질에 맞는 번호 선택      -     ");

    download_avonly(url, resolution);

def download_avonly(url, resolution):
    output_path = "downloads"
    try:
        # 다운로드 폴더 생성
        os.makedirs(output_path, exist_ok=True)

        real_resolution = convert_resolution(resolution);
        # yt-dlp 옵션 설정
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # 저장 경로 및 파일명
            'format': f"bestvideo[height={real_resolution}]+bestaudio/best",           # 최고 화질 비디오 + 최고 음질 오디오
            'merge_output_format': 'mp4',                   # 최종 병합 결과 mp4
            # FFmpeg에 직접 인자를 전달해 영상은 그대로, 오디오만 변환
            'postprocessor_args': [
                '-c:v', 'copy',        # 비디오는 그대로 복사 (재인코딩 X)
                '-c:a', 'aac',         # 오디오는 aac로 변환
                '-b:a', '192k'         # 오디오 비트레이트 192kbps
            ],
            'postprocessors': [
                {
                    # 비디오와 오디오를 Remux(재패키징)하여 MP4로 저장
                    'key': 'FFmpegVideoRemuxer',
                    'preferedformat': 'mp4'
                },
            ],
        }
        # yt-dlp 실행
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"다운로드가 완료됬습니다.")
            input("메인화면으로 이동하려면 엔터");
            main();


    except Exception as e:
        print(f"오류 발생: {e}")
        input("메인화면으로 이동하려면 엔터");
        main();

def convert_resolution(resolution):
    if resolution == "1":
        return "144";
    elif resolution == "2":
        return "240";
    elif resolution == "3":
        return "360";
    elif resolution == "4":
        return "480";
    elif resolution == "5":
        return "720";
    elif resolution == "6":
        return "1080";
    elif resolution == "7":
        return "1440";
    elif resolution == "8":
        return "2160";
    elif resolution == "9":
        return "4320";
    return "1080";

def cls():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:               # macOS, Linux 등
        os.system('clear')


if __name__ == "__main__":
    main()
