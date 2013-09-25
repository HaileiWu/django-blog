Function
----
A django blog App:

  1. Create/Edit blog post by admin site(markdown)
  2. Add blog tags
  3. Comment on a blog post
  4. Show month based blog archives
  5. Show tag based blog
  6. Raystack search
  7. Generate RSS feeds

ToDoList
----
  1. files/pictures upload
  2. Improve the existing functionality
  3. Interface rendering 
  4. ...

Use
---
  1. modify the database setting in the settings.py
  2. `pip install markdown pygments django-pagedown`
  3. `pip install django-haystack`
  4. `python manage.py rebuild_index`
  5. `python manage.py runserver`
  6. default admin site http://127.0.0.1:8000/admin
  7. default blog site http://127.0.0.1:8000/blog/articles
	
