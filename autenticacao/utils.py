import re
from django.contrib import messages
from django.contrib.messages import constants
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def password_is_valid(request, senha, confirmar_senha):
    if len(senha) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
        return False
    if not senha == confirmar_senha:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    if not re.search('[A-Z]', senha):
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter letra maiúscula')
        return False
    if not re.search('[a-z]', senha):
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter letra minúsculas')
        return False
    if not re.search('[1-9]', senha):
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter números')
        return False
    
    return True

def email_html(path_template: str, assunto: str, para: list, **kwargs) -> dict:
    
    
    html_content = render_to_string(path_template, kwargs)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, para)
    email.attach_alternative(html_content, "text/html")
    email.send()
    return {'status': 1}
