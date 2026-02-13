from django.contrib import admin
from .models import Team, User, Activity, Leaderboard, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'description', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['_id']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['_id', 'username', 'hero_name', 'email', 'team_id', 'created_at']
    search_fields = ['username', 'email', 'hero_name', 'first_name', 'last_name']
    list_filter = ['team_id']
    ordering = ['_id']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['_id', 'user_id', 'activity_type', 'duration_minutes', 
                    'calories_burned', 'date']
    search_fields = ['activity_type', 'notes']
    list_filter = ['activity_type', 'date']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['rank', 'hero_name', 'team_name', 'total_activities', 
                    'total_calories', 'total_duration_minutes', 'last_updated']
    search_fields = ['username', 'hero_name', 'team_name']
    list_filter = ['team_name']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'category', 'difficulty', 'duration_minutes']
    search_fields = ['name', 'description', 'category']
    list_filter = ['difficulty', 'category']
    ordering = ['_id']
