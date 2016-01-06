from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^products/', include('products.urls')),
    url(r'^products/', include('products.urls', namespace="products")),
    url(r'^categories/', include('products.urls_categories', namespace="categories")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
