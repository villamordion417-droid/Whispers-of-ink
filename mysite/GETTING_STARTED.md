# 🚀 Getting Started with Whispers of Ink

## Initial Setup

### Step 1: Start the Server

**On Windows:**
```bash
run.bat
```

**On macOS/Linux:**
```bash
bash run.sh
```

Or manually:
```bash
python manage.py runserver
```

### Step 2: Create Superuser (Admin Account)

In another terminal window:
```bash
python manage.py createsuperuser
```

Follow the prompts:
- **Username:** Choose any username (e.g., `admin`)
- **Email:** Enter your email
- **Password:** Create a strong password
- **Password (again):** Confirm password

Example:
```
Username: admin
Email: admin@example.com
Password: ••••••••
Password (again): ••••••••
Superuser created successfully.
```

### Step 3: Access the Application

Open your web browser and navigate to:
- **Home Page:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin

## Using the Admin Panel

1. Visit http://localhost:8000/admin
2. Log in with your superuser credentials
3. You'll see the admin dashboard with options for:
   - **Users:** Manage user accounts
   - **Categories:** Add/edit writing categories
   - **Posts:** Manage all writings
   - **Comments:** Manage user comments

### Adding More Categories

1. Click "Categories" under the Writings section
2. Click "Add category"
3. Fill in:
   - **Name:** Category name (e.g., "Fantasy")
   - **Slug:** URL-friendly version (e.g., "fantasy")
   - **Description:** Brief description (optional)
4. Click "Save"

The category will now appear in the category filter on the Writings page.

## First Time User Guide

### Creating a Test Post

1. Register a new account (or use admin if testing)
2. Click "+ New Writing" (or "+ Write New Piece" in dashboard)
3. Fill in:
   - **Title:** "My First Poetry"
   - **Category:** Select "Poetry"
   - **Content:** Write your sample text
   - **Inspiration Note:** (Optional) "This is my first piece"
4. Click "Publish"

### Testing Comments

1. View the post you just created
2. Scroll to "Feedback & Comments"
3. If logged in, type a comment and click "Post Comment"
4. The comment will appear immediately

### Filtering and Searching

1. Go to "All Writings"
2. Click category buttons to filter
3. Use the search box to find posts by title
4. The category indicator at top shows what's selected

## Features to Try

### ✍️ Writing Features
- [ ] Create a new writing
- [ ] Add an inspiration note
- [ ] Edit your writing
- [ ] View your dashboard
- [ ] Delete a writing (with confirmation)

### 👥 Community Features
- [ ] Browse all writings
- [ ] Filter by category
- [ ] Search for writings
- [ ] View author info
- [ ] Leave a comment
- [ ] Read others' comments

### 👤 Account Features
- [ ] Register a new account
- [ ] Log in
- [ ] View your dashboard
- [ ] Log out
- [ ] Read about the platform

## Troubleshooting

### Issue: "Page not found" (404)
**Solution:** Make sure the server is running and you're using the correct URL

### Issue: Database errors
**Solution:** Run migrations again:
```bash
python manage.py migrate
```

### Issue: Can't log in
**Solution:** 
- Verify your username and password are correct
- Create a new account if you forgot credentials
- Use admin panel at /admin to reset passwords

### Issue: Categories not showing
**Solution:** 
- Run the initialization script:
  ```bash
  python init_data.py
  ```
- Or add categories manually in the admin panel

### Issue: Comments not appearing
**Solution:**
- You must be logged in to post comments
- Refresh the page after posting
- Check that the post has comments permission enabled

## Best Practices

### For Writers
1. ✨ Write from the heart - authenticity resonates
2. 📝 Choose meaningful titles
3. 💭 Add inspiration notes to connect with readers
4. ✏️ Edit and refine your work
5. 🌿 Share diverse topics and perspectives

### For Administrators
1. 🔐 Keep your admin password secure
2. 📋 Moderate comments if needed
3. 📌 Delete spam or inappropriate content
4. 👥 Welcome new community members
5. 🎨 Maintain the peaceful aesthetic

## Next Steps

1. **Customize the Site:**
   - Edit `templates/base.html` to change colors/fonts
   - Add your own logo/branding
   - Customize the home page text

2. **Add More Categories:**
   - Create categories that match your community
   - Make category descriptions engaging

3. **Deploy to Production:**
   - Set `DEBUG = False` in settings.py
   - Use a production database (PostgreSQL recommended)
   - Set up HTTPS
   - Configure allowed hosts

4. **Backup Your Data:**
   - Regularly backup `db.sqlite3`
   - Export categories and posts

## Project Structure Quick Reference

```
📂 mysite/
├── 📄 manage.py           - Django command line
├── 📄 db.sqlite3          - Database (SQLite)
├── 📄 README.md           - Full documentation
├── 📄 requirements.txt     - Python dependencies
├── 📄 run.bat/run.sh      - Quick start scripts
│
├── 📂 mysite/             - Project settings
│   ├── settings.py        - Configuration
│   └── urls.py            - URL routing
│
├── 📂 accounts/           - User accounts
├── 📂 writings/           - Writing posts
├── 📂 comments/           - Comments system
├── 📂 core/               - Home/about pages
│
├── 📂 templates/          - HTML files
│   ├── base.html          - Main template
│   ├── 📂 accounts/       - Login/register
│   ├── 📂 writings/       - Posts
│   └── 📂 core/           - Home/about
│
└── 📂 static/             - CSS/JS files
    └── 📂 css/            - Stylesheets
```

## Getting Help

### View the code:
- Check `views.py` in each app to understand how features work
- Look at `models.py` to understand data structure
- Review `urls.py` to see available routes

### Common URLs:
- `/` - Home page
- `/accounts/register/` - Sign up
- `/accounts/login/` - Log in
- `/accounts/dashboard/` - Your dashboard
- `/writings/` - All writings
- `/writings/create/` - Write new piece
- `/about/` - About page
- `/admin/` - Admin panel

---

**Happy Writing! Feel free to customize and expand this platform to match your vision.** ✨
