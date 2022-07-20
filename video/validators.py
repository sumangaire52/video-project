from django.core.exceptions import ValidationError
from moviepy.editor import VideoFileClip

''' 
def validate_size(video):
    file_size = video.size
    limit_gb = 1
    if file_size > limit_gb * (1024**3):
        raise ValidationError(f"Max size of file is {limit_gb} GB")


def validate_duration(video):
    file_path = video.temporary_file_path()
    clip = VideoFileClip(file_path)
    if clip.duration > 10*60:
        raise ValidationError(f"Max duration of video is 10 Minutes")
'''

def validate_video(video):
    supported_extensions = ['mp4','mkv']
    extension = video.name.split('.')[-1]

    if video.size > 1024**3:
        raise ValidationError(f"Max size of file is 1 GB")
        
    if extension in supported_extensions:
        file_path = video.temporary_file_path()
        clip = VideoFileClip(file_path)

        if clip.duration > 10*60:
            raise ValidationError(f"Max duration of video is 10 Minutes")

    else:
        raise ValidationError("File must be mp4 or mkv")