from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Orders,name="Orders"),
	url(r'^List_Product/$',List_Product,name="List_Product"),
	url(r'^Send_Order/$',Send_Order,name="Send_Order"),
	url(r'^Activate_Client/$',Activate_Client,name="Activate_Client"),
]