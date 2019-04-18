# from django.urls import path

# from . import views

# app_name='sec_guard'

# urlpatterns=[
# 		path('', views.index, name='index'),
# 		path('new_entry', views.new_entry, name='new_entry'),
# 		path('search_by_phone', views.search_by_phone, name='search_by_phone'),
# 		path('detail', views.detail, name='detail'),
# ]




from django.urls import path
from .apiviews import PackageDetailUpdate, PackageCreate

urlpatterns = [
    path("sec_guard/", PackageCreate.as_view(), name="package_create"),
    path("sec_guard/<pk>/", PackageDetailUpdate.as_view(), name="package_detail_update"),
]