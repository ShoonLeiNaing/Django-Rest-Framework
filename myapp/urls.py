
from django.urls import path,include
from .views import article_list,article_detail,ArticleApiView,AricleDetailApiView,GenericListView,ArticleViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',ArticleViewSet,basename='article')


urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    path('article/', article_list,name="article"),
    path('articleapi/',ArticleApiView.as_view(),name="article api"),
    path('articledetailapi/<int:id>/',AricleDetailApiView.as_view(),name="article detail api"),
    path('article_detail/<int:pk>/',article_detail,name="article_detail"),
    path('generic/article/<int:id>/',GenericListView.as_view(),name="generic list view"),
    # path('generic/detail/<int:id>/',GenericDetailView.as_view(),name="generic detail view")

]
