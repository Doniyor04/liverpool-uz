from django.contrib import admin
from .models import Stadium, StadiumImage, ClubAchievement, ImportantDate, Legend


# Register your models here.
class StadiumImageInline(admin.TabularInline):
    model = StadiumImage
    extra = 1

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ('name', 'established_year', 'capacity')
    search_fields = ('name',)
    inlines = [StadiumImageInline]

@admin.register(StadiumImage)
class StadiumImageAdmin(admin.ModelAdmin):
    list_display = ('stadium', 'title', 'is_main', 'uploaded_at')
    list_filter = ('stadium', 'is_main')

@admin.register(ClubAchievement)
class ClubAchievementAdmin(admin.ModelAdmin):
    list_display= ('title', 'numb_achievement')
    
@admin.register(ImportantDate)
class ImportantDateAdmin(admin.ModelAdmin):
    list_display= ('title', 'content', 'year', 'image')

@admin.register(Legend)
class LegendAdmin(admin.ModelAdmin):
    list_display= ('name', 'about', 'image')
