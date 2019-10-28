import speech_recognition as sr
from google.cloud import texttospeech
import pymongo
# obtain audio from the microphone
r = sr.Recognizer()
dbClient = pymongo.MongoClient(
    "mongodb+srv://<username>:<password>@cluster0-ojqdw.mongodb.net/test?retryWrites=true&w=majority")
control = dbClient['test']['control']

print(control.find_one({"_id": "5db66bbe8e8b7f40404c7094"}))

# speechClient = texttospeech.TextToSpeechClient()
# synthesis_input = texttospeech.types.SynthesisInput(text="Mi casa, tu casa!")

# voice = texttospeech.types.VoiceSelectionParams(
#     language_code='es-CO',
#     ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# audio_config = texttospeech.types.AudioConfig(
#     audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# response = speechClient.synthesize_speech(synthesis_input, voice, audio_config)

# with open('output.mp3', 'wb') as out:
#     out.write(response.audio_content)
#     print('Audio content written to file "output.mp3"')

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio, language="es-CO")
    print(text)
    if 'control' in text:
        if 'cambiar luces a' in text:
            if 'rojo' in text:
                control.find_one_and_update({"_id": "5db66bbe8e8b7f40404c7094"}, {
                                            "$set": {"rgb_color": [255, 0, 0]}})
            elif 'verde' in text:
                control.find_one_and_update({"_id": "5db66bbe8e8b7f40404c7094"}, {
                                            "$set": {"rgb_color": [0, 255, 0]}})
            elif 'azul' in text:
                control.find_one_and_update({"_id": "5db66bbe8e8b7f40404c7094"}, {
                                            "$set": {"rgb_color": [0, 0, 255]}})
            elif 'amarillo' in text:
                control.find_one_and_update({"_id": "5db66bbe8e8b7f40404c7094"}, {
                                            "$set": {"rgb_color": [255, 255, 0]}})
            elif 'morado' in text:
                control.find_one_and_update({"_id": "5db66bbe8e8b7f40404c7094"}, {
                                            "$set": {"rgb_color": [255, 0, 255]}})
        elif 'mover carro hacia' in text:
            if 'adelante' in text:
                control.find_one_and_update({"_id": "5db66bbe8e8b7f40404c7094"}, {
                                            "$set": {"car_forward": True,"car_backward":False,"car_right":False,"car_left":False}})
            elif 'atras' in text:
                control.find_one_and_update({"_id": "5db66bbe8e8b7f40404c7094"}, {
                                            "$set": {"car_forward": False,"car_backward":True,"car_right":False,"car_left":False}})
            elif 'izquierda' in text:
                control.find_one_and_update({"_id": "5db66bbe8e8b7f40404c7094"}, {
                                            "$set": {"car_forward": False,"car_backward":False,"car_right":False,"car_left":True}})
            elif 'derecha' in text:
                control.find_one_and_update({"_id": "5db66bbe8e8b7f40404c7094"}, {
                                            "$set": {"car_forward": False,"car_backward":False,"car_right":True,"car_left":False}})	
        elif 'encender luces' in text:
			if 'lado izquierdo' in text:
				control.find_one_and_update({"_id": "5db66bbe8e8b7f40404c7094"}, {
                                            "$set": {"left_lights": True}})
			elif 'lado derecho' in text:
				control.find_one_and_update({"_id": "5db66bbe8e8b7f40404c7094"}, {
                                            "$set": {"left_lights": False}})
        elif 'apagar luces' in text:
			if 'de atras' in text:
				pass
			if 'de los lados' in text:
				pass
except sr.UnknownValueError:
    print("ERROR FATAL: No se pudo reconocer nada de lo dicho")
except sr.RequestError as e:
    print(
        "ERROR FATAL: No se pudieron solicitar los datos del audio; {0}".format(e))
