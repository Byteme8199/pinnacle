from django.forms import ModelForm
from video.models import Video, VideoType

class VideoForm(ModelForm):

	class Meta:
		model = Video
		exclude = ('account', 'created_date')