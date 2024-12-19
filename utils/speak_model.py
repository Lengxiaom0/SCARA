import pyttsx3 
from aip import AipSpeech
def play_mp3(filename):
    # 这里使用了playsound库来播放MP3文件，您需要先安装这个库（pip install playsound）
    from playsound import playsound
    playsound(filename)

APP_ID = '95321325'
API_KEY = '6uvQPuyskiykL217wyjHzYcT'
SECRET_KEY = 'u7C8z0re3sZqecXGljtPTNoXFhkOfJvv'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def speak(word_file,model_speak_audio_path):
    with open(word_file,"r",encoding="utf-8") as f:
        content=f.read()
    result  = client.synthesis(content, 'zh', 6, {
        'vol': 6, 'per':4,
    })
    if not isinstance(result, dict):
        with open(model_speak_audio_path, 'wb') as f:
            f.write(result)
    print('process end')
    play_mp3(model_speak_audio_path)
    
