from django.template import TemplateDoesNotExist

TEMPLATES = {}

def register_template(name, template):
    global TEMPLATES
    TEMPLATES[name] = template

def load_template_source(template_name, template_dirs=None):
    if TEMPLATES.has_key(template_name):
        return (TEMPLATES[template_name], None)
    else:
        raise TemplateDoesNotExist

load_template_source.is_usable = True
