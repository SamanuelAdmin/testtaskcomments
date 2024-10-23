import os
import random

from django.db import models
from django.conf import settings

from PIL import Image

from .modules import token_generator, filetype_checker


def customFileUploadToMethod(instance, filename) -> str: # get unique name with correct path
	uploadFolder = os.path.join(
		settings.MEDIA_ROOT,
		instance.username[0] if instance.username[0] in 'abcdefghljklmnopqrstuvwxyz' \
		            else random.choice('abcdefghljklmnopqrstuvwxyz')
	)
	if not os.path.exists(uploadFolder): os.makedirs(uploadFolder)

	# generate unique filename (yeah, i know about another ways to do it)
	fileToken = token_generator.generateToken()
	baseFilename, extension = os.path.splitext(filename)
	filename = f'{baseFilename}_{fileToken}{extension}'

	# set new name
	fullFilePath = os.path.join(uploadFolder, filename)
	return fullFilePath


# Create your models here.
class Comment(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField()
	homepage = models.URLField(blank=True)
	text = models.TextField()
	time_create = models.DateTimeField(auto_now_add=True)
	parentComment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
	file = models.FileField(blank=True, upload_to=customFileUploadToMethod)

	objects = models.Manager()

	# its for the future, pls dont touch it :)
	def save(self, *args, **kwargs):
		super(Comment, self).save(*args, **kwargs)

		if self.file:
			filepath = self.file.path

			# if file is image (not a text)
			if filetype_checker.fileMime(filepath) != 'text/plain':
				image = Image.open(filepath)
				imageSize = (image.width, image.height)

				if imageSize > settings.MAX_IMAGE_SIZE:
					image = image.resize(
						(round(image.width / imageSize[0] * settings.MAX_IMAGE_SIZE[0]),
						 round(image.height / imageSize[0] * settings.MAX_IMAGE_SIZE[1])),
					)

					image.save(filepath)


	def __str__(self):
		return f'[{self.id}] {self.username} {self.time_create}'

	class Meta:
		ordering = ['-time_create']

