from django.urls import path
from rest_framework.routers import SimpleRouter

from store.views import BookViewSet, UserBookRelationView

router = SimpleRouter()
router.register('book', BookViewSet)
router.register('book-relation', UserBookRelationView)

urlpatterns = []

urlpatterns += router.urls
