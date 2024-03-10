from social_media.models import SocialMedia

def load_social_obj(request):
    social_objs = SocialMedia.objects.all()
    return {'social_objs': social_objs}