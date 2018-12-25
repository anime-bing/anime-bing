from django.contrib import admin
from .models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','status')
    list_filter = ('status','created_at',)
    serach_fields = ('author__username','title')
    prepopulated_fields = {'slug':('title',)}

    list_editable = ('status',)


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
