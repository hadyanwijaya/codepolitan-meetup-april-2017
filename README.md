API Web Development with Django Rest Framework + Celery
-------------------------------------------------------

Stack:

* Django
* Django Rest Framework
* MySQL
* Celery
* Redis

Requirements:

* reportlab
* celery
* djangorestframework
* django
* PyMySQL
* redis-py

Topic:

* Pengenalan
* Instalasi
* Membuat Model
* Membuat Halaman Admin
* Membuat API dengan Django Rest Framework (Serializer, ViewSet, Permission, URL, Authentication)
* Mengirim email dengan Celery Periodic Task
* Konversi artikel ke pdf dengan Celery dan ReportLab

Django Development Workflow:

* create project
* initial migration
* create super user
* create apps
* create model and admin
* attach apps to settings.py
* create serializer
* create viewsets
* set the rest framework setting
* add rest framework url
* run server

Problem selanjutnya:

* gak bisa update postingan
* cara biar field ga bisa diedit
* cara biar bisa nampilin output sesuai harapan tapi form console ga semua nampil misal field user ga perlu nampil di output comment

command:

$ ./manage.py runserver
$ celery -A myapp.celery:app worker -c 4  -B --loglevel=INFO
$ python -m smtpd -n -c DebuggingServer localhost:1025