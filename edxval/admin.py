"""
Admin file for django app edxval.
"""

from django.contrib import admin
from .models import Video, Profile, EncodedVideo, Subtitle

admin.site.register(Video)
admin.site.register(Profile)
admin.site.register(EncodedVideo)
admin.site.register(Subtitle)
