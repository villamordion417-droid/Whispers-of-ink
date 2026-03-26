# 🕊️ Whispers of Ink

A peaceful, creative writing platform where writers can share their stories, poems, essays, and reflections with the world.

## ✨ Features

### User Authentication
- User registration and account creation
- Secure login system
- User dashboard for managing writings
- Personalized user profiles

### Writing Management
- Create posts with title, content, category, and inspiration notes
- Edit your own published writings
- Delete your posts with confirmation
- Organize posts by 8 themes: Love, Pain, Hope, Youth, Life, Reflection, Poetry, Short Story

### Community Features
- View all published writings in chronological order
- Filter writings by category
- Search writings by title or content
- Leave comments on posts (requires login)
- Read feedback from community members

### Design
- Calm, peaceful aesthetic with soft colors
- Minimalist design for distraction-free reading
- Responsive layout for mobile and desktop
- Elegant typography using Georgia serif font

## 🛠️ Technology Stack

- **Backend:** Django 6.0.3
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite3
- **Authentication:** Django built-in user authentication

## 📋 Project Structure

```
mysite/
├── accounts/              # User authentication and profiles
│   ├── models.py         # Link to Django User model
│   ├── views.py          # Login, register, logout, dashboard
│   └── urls.py           # Authentication URLs
│
├── writings/             # Main writing posts functionality
│   ├── models.py         # Post, Category models
│   ├── views.py          # CRUD operations for posts
│   ├── admin.py          # Admin interface
│   └── urls.py           # Post URLs
│
├── comments/             # Comment system
│   ├── models.py         # Comment model
│   ├── forms.py          # Comment form
│   ├── admin.py          # Comment admin
│   └── views.py          # (handled in writings app)
│
├── core/                 # Home and general pages
│   ├── views.py          # Home, About pages
│   └── urls.py           # Core URLs
│
├── templates/            # HTML templates
│   ├── base.html         # Base template with styling
│   ├── accounts/         # Auth templates
│   ├── writings/         # Writing templates
│   └── core/             # Home and about templates
│
├── static/               # Static files (CSS, JS, images)
│   └── css/              # CSS files
│
├── manage.py             # Django management script
├── db.sqlite3            # Database file
└── init_data.py          # Script to initialize categories
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Navigate to project directory:**
   ```bash
   cd c:\Users\User\Desktop\jillian_pangit\mysite
   ```

2. **Install dependencies (if needed):**
   ```bash
   pip install django
   ```

3. **Run migrations (already done):**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account for accessing /admin

5. **Start development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Website: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## 📖 Usage Guide

### For Writers

1. **Sign Up**
   - Click "Sign Up" on the home page
   - Fill in username, email, and password
   - Your account is ready to use!

2. **Create a Writing**
   - Click "+ New Writing" in navigation or "Write Something" button
   - Fill in title, select category, write your content
   - Optionally add an inspiration note
   - Click "Publish"

3. **Edit Your Writing**
   - Go to your Dashboard
   - Click "Edit" on any of your posts
   - Make changes and save

4. **Delete a Writing**
   - Go to your Dashboard
   - Click "Delete" on the post
   - Confirm deletion (cannot be undone)

5. **View Dashboard**
   - Click "Dashboard" in navigation
   - See all your published writings
   - Quick access to edit/delete/view options

### For Readers

1. **Browse Writings**
   - Visit "All Writings" page
   - Browse all published works
   - Filter by category using category buttons
   - Search by title using the search box

2. **Read a Writing**
   - Click on any writing to view full content
   - See author information and post date
   - Read inspiration note (if provided)

3. **Leave Comments**
   - Must be logged in to comment
   - Scroll to comments section
   - Type your feedback and click "Post Comment"
   - Comments appear in chronological order

## 🎨 Customization

### Add New Categories

1. Go to http://localhost:8000/admin
2. Log in with superuser credentials
3. Navigate to "Writings" → "Categories"
4. Click "Add Category"
5. Fill in name, slug (lowercase, no spaces), and description

### Modify Design

Edit `templates/base.html` to customize:
- Fonts and colors (currently: soft pastels, Georgia serif)
- Layout and spacing
- Navigation structure

Main color palette:
- Primary: #c9a961 (gold)
- Text: #6b5344 (dark brown)
- Background: #faf8f3 (off-white)
- Accent: #f0e8dc (beige)

## 🔐 Security Notes

- Keep `SECRET_KEY` in `mysite/settings.py` secret
- Never share your superuser credentials
- Set `DEBUG = False` before deploying to production
- Create a `.env` file for sensitive settings in production

## 📝 Models Overview

### User
- Django's built-in User model
- Fields: username, email, password

### Category
- name (CharField)
- slug (SlugField)
- description (TextField)

### Post
- title (CharField)
- content (TextField)
- author (ForeignKey to User)
- category (ForeignKey to Category)
- inspiration_note (TextField, optional)
- created_at (DateTimeField)
- updated_at (DateTimeField)

### Comment
- post (ForeignKey to Post)
- author (ForeignKey to User)
- content (TextField)
- created_at (DateTimeField)
- updated_at (DateTimeField)

## 🐛 Troubleshooting

### "No such table" errors
- Run: `python manage.py migrate`

### Page shows 404 error
- Check URL spelling in browser
- Verify URLs are correctly configured in urls.py

### Static files not loading
- Run: `python manage.py collectstatic`

### Can't submit forms
- Ensure you're logged in for comment/create post
- Check that POST is selected, not GET

## 📧 Contact & Support

For issues or questions, refer to:
- Views structure in each app's `views.py`
- Model definitions in `models.py`
- Template organization in `templates/` directory

## 📄 License

Created for educational purposes.

---

**Version:** 1.0  
**Last Updated:** 2024  
**Made with ✨ for writers everywhere**
