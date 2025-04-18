from captcha.fields import CaptchaField
from django.forms import Form
class Mycaptcha(Form):
    cap=CaptchaField()