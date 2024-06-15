from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import extract_audio, transcribe_audio, enhance_text, text_to_audio

def upload_video(request):
    if request.method == 'POST' and request.FILES['video']:
        video = request.FILES['video']
        fs = FileSystemStorage()
        video_path = fs.save(video.name, video)
        video_url = fs.url(video_path)
        audio_path = video_path.replace('.mp4', '.mp3')
        processed_audio_path = video_path.replace('.mp4', '_processed.mp3')

        extract_audio(video_path, audio_path)
        transcript = transcribe_audio(audio_path)
        enhanced_text = enhance_text(transcript)
        text_to_audio(enhanced_text, processed_audio_path)
        
        processed_audio_url = fs.url(processed_audio_path)
        return render(request, 'convertorApp/upload.html', {
            'processed_audio_url': processed_audio_url
        })
    return render(request, 'convertor/upload.html')
