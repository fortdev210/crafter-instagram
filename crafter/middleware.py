class InstagramMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        access_token = None
        user_id = None

        if 'access_token' in request.session:
            access_token = request.session['access_token']
            user_id = request.session['user_id']
        # Add the access_token and user_id to the request object
        request.access_token = access_token
        request.user_id = user_id

        response = self.get_response(request)

        return response
