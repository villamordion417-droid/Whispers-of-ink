import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from writings.models import Category, Post
from django.utils import timezone

# Create categories
categories_data = [
    {'name': 'Love', 'slug': 'love', 'description': 'Writings about love, relationships, and affection'},
    {'name': 'Pain', 'slug': 'pain', 'description': 'Exploring hardship, loss, and difficult emotions'},
    {'name': 'Hope', 'slug': 'hope', 'description': 'Uplifting tales of resilience and positive outcomes'},
    {'name': 'Youth', 'slug': 'youth', 'description': 'Reflections on growing up and youthful experiences'},
    {'name': 'Life', 'slug': 'life', 'description': 'Observations about the human experience'},
    {'name': 'Reflection', 'slug': 'reflection', 'description': 'Thoughtful meditations and self-discovery'},
    {'name': 'Poetry', 'slug': 'poetry', 'description': 'Poetic expressions and verses'},
    {'name': 'Short Story', 'slug': 'short-story', 'description': 'Brief fictional narratives'},
]

print("Creating categories...")
for cat_data in categories_data:
    category, created = Category.objects.get_or_create(
        slug=cat_data['slug'],
        defaults={
            'name': cat_data['name'],
            'description': cat_data['description']
        }
    )
    if created:
        print(f"✓ Created category: {category.name}")
    else:
        print(f"○ Category already exists: {category.name}")

print("\nInitialization complete!")
print(f"Total categories: {Category.objects.count()}")
