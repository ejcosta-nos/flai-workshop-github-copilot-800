from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime
from .models import Team, User, Activity, Leaderboard, Workout


class TeamAPITestCase(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(
            _id=1,
            name='Test Team',
            description='A test team',
            created_at=datetime.now()
        )

    def test_list_teams(self):
        """Test listing all teams"""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_team(self):
        """Test retrieving a single team"""
        response = self.client.get(f'/api/teams/{self.team._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Team')


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            _id=1,
            username='testuser',
            email='test@example.com',
            first_name='Test',
            last_name='User',
            team_id=1,
            hero_name='Test Hero',
            power='Testing powers',
            created_at=datetime.now()
        )

    def test_list_users(self):
        """Test listing all users"""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_user(self):
        """Test retrieving a single user"""
        response = self.client.get(f'/api/users/{self.user._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')


class ActivityAPITestCase(APITestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            _id=1,
            user_id=1,
            activity_type='Running',
            duration_minutes=30,
            distance_km=5.0,
            calories_burned=300,
            date=datetime.now(),
            notes='Test run'
        )

    def test_list_activities(self):
        """Test listing all activities"""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_activity(self):
        """Test retrieving a single activity"""
        response = self.client.get(f'/api/activities/{self.activity._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['activity_type'], 'Running')


class LeaderboardAPITestCase(APITestCase):
    def setUp(self):
        self.leaderboard_entry = Leaderboard.objects.create(
            _id=1,
            user_id=1,
            username='testuser',
            hero_name='Test Hero',
            team_id=1,
            team_name='Test Team',
            total_activities=10,
            total_calories=5000,
            total_duration_minutes=300,
            rank=1,
            last_updated=datetime.now()
        )

    def test_list_leaderboard(self):
        """Test listing leaderboard entries"""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_leaderboard_entry(self):
        """Test retrieving a single leaderboard entry"""
        response = self.client.get(f'/api/leaderboard/{self.leaderboard_entry._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rank'], 1)


class WorkoutAPITestCase(APITestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            _id=1,
            name='Test Workout',
            description='A test workout',
            exercises=[
                {'name': 'Push-ups', 'sets': 3, 'reps': 10}
            ],
            difficulty='Beginner',
            duration_minutes=30,
            category='Strength'
        )

    def test_list_workouts(self):
        """Test listing all workouts"""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_workout(self):
        """Test retrieving a single workout"""
        response = self.client.get(f'/api/workouts/{self.workout._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Workout')


class APIRootTestCase(APITestCase):
    def test_api_root(self):
        """Test API root endpoint"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

    def test_root_redirect(self):
        """Test root URL redirects to API"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
