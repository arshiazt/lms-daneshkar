from django import template

from user.models import Profile

register = template.Library()


@register.simple_tag
def last_profiles(count=2):
    return Profile.objects.order_by("-created_at")[:count]
