from .models import User


def current_user(request):
    """Injects current_user into every template automatically."""
    user_id = request.session.get('user_id')
    if not user_id:
        return {'current_user': None}
    try:
        user = User.objects(id=user_id).first()
        return {'current_user': user}
    except Exception:
        return {'current_user': None}
