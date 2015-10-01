import ckanext.hdx_users.model as umodel
import ckan.logic as logic
import pylons.config as config

NotFound = logic.NotFound

def token_show(context, user):
    model = context['model']
    id = user.get('id')
    token_obj = umodel.ValidationToken.get(user_id=id)
    if token_obj is None:
        raise NotFound
    return token_obj.as_dict()


def token_show_by_id(context, data_dict):
    token = data_dict.get('token', None)
    token_obj = umodel.ValidationToken.get_by_token(token=token)
    if token_obj is None:
        raise NotFound
    return token_obj.as_dict()