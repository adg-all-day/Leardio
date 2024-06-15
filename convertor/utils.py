from moviepy.editor import VideoFileClip
from google.cloud import speech, texttospeech
import io
import openai
import speech_recognition as sr
import pyttsx3
from pydub import AudioSegment


openai.api_key = '*****'

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)


def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    transcript = ""
    
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)  # Read the entire audio file

        # Use the recognizer's built-in offline recognizer (Sphinx)
        transcript = recognizer.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print(f"Sphinx error; {e}")
    except FileNotFoundError:
        print(f"File not found: {audio_path}")
    except Exception as e:
        print(f"Error processing audio {audio_path}: {e}")

    return transcript

# Example usage:
# audio_file_path = "path/to/your/audio/file.wav"
# print(transcribe_audio(audio_file_path))




import openai

# Initialize OpenAI API client with your API key

def enhance_text(text):
    # Specify the model ID
    model = "text-davinci-003"

    # Construct the prompt
    prompt = f"""The following is a transcript of a tutorial video, enhance 
                it so that it can ba assimilated by the visually impaired 
                who have no access to the visual aid of the video. Add 
                more data from internet sources where needed and start the 
                text with a greeting and a briefing of the course and 
                things you would cover: {text}"""

    # Call the API with the new format
    response = openai.completions.create(
        model=model,
        prompt=prompt,
        max_tokens=1000
    )

    # Extract and return the enhanced text
    enhanced_text = response.choices[0].text.strip()
    return enhanced_text

# Example usage:
# enhanced_text = enhance_text("Your input text here")
# print(enhanced_text)



"""def enhance_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= """"""The following is a transcript of a tutorial video, enhance 
                  it so that it can ba assimilated by the visually impaired 
                  who have no access to the visual aid of the video. Add 
                  more data from internet sources where needed and start the 
                  text with a greeting and a briefing of the course and 
                  things you would cover:""" """ + text,
        max_tokens=1000
    )
    enhanced_text = response.choices[0].text.strip()
    return enhanced_text"""



def text_to_audio(text, audio_path):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Save the speech to a temporary WAV file
    temp_wav_path = "temp_audio.wav"
    engine.save_to_file(text, temp_wav_path)
    engine.runAndWait()

    # Convert the WAV file to MP3 using pydub
    audio = AudioSegment.from_wav(temp_wav_path)
    audio.export(audio_path, format="mp3")

    # Optionally, remove the temporary WAV file
    import os
    os.remove(temp_wav_path)

# Example usage:
# text_to_audio("Hello, this is a test.", "output_audio.mp3")

"""def text_to_audio(text, audio_path):
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
"""