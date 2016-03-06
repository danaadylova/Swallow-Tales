from django.contrib import admin

# Register your models here.
from .models import Story
from .models import StorySection
from .models import Bookmark


admin.site.register(Story)
admin.site.register(StorySection)
admin.site.register(Bookmark)
