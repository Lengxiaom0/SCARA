import wave
from pyaudio import PyAudio,paInt16  #导入音频处理库Pyaudio，没有的话要pip 安装
from aip import AipSpeech
# 设置采样参数
NUM_SAMPLES = 2000
# 默认录音4s
TIME = 5

# 百度智能云平台语音技能密钥
# 请输入您的BaiduAPP_ID，下面自行调用应用哦~
BaiduAPP_ID = '88027780'  
# 请输入您的BaiduAPI_KEY      
BaiduAPI_KEY = '8Y8tWSfHu9oIXoh4uwa89Vzt'
# 请输入您的SECRET_KEY      
SECRET_KEY = 'JdRDt3JXjNxbFGF0f807YPOD5mZ9TmMi'

client = AipSpeech(BaiduAPP_ID, BaiduAPI_KEY, SECRET_KEY)

def save_wave_file(filename,data):  
    wf = wave.open(filename,'wb')  # 打开WAV文档
    wf.setnchannels(1)  #配置声道数            
    wf.setsampwidth(2)  #配置量化位数              
    wf.setframerate(16000) #采样频率         
    wf.writeframes(b"".join(data))  # 将wav_data转换为二进制数据写入文件
    wf.close()

# 定义录音函数
def record(user_speak_wav_path):
    print('Start recording.')
    # 实例化PyAudio对象，开启声音输入
    pa = PyAudio()  
    # 打开输入流并设置音频采样参数 1 channel 16K framerate 
    stream = pa.open(format = paInt16,
                        channels = 1,
                        rate = 16000,
                        input = True,
                        frames_per_buffer = NUM_SAMPLES)
    # 录音缓存数组
    audioBuffer = []   
    # 循环采集音频 默认录制4s
    count = 0
    while count<TIME*10:
        # 一次性录音采样字节的大小
        string_audio_data = stream.read(NUM_SAMPLES)  
        audioBuffer.append(string_audio_data)
        count +=1
        # 加逗号不换行输出
        print('.', end='')  
    print('')
    print('End recording.')
    # 保存录制的语音文件到audio.wav中并关闭输入流
    save_wave_file(user_speak_wav_path,audioBuffer)
    stream.close()

# 语音识别函数
def asr_updata(user_speak_wav_path):
    with open(user_speak_wav_path, 'rb') as f:
        audio_data = f.read()
    result = client.asr(audio_data, 
                        'wav', 16000, {   # 采样频率16K
                        'dev_pid': 1536, 
                                          # 1536 普通话
                                          # 1537 普通话（纯中文识别）
                                          # 1737 英语
                                          # 1637 粤语
                                          # 1837 四川话
                     })
    
    print(result)  #打印出来，报错的时候可以查看代码
    val = 'result' in result.keys()
    print("val:",val)
    if val == True:   
        result_text = result["result"][0]
    else:
        result_text = '语音未识别'
    print("result_text:",result_text)
    return result_text



