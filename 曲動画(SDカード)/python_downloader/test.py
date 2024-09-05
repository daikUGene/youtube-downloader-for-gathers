from yt_dlp import YoutubeDL

def download_videos_from_file(file_path):
    # ファイルからURLを読み取る
    with open(file_path, 'r') as file:
        urls = file.readlines()
    
    # 改行文字を削除してURLをクリーニングする
    urls = [url.strip() for url in urls]

    # ダウンロードと変換のオプション設定
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'm4v',
        }],
    }

    # URLごとにダウンロード
    for url in urls:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

def main():
    # テキストファイルのパスを指定してダウンロードする
    file_path = 'urls.txt'
    download_videos_from_file(file_path)

if __name__ == "__main__":
    main()
