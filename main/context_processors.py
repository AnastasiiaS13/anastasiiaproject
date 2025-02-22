from .models import ContactInfo

def contact_info(request):
    data=ContactInfo.objects.first()

    if data:
        return {
            'location' : data.location,
            'number' : data.number,
            'email' : data.email,
            'text' : data.text,
            'opening_hours' : data.opening_hours,

            'facebook_link' : data.facebook_link,
            'twitter_link' : data.twitter_link,
            'linkedin_link' : data.linkedin_link,
            'instagram_link' : data.instagram_link,
            'pinterest_link' : data.pinterest_link,
        }
    return {
        'location': '',
        'number': '',
        'email': '',
        'text': '',
        'opening_hours': '',

        'facebook_link': '',
        'twitter_link': '',
        'linkedin_link': '',
        'instagram_link': '',
        'pinterest_link': '',
    }