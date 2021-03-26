from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class song(models.Model):
    Id=models.AutoField(primary_key=True)
    name_of_song = models.CharField(max_length=100, blank=False, default='')
    duration = models.IntegerField(max_length=20,blank=False, default='')
    published = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.name_of_song
    def get_absolute_url(self):
        return reverse('song_list', kwargs={'slug': self.slug})
class participants(object):
	"""docstring for participants"""
	name = models.CharField(max_length=100, blank=False, default='')
	def __str__(self):
		return self.name
		

class podcast(models.Model):
	Id=models.AutoField(primary_key=True)
	name_of_podcast = models.CharField(max_length=100, blank=False, default='')
	duration = models.IntegerField(max_length=200,blank=False, default='')
	uploded_time = models.DateTimeField(default=timezone.now)
	host = models.CharField(max_length=100, blank=False, default='')
	participants=models.CharField(max_length=100, blank=False, default='')
	def publish(self):
		self.published_date=timezone.now()
		self.save
	def __str__(self):
		return self.name_of_podcast
	def get_absolute_url(self):
		return reverse('podcast_list', kwargs={'slug': self.slug})

class audiobook(models.Model):
	Id=models.AutoField(primary_key=True)
	title_of_book = models.CharField(max_length=100, blank=False, default='')
	author_of_title = models.CharField(max_length=100, blank=False, default='')
	narrator = models.CharField(max_length=100, blank=False, default='')
	duration = models.IntegerField(max_length=20,blank=False, default='')
	uploded_time = models.DateTimeField(default=timezone.now)

	def publish():
		self.published_date=timezone.now()
		self.save
	def __str__(self):
		return self.title_of_book
	def get_absolute_url(self):
		return reverse('audiobook_list', kwargs={'slug': self.slug})
