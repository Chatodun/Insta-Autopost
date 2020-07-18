from django.contrib import admin

# Register your models here.
from posting.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
