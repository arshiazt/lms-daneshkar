def site_defaults(request):

    return {
        'site_name':'lms daneshkar',
        'site_description':'Django Website',
        'is_instructor': request.user.is_authenticated and request.user.profile.role == 'instrauctor'
    }