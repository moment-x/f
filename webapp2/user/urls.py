from django.conf.urls import url


from user.api import entry

urlpatterns = [
    url(r'^signup/$', entry.sign_up),
    url(r'^signin/$', entry.sign_in_with_feed),
    url(r'^signout/$', entry.sign_out),
    url(r'^resetpw/$', entry.reset_password_login),
    url(r'^update/$', entry.update_user_info),
    url(r'^add/$', entry.add_friend),
    url(r'^react/$', entry.react_friend),
    url(r'^validate/$', entry.validate),
]
