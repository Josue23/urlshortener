import random
import string
from django.conf import settings
# from shortener.models import KirrURL

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

# gerador de shortcode
def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for _ in range(size))


# instance é a instancia do modulo KirrURL
def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    # Getting the class direct from the KirrURL model
    # print(instance)
    # print(instance.__class__)
    # print(instance.__class__.__name__)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code