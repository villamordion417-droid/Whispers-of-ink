# ⚡ Whispers of Ink - Quick Reference

## 🚀 Start Here

```bash
# Start the server
python manage.py runserver

# Visit in browser
http://localhost:8000
```

---

## 📋 Essential Commands

### Server Management
```bash
# Start development server
python manage.py runserver

# Start on specific port
python manage.py runserver 8080

# Create admin account
python manage.py createsuperuser

# Check system
python manage.py check
```

### Database
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Initialize sample data
python init_data.py

# Access database shell
python manage.py dbshell
```

### Static Files
```bash
# Collect static files
python manage.py collectstatic

# Show static files location
python manage.py collectstatic --dry-run
```

### Django Shell
```bash
# Interactive Python shell with Django
python manage.py shell

# Example commands:
# >>> from writings.models import Post
# >>> posts = Post.objects.all()
# >>> post = Post.objects.get(id=1)
```

---

## 🌐 All URLs

| URL | Purpose |
|-----|---------|
| `/` | Home page |
| `/about/` | About page |
| `/accounts/register/` | Sign up |
| `/accounts/login/` | Login |
| `/accounts/logout/` | Logout |
| `/accounts/dashboard/` | Your dashboard |
| `/writings/` | All writings |
| `/writings/create/` | New writing |
| `/writings/post/<id>/` | View post |
| `/writings/post/<id>/edit/` | Edit post |
| `/writings/post/<id>/delete/` | Delete post |
| `/admin/` | Admin panel |

---

## 🔑 Default Admin Login

- **URL:** http://localhost:8000/admin
- **Username:** (created with `createsuperuser`)
- **Password:** (created with `createsuperuser`)

---

## 📁 Key Files

### Configuration
- `mysite/settings.py` - Main settings
- `mysite/urls.py` - URL routing

### Database Models
- `writings/models.py` - Post & Category
- `comments/models.py` - Comment
- `accounts/models.py` - Uses Django User

### Views (Logic)
- `accounts/views.py` - Auth logic
- `writings/views.py` - Post CRUD
- `core/views.py` - Home & About

### Templates
- `templates/base.html` - Main template
- `templates/accounts/` - Auth pages
- `templates/writings/` - Post pages
- `templates/core/` - Home/About

---

## 🎨 Customization

### Change Colors
Edit `templates/base.html` in the `<style>` section:
```css
.btn-primary {
    background-color: #new-color;
}
```

### Add Navigation Link
Edit `templates/base.html` in the nav-links:
```html
<li><a href="{% url 'new_page' %}">New Link</a></li>
```

### Add Category
Go to http://localhost:8000/admin → Categories → Add

### Change Site Title
Edit `mysite/settings.py` and look for title references

---

## 🔧 Common Tasks

### Reset Superuser Password
```bash
python manage.py changepassword admin
```

### Delete All Data
```bash
# WARNING: This deletes everything!
python manage.py flush
```

### Create Test User
```bash
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_user('testuser', 'test@test.com', 'password123')
```

### View All Posts
```bash
python manage.py shell
>>> from writings.models import Post
>>> for post in Post.objects.all():
...     print(f"{post.title} by {post.author}")
```

### Delete a Post
```bash
python manage.py shell
>>> from writings.models import Post
>>> post = Post.objects.get(id=1)
>>> post.delete()
```

---

## 📊 Database Structure

### Users Table
- id, username, email, password, first_name, last_name, is_staff, etc.

### Categories Table
- id, name, slug, description

### Posts Table
- id, title, content, author_id, category_id, inspiration_note, created_at, updated_at

### Comments Table
- id, post_id, author_id, content, created_at, updated_at

---

## 🛠️ Troubleshooting

### Server won't start
```bash
# Check Python version
python --version

# Check Django installation
python -m pip show django

# Reinstall Django
python -m pip install --upgrade django
```

### Database errors
```bash
# Recreate database
rm db.sqlite3
python manage.py migrate
python init_data.py
```

### Import errors
```bash
# Verify app is in INSTALLED_APPS
# Check mysite/settings.py
```

### Port already in use
```bash
# Use different port
python manage.py runserver 8001
```

---

## 📱 Mobile Testing

```bash
# Get your machine IP
ipconfig getifaddr en0  # macOS
hostname -I            # Linux
ipconfig               # Windows

# Access from phone on same network
http://YOUR_IP:8000
```

---

## 🔒 Security Reminders

- ✅ Never share SECRET_KEY
- ✅ Never commit passwords to git
- ✅ Set DEBUG = False in production
- ✅ Use HTTPS in production
- ✅ Update Django regularly
- ✅ Keep backups of database

---

## 📚 File Descriptions

| File | Contains |
|------|----------|
| `manage.py` | Django CLI |
| `db.sqlite3` | Database |
| `requirements.txt` | Dependencies |
| `README.md` | Full docs |
| `GETTING_STARTED.md` | Setup guide |
| `FEATURES_CHECKLIST.md` | Feature list |
| `DEVELOPMENT_NOTES.md` | Code notes |
| `PROJECT_SUMMARY.md` | Overview |
| `run.bat` | Windows start |
| `run.sh` | Mac/Linux start |

---

## 🌟 Pro Tips

1. **Use Django Admin** - Manage content easily at /admin/
2. **Enable Debug Toolbar** - Install django-debug-toolbar for profiling
3. **Use Django Shell** - Test code quickly with `python manage.py shell`
4. **Version Control** - Use git to track changes
5. **Backup Regularly** - Copy db.sqlite3 regularly
6. **Test Thoroughly** - Test all features before deploying
7. **Read the Code** - Check views.py to understand flow
8. **Use Comments** - Document complex logic

---

## 💡 Quick Features Overview

| Feature | Location |
|---------|----------|
| Write Posts | /writings/create/ |
| View Posts | /writings/ |
| Edit Your Posts | Dashboard |
| Delete Posts | Dashboard |
| Leave Comments | Post detail page |
| Filter by Category | /writings/?category=love |
| Search | /writings/?search=word |
| View Dashboard | /accounts/dashboard/ |
| Edit Profile | /accounts/dashboard/ |
| Admin Panel | /admin/ |

---

## 🎯 Performance

### Optimization Tips
- Use django-debug-toolbar to find slow queries
- Add database indexes for frequently searched fields
- Use select_related() and prefetch_related() in views
- Enable caching for expensive queries
- Minify CSS and JavaScript in production

### Current Setup
- ✅ Database: SQLite (OK for single server)
- ✅ Caching: Not configured (add if slow)
- ✅ Static files: local (use CDN in production)
- ✅ Email: Not configured (add for password reset)

---

## 📈 Next Steps

1. Create admin account: `python manage.py createsuperuser`
2. Start server: `python manage.py runserver`
3. Visit home: http://localhost:8000
4. Register account: /accounts/register/
5. Write first post: /writings/create/
6. Explore features

---

**Need Help? Check the detailed docs in README.md and GETTING_STARTED.md** 📚
