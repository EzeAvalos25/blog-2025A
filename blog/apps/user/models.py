from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os


def get_avatar_filename(instance, filename):
  # avatar_default.jpg
  # avatar_default      .jpg
  base_filename, file_extension = os.path.splitext(filename)
  # user_827ffcb9-7e50-4264-81e1-46c2dc6fc098_avatar.png
  new_filename = f"user_{instance.id}_avatar{file_extension}"

  # user/avatar/user_827ffcb9-7e50-4264-81e1-46c2dc6fc098_avatar.png
  return os.path.join('user/acatar/', new_filename)

class User(AbstractUser):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  alias = models.CharField(max_length=50, blank=True)
  avatar = models.ImageField(upload_to=get_avatar_filename, default='user/defaul/avatar_default.jpg')

  def __str__(self):
   return self.username