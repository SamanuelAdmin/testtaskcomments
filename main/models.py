from django.db import models

# Create your models here.
class Comment(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField()
	homepage = models.URLField(blank=True)
	text = models.TextField()
	time_create = models.DateTimeField(auto_now_add=True)
	parentComment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return f'[{self.id}] {self.username} {self.time_create}'