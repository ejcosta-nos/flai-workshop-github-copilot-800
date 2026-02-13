from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from pymongo import MongoClient
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        
        self.stdout.write(self.style.SUCCESS('Clearing existing data...'))
        
        # Clear existing collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        
        self.stdout.write(self.style.SUCCESS('Creating unique index on email field...'))
        
        # Create unique index on email field
        db.users.create_index([("email", 1)], unique=True)
        
        self.stdout.write(self.style.SUCCESS('Populating teams...'))
        
        # Create teams
        teams = [
            {
                '_id': 1,
                'name': 'Team Marvel',
                'description': 'Earth\'s Mightiest Heroes',
                'created_at': datetime.now()
            },
            {
                '_id': 2,
                'name': 'Team DC',
                'description': 'Justice League Champions',
                'created_at': datetime.now()
            }
        ]
        db.teams.insert_many(teams)
        
        self.stdout.write(self.style.SUCCESS('Populating users...'))
        
        # Create users (superheroes)
        users = [
            # Team Marvel
            {
                '_id': 1,
                'username': 'ironman',
                'email': 'tony.stark@marvel.com',
                'first_name': 'Tony',
                'last_name': 'Stark',
                'team_id': 1,
                'hero_name': 'Iron Man',
                'power': 'Genius intellect and powered armor',
                'created_at': datetime.now()
            },
            {
                '_id': 2,
                'username': 'captainamerica',
                'email': 'steve.rogers@marvel.com',
                'first_name': 'Steve',
                'last_name': 'Rogers',
                'team_id': 1,
                'hero_name': 'Captain America',
                'power': 'Super soldier serum and tactical genius',
                'created_at': datetime.now()
            },
            {
                '_id': 3,
                'username': 'blackwidow',
                'email': 'natasha.romanoff@marvel.com',
                'first_name': 'Natasha',
                'last_name': 'Romanoff',
                'team_id': 1,
                'hero_name': 'Black Widow',
                'power': 'Master spy and martial artist',
                'created_at': datetime.now()
            },
            {
                '_id': 4,
                'username': 'thor',
                'email': 'thor.odinson@marvel.com',
                'first_name': 'Thor',
                'last_name': 'Odinson',
                'team_id': 1,
                'hero_name': 'Thor',
                'power': 'God of Thunder with Mjolnir',
                'created_at': datetime.now()
            },
            {
                '_id': 5,
                'username': 'hulk',
                'email': 'bruce.banner@marvel.com',
                'first_name': 'Bruce',
                'last_name': 'Banner',
                'team_id': 1,
                'hero_name': 'Hulk',
                'power': 'Gamma radiation transformation',
                'created_at': datetime.now()
            },
            # Team DC
            {
                '_id': 6,
                'username': 'batman',
                'email': 'bruce.wayne@dc.com',
                'first_name': 'Bruce',
                'last_name': 'Wayne',
                'team_id': 2,
                'hero_name': 'Batman',
                'power': 'Detective skills and advanced technology',
                'created_at': datetime.now()
            },
            {
                '_id': 7,
                'username': 'superman',
                'email': 'clark.kent@dc.com',
                'first_name': 'Clark',
                'last_name': 'Kent',
                'team_id': 2,
                'hero_name': 'Superman',
                'power': 'Kryptonian superpowers',
                'created_at': datetime.now()
            },
            {
                '_id': 8,
                'username': 'wonderwoman',
                'email': 'diana.prince@dc.com',
                'first_name': 'Diana',
                'last_name': 'Prince',
                'team_id': 2,
                'hero_name': 'Wonder Woman',
                'power': 'Amazonian strength and lasso of truth',
                'created_at': datetime.now()
            },
            {
                '_id': 9,
                'username': 'flash',
                'email': 'barry.allen@dc.com',
                'first_name': 'Barry',
                'last_name': 'Allen',
                'team_id': 2,
                'hero_name': 'The Flash',
                'power': 'Super speed',
                'created_at': datetime.now()
            },
            {
                '_id': 10,
                'username': 'aquaman',
                'email': 'arthur.curry@dc.com',
                'first_name': 'Arthur',
                'last_name': 'Curry',
                'team_id': 2,
                'hero_name': 'Aquaman',
                'power': 'Atlantean strength and aquatic abilities',
                'created_at': datetime.now()
            }
        ]
        db.users.insert_many(users)
        
        self.stdout.write(self.style.SUCCESS('Populating activities...'))
        
        # Create activities
        activities = []
        activity_types = ['Running', 'Swimming', 'Cycling', 'Weight Training', 'Yoga', 'Boxing']
        activity_id = 1
        
        for user_id in range(1, 11):
            for _ in range(random.randint(5, 10)):
                activity_type = random.choice(activity_types)
                activities.append({
                    '_id': activity_id,
                    'user_id': user_id,
                    'activity_type': activity_type,
                    'duration_minutes': random.randint(15, 120),
                    'distance_km': round(random.uniform(1.0, 20.0), 2) if activity_type in ['Running', 'Swimming', 'Cycling'] else None,
                    'calories_burned': random.randint(100, 800),
                    'date': datetime.now() - timedelta(days=random.randint(0, 30)),
                    'notes': f'Great {activity_type.lower()} session!'
                })
                activity_id += 1
        
        db.activities.insert_many(activities)
        
        self.stdout.write(self.style.SUCCESS('Populating workouts...'))
        
        # Create workouts
        workouts = [
            {
                '_id': 1,
                'name': 'Hero\'s Morning Routine',
                'description': 'Start your day like a superhero',
                'exercises': [
                    {'name': 'Push-ups', 'sets': 3, 'reps': 20},
                    {'name': 'Squats', 'sets': 3, 'reps': 25},
                    {'name': 'Planks', 'sets': 3, 'duration_seconds': 60}
                ],
                'difficulty': 'Intermediate',
                'duration_minutes': 30,
                'category': 'Strength'
            },
            {
                '_id': 2,
                'name': 'Speed Force Training',
                'description': 'Build explosive speed and agility',
                'exercises': [
                    {'name': 'Sprint Intervals', 'sets': 5, 'duration_seconds': 30},
                    {'name': 'Jump Rope', 'sets': 3, 'reps': 100},
                    {'name': 'Box Jumps', 'sets': 4, 'reps': 15}
                ],
                'difficulty': 'Advanced',
                'duration_minutes': 45,
                'category': 'Cardio'
            },
            {
                '_id': 3,
                'name': 'Amazonian Warrior Workout',
                'description': 'Build strength and endurance',
                'exercises': [
                    {'name': 'Deadlifts', 'sets': 4, 'reps': 10},
                    {'name': 'Battle Rope', 'sets': 3, 'duration_seconds': 45},
                    {'name': 'Burpees', 'sets': 3, 'reps': 15}
                ],
                'difficulty': 'Advanced',
                'duration_minutes': 50,
                'category': 'Strength'
            },
            {
                '_id': 4,
                'name': 'Detective Core Workout',
                'description': 'Focus on core stability and balance',
                'exercises': [
                    {'name': 'Russian Twists', 'sets': 3, 'reps': 30},
                    {'name': 'Leg Raises', 'sets': 3, 'reps': 15},
                    {'name': 'Mountain Climbers', 'sets': 3, 'reps': 20}
                ],
                'difficulty': 'Beginner',
                'duration_minutes': 25,
                'category': 'Core'
            },
            {
                '_id': 5,
                'name': 'Atlantean Swimming Circuit',
                'description': 'Master the waters',
                'exercises': [
                    {'name': 'Freestyle', 'sets': 5, 'distance_meters': 100},
                    {'name': 'Backstroke', 'sets': 5, 'distance_meters': 100},
                    {'name': 'Butterfly', 'sets': 3, 'distance_meters': 50}
                ],
                'difficulty': 'Intermediate',
                'duration_minutes': 60,
                'category': 'Swimming'
            }
        ]
        db.workouts.insert_many(workouts)
        
        self.stdout.write(self.style.SUCCESS('Calculating leaderboard...'))
        
        # Calculate and populate leaderboard
        leaderboard_entries = []
        for user in users:
            user_activities = [a for a in activities if a['user_id'] == user['_id']]
            total_calories = sum(a['calories_burned'] for a in user_activities)
            total_duration = sum(a['duration_minutes'] for a in user_activities)
            total_activities = len(user_activities)
            
            leaderboard_entries.append({
                '_id': user['_id'],
                'user_id': user['_id'],
                'username': user['username'],
                'hero_name': user['hero_name'],
                'team_id': user['team_id'],
                'team_name': 'Team Marvel' if user['team_id'] == 1 else 'Team DC',
                'total_activities': total_activities,
                'total_calories': total_calories,
                'total_duration_minutes': total_duration,
                'rank': 0,  # Will be calculated based on total_calories
                'last_updated': datetime.now()
            })
        
        # Sort by total calories and assign ranks
        leaderboard_entries.sort(key=lambda x: x['total_calories'], reverse=True)
        for idx, entry in enumerate(leaderboard_entries, start=1):
            entry['rank'] = idx
        
        db.leaderboard.insert_many(leaderboard_entries)
        
        # Print summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('DATABASE POPULATION COMPLETE!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(f'Teams created: {len(teams)}')
        self.stdout.write(f'Users created: {len(users)}')
        self.stdout.write(f'Activities created: {len(activities)}')
        self.stdout.write(f'Workouts created: {len(workouts)}')
        self.stdout.write(f'Leaderboard entries: {len(leaderboard_entries)}')
        self.stdout.write(self.style.SUCCESS('='*50 + '\n'))
        
        # Print top 5 leaderboard
        self.stdout.write(self.style.WARNING('TOP 5 LEADERBOARD:'))
        for entry in leaderboard_entries[:5]:
            self.stdout.write(
                f"  {entry['rank']}. {entry['hero_name']} ({entry['team_name']}) - "
                f"{entry['total_calories']} calories, {entry['total_activities']} activities"
            )
        
        client.close()
