from django.contrib import admin
from blogging.models import Post, PostAdmin, Category, CategoryAdmin

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)