import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page


def populate():
    python_pages = [
        {'title' : 'Official Python Tutorial',
         'url' : 'http://docs.python.org/3/tutorial/',
         'views' : 10000-3},
        {'title' : 'How to Think like a Computer Scientist',
         'url' : 'http://www.greenteapress.com/thinkpython/',
         'views' : 10000-2},
        {'title' : 'Learn Python in 10 Minutes',
         'url' : 'http://www.korokithakis.net/tutorials/python/',
         'views' : 4},
    ]

    django_pages =[
        {'title': 'Official Django Tutorial',
         'url' : 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views' : 10000-1},
        {'title' : 'Django Rocks',
        'url' : 'http://www.djangorocks.com/',
        'views' : 10000-3},
        {'title' : 'How to Tango with Django',
         'url' : 'http://www.tangowithdjango.com/',
         'views' : 10000} ]
    
    other_pages = [
        {'title' : 'Bottle',
         'url' : 'http://bottlepy.org/docs/dev/',
         'views' : 2},
        {'title' : 'Flask',
         'url' : 'http://flask.pocoo.org',
         'views' : 1}
    ]

    cats = {'Python' : {'pages' : python_pages, 'views' : 128, 'likes' : 64},
            'Django' : {'pages' : django_pages, 'views' : 64, 'likes' : 32},
            'Other Frameworks' : {'pages' : other_pages, 'views' : 32, 'likes' : 16}}
    
    def add_page(cat, title, url, views=0):
        p = Page.objects.get_or_create(category=cat, title=title)[0]
        p.url = url
        p.views = views
        p.save()
        return p
    
    def add_cat(name, views, likes):
        category = Category.objects.get_or_create(name=name)[0]
        category.views = views
        category.likes = likes
        category.save()
        return category
    
    for cat, cat_data in cats.items():
        category = add_cat(cat, cat_data['views'], cat_data['likes'])
        for page in cat_data['pages']:
            add_page(category, page['title'], page['url'], page['views'])
    
    for category in Category.objects.all():
        for page in Page.objects.filter(category=category):
            print(f'- {category}: {page}')

    
    

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()