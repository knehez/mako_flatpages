
copy folder

### settings.py

INSTALLED_APPS add 'django.contrib.sites',
SITE_ID = 1

INSTALLED_APPS add 'mako_flatpages',
MIDDLEWARE_CLASSES add 'mako_flatpages.middleware.FlatpageFallbackMiddleware',

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")


```sh
python manage.py syncdb
```

```sh
python manage.py migrate
```

create templates/flatpages/default.html.mako


## django use mako


### views.py

```python
from mako.template import Template
from mako.lookup import TemplateLookup
from django.http import HttpResponse

...

def home(request):
	...
	lookup = TemplateLookup(directories=[settings.TEMPLATES_DIR])

	t = lookup.get_template("flatpages/def_site.html.mako")
	
	rendered = t.render(content="apple")
	return HttpResponse(rendered)
...
```
	
	
	
### templates/flatpages/default.html.mako
```html
<%inherit file="../1.mako"/>

${flatpage.content
```

### templates/1.mako

```html
<html>
    <body>
        <div class="header">
            <%block name="header"/>
        </div>

        ${self.body()}

        <div class="footer">
            <%block name="footer">
                this is the footer
            </%block>
        </div>
    </body>
</html>
```