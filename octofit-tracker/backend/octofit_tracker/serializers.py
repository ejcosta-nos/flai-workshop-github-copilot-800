from rest_framework import serializers
from .models import Team, User, Activity, Leaderboard, Workout


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='_id', read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='_id', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                  'team_id', 'hero_name', 'power', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='_id', read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration_minutes', 
                  'distance_km', 'calories_burned', 'date', 'notes']


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='_id', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'username', 'hero_name', 'team_id', 
                  'team_name', 'total_activities', 'total_calories', 
                  'total_duration_minutes', 'rank', 'last_updated']


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='_id', read_only=True)
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'exercises', 'difficulty', 
                  'duration_minutes', 'category']
