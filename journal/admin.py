from django.contrib import admin

from .models import Budget, Diary, Event, Meeting, Plan, Project, Quote, Todo

# Register your models here.
admin.site.register(Todo);
admin.site.register(Diary);
admin.site.register(Meeting);
admin.site.register(Event);
admin.site.register(Plan);
admin.site.register(Project);
admin.site.register(Quote);
admin.site.register(Budget);