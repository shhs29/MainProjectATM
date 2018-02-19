from gtts import gTTS
import os
tts = gTTS(text='Hey there Theres an error', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
