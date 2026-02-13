from djongo import models


class Team(models.Model):
    _id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class User(models.Model):
    _id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team_id = models.IntegerField()
    hero_name = models.CharField(max_length=200)
    power = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.hero_name


class Activity(models.Model):
    _id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    calories_burned = models.IntegerField()
    date = models.DateTimeField()
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.activity_type} - {self.user_id}"


class Leaderboard(models.Model):
    _id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    hero_name = models.CharField(max_length=200)
    team_id = models.IntegerField()
    team_name = models.CharField(max_length=200)
    total_activities = models.IntegerField()
    total_calories = models.IntegerField()
    total_duration_minutes = models.IntegerField()
    rank = models.IntegerField()
    last_updated = models.DateTimeField()

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']

    def __str__(self):
        return f"{self.rank}. {self.hero_name}"


class Workout(models.Model):
    _id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    exercises = models.JSONField()
    difficulty = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    category = models.CharField(max_length=100)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
