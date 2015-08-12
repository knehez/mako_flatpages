In your Django application directory launch: 

```sh
git clone https://github.com/knehez/mako_flatpages.git
```

### Configure settings.py

Add two modules required:

```python
INSTALLED_APPS = (
	...,
	'django.contrib.sites',
	'mako_flatpages',
)
# add SITE_ID = 1 as well
SITE_ID = 1
```

Among MIDDLEWARE_CLASSES add 'mako_flatpages.middleware.FlatpageFallbackMiddleware',

```python
MIDDLEWARE_CLASSES = (
	...,
	'mako_flatpages.middleware.FlatpageFallbackMiddleware',
)
# if not exists add the following:
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
```

Launch manage.py tasks:

```sh
python manage.py syncdb
```

```sh
python manage.py migrate
```

create file:
### templates/flatpages/default.html.mako
```html
# my mako template in a flat page:
${flatpage.content}
```

In you view.py wher you would like to use this make_flatpages use the following:
### views.py example

```python
from mako.template import Template
from mako.lookup import TemplateLookup
from django.http import HttpResponse

...

def home(request):
	...
	lookup = TemplateLookup(directories=[settings.TEMPLATES_DIR])
    
    # reference for your template
	t = lookup.get_template("flatpages/def_site.html.mako")
	
	# apply template
	rendered = t.render(content="apple")
	
	return HttpResponse(rendered)
...
```
	
### admin interface is available here: http://127.0.0.1:8000/admin/mako_flatpages/flatpage/
