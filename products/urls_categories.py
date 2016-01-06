from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', CategoryListView.as_view(), name='categories'),
    url(r'^(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category_detail'),

]

# urlpatterns = [
#     url(r'^(?P<id>\d+)', 'products.views.product_detail_view_func', name='product_detail_function'),
# ]