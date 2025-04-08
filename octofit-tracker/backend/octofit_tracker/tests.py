from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        team = Team.objects.create(name="Team A")
        team.members.add(user)
        self.assertEqual(team.name, "Team A")
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        activity = Activity.objects.create(user=user, activity_type="Running", duration="00:30:00")
        self.assertEqual(activity.activity_type, "Running")
        self.assertEqual(activity.user, user)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)
        self.assertEqual(leaderboard.user, user)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Push-ups", description="Do 20 push-ups")
        self.assertEqual(workout.name, "Push-ups")
        self.assertEqual(workout.description, "Do 20 push-ups")