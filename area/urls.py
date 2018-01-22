from django.conf.urls import include, url
from django.contrib import admin
from area import views
urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', admin.site.urls)),
    url(r'^show_area/$', views.show_area), # 省市县案例
    # url(r'^show_area/(\d+)/$', views.parent_area),  # 自关联案例`
    url(r'^base/$', views.base),
    url(r'^child/$', views.child),
    url(r"^upload_pic/$",views.upload_pic),
    url(r"^upload_addr/$", views.upload_addr),
    url(r"^provice_area/(\d*)/?$",views.provice_area),
    url(r"^prov/$",views.get_prov),
    url(r"^city/(\d+)/$", views.get_city),
    url(r"^dis/(\d+)/$", views.get_city),

]
