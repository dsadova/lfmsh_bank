from django.conf.urls import url
from django.contrib.auth import views as auth_views

from bank import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': 'bank/login.html', },
        name='login'),

    url(r'^my_transactions/$', views.my_transactions, name='my_transactions'),

    url(r'^students$', views.students, name='students'),
    url(r'^staff$', views.staff, name='staff'),

    url(r'^add_transaction/(?P<type_name>[a-z_2]+)/tmp(?P<from_template>[0-9]+)/$', views.add_transaction,
        name='add_transaction_from_template'),
    url(r'^add_transaction/(?P<type_name>[a-z_2]+)/upd(?P<update_of>[0-9]+)/$', views.add_transaction,
        name='update_transaction'),
    url(r'^add_transaction/(?P<type_name>.+)/$', views.add_transaction, name='add_transaction'),

    url(r'^user/(?P<username>.+)/$', views.user, name='user'),

    url(r'^decline_transaction/(?P<transaction_id>[0-9]+)/$', views.decline_transaction, name='decline_transaction'),

    url(r'^dec_trans_ok/(?P<trans_id>[0-9]+)/$', views.dec_trans_ok, name='trans_dec_ok'),

    url(r'^trans_list/(?P<username>.+)/$', views.trans_list, name='trans_list'),
    url(r'^meta_list/(?P<trans_id>.+)/$', views.meta_list, name='meta_list'),

    url(r'^trans_red/(?P<trans_id>.+)/$', views.trans_red, name='trans_red'),

    url(r'manage_p2p', views.manage_p2p, name='manage_p2p'),

    url(r'^super_table/$', views.super_table, name='super_table'),
    url(r'^media/$', views.media, name='media'),

]
