from moviepy.editor import VideoFileClip
from google.cloud import speech, texttospeech
import io
import openai
from pydub import AudioSegment

openai.api_key = ''

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

import speech_recognition as sr

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    transcript = ""
    
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)  # Read the entire audio file

        transcript = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except FileNotFoundError:
        print(f"File not found: {audio_path}")
    except Exception as e:
        print(f"Error processing audio {audio_path}: {e}")

    return transcript

# Example usage:
# audio_file_path = "path/to/your/audio/file.wav"
# print(transcribe_audio(audio_file_path))


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

def convert_wav_to_mp3(wav_path, mp3_path):
    audio = AudioSegment.from_wav(wav_path)
    audio.export(mp3_path, format="mp3")