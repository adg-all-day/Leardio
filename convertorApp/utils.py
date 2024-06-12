from moviepy.editor import VideoFileClip
from google.cloud import speech, texttospeech
import io
import openai

openai.api_key = 'sk-proj-mJkbWuiznrhSWpVzzoreT3BlbkFJpSdtYKlLVSiNpYCaROnB'

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

def transcribe_audio(audio_path):
    client = speech.SpeechClient()
    with io.open(audio_path, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    response = client.recognize(config=config, audio=audio)
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript + " "
    return transcript

def enhance_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= """The following is a transcript of a tutorial video, enhance 
                  it so that it can ba assimilated by the visually impaired 
                  who have no access to the visual aid of the video. Add 
                  more data from internet sources where needed and start the 
                  text with a greeting and a briefing of the course and 
                  things you would cover: """ + text,
        max_tokens=1000
    )
    enhanced_text = response.choices[0].text.strip()
    return enhanced_text

def text_to_audio(text, audio_path):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open(audio_path, "wb") as out:
        out.write(response.audio_content)
