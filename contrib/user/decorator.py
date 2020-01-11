from contrib.models import User


# FIXME: define as decorator
# FIXME: dla danego uzytkownika?
def auth_verify(session, request, username=None):
    auth_tokens = []

    if request.cookies.get("auth_token") is not None:
        auth_tokens.append(request.cookies.get("auth_token"))
    if request.args is not None and "auth_token" in request.args:
        auth_tokens.append(request.args["auth_token"])
    if request.json is not None and "auth_token" in request.json:
        auth_tokens.append(request.json["auth_token"])

    for auth_token in auth_tokens:
        user = User.verify_auth_token(session, auth_token)
        if (user and username is None) or (user.username == username
                                           and username is not None):
            return True

    return False
