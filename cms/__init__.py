from django.template import TemplateDoesNotExist

TEMPLATES = {}

def register_template(name, template):
    TEMPLATES[name] = template

def load_template_source(template_name, template_dirs=None):
    if template_name in TEMPLATES:
        return (TEMPLATES[template_name], None)
    else:
        raise TemplateDoesNotExist

load_template_source.is_usable = True
