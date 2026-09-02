from django import template

register = template.Library()


@register.filter(name="reverse_str")
def reverse_str(value):
    return value[::-1]


@register.filter(name="format_ir")
def format_ir(phone, delimiter="-"):
    if len(phone) != 11 or not phone.isdigit():
        return phone
    return f"{phone[:4]}{delimiter}{phone[4:7]}{delimiter}{phone[7:]}"
