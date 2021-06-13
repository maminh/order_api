from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.ProductView, 'products')

urlpatterns = router.urls