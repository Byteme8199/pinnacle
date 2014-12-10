# Create your views here.
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from video.models import Video, VideoReply, PhotoReply
from video.forms import VideoForm
from account.models import Account
from django.views.generic.edit import FormView
from django.utils import timezone

from subprocess import check_output

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class PhotoView(LoggedInMixin, ListView):
	
	model = PhotoReply
	template_name = 'videos/photo.html'
	
	def get_queryset(self):
		#qs = Video.objects.filter(account=self.request.user.account.id)
		#for vid in qs:
			#print vid.thumbnail_holder
			#vid.thumbnail()
 		return PhotoReply.objects.filter(pk=self.request.id)

class VideoView(LoggedInMixin, ListView):

	model = Video
	template_name = 'videos/index.html'
	
	def get_queryset(self):
		#qs = Video.objects.filter(account=self.request.user.account.id)
		#for vid in qs:
			#print vid.thumbnail_holder
			#vid.thumbnail()
 		return Video.objects.filter(account=self.request.user.account.id)
	
class GuestVideoView(LoggedInMixin, ListView):
	model = Video
	template_name = 'videos/index.html'

	def get_queryset(self):
		if self.request.user.is_staff:
			thisid = self.request.path.split('/')
			return Video.objects.filter(account=thisid[2])
		else:
			return Video.objects.filter(account=self.request.user.account.id)
	
class AddVideoView(LoggedInMixin, FormView):
	
	model = Video
	template_name = 'videos/add.html'
	form_class = VideoForm
	success_url = '/videos/?success=Upload Successful'
	
	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		account_id = Account.objects.get(pk=self.request.user.account.id)
		video = Video(account=account_id, title=form.cleaned_data['title'], created_date=timezone.now(),note=form.cleaned_data['note'], file=form.cleaned_data['file'] )
		video.save()
		
		### Get Video, compress It and make a thumbnail
		
		#vidfile = Video.objects.get(pk=video.id)
		
		#new_path = str(vidfile.file.path).replace(str(vidfile.file), str(self.request.user.account.id) + "/" + str(vidfile.file))
	
		#new_thumb = str(vidfile.file.path).replace(".","-") + ".jpg"
		#new_vid = str(vidfile.file.path).replace(str(vidfile.file), str(self.request.user.account.id) + "/comp_" + str(vidfile.file))
		
		#check_output(["ffmpeg", "-i", str(vidfile.file.path), "-y", "-acodec", "mp2", str(new_vid)])
		#check_output(["ffmpeg", "-itsoffset", "-4", "-i", str(vidfile.file.path), "-vcodec", "mjpeg", "-vframes", "1", "-an", "-f", "rawvideo", "-s", "320x240", str(new_thumb)])
		
		return super(AddVideoView, self).form_valid(form)