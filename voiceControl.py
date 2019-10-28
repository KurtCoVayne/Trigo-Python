import speech_recognition as sr
from google.cloud import texttospeech
from pymongo import *
# obtain audio from the microphone
r = sr.Recognizer()
# dbClient = MongoClient('mongodb+srv://nodeApplications:zT8GkAlf9kqkuPkc@cluster0-ojqdw.mongodb.net/test?retryWrites=true&w=majority')
speechClient = texttospeech.TextToSpeechClient()
synthesis_input = texttospeech.types.SynthesisInput(text="Mi casa, tu casa!")

voice = texttospeech.types.VoiceSelectionParams(
    language_code='es-CO',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

response = speechClient.synthesize_speech(synthesis_input, voice, audio_config)

with open('output.mp3', 'wb') as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)
try:
	text = r.recognize_google(audio, language = "es-CO")
	if 'control' in text:
		if 'cambiar luces a' in text: 
			if 'rojo' in text:
				pass
			elif 'verde' in text:
				pass
			elif 'azul' in text:
				pass
			elif 'amarillo' in text:
				pass
			elif 'morado' in text:
				pass
		elif 'mover carro hacia' in text:
			if 'adelante' in text:
				pass
			elif 'atras' in text:
				pass
			elif 'izquierda' in text:
				pass
			elif 'derecha' in text:
				pass
except sr.UnknownValueError:
	print("ERROR FATAL: No se pudo reconocer nada de lo dicho")
except sr.RequestError as e:
	print("ERROR FATAL: No se pudieron solicitar los datos del audio; {0}".format(e))