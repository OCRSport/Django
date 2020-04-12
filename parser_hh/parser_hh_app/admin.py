from django.contrib import admin
from .models import Code_Region, Vacancy, Skill

admin.site.register(Code_Region)
admin.site.register(Vacancy)


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'info']


admin.site.register(Skill, SkillAdmin)
