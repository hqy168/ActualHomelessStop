from django.contrib import admin
from .models import Nonprofit
from .models import Event
from .models import Post

admin.site.register(Nonprofit)
admin.site.register(Event)
admin.site.register(Post)