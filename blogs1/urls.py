

from rest_framework.routers import DefaultRouter

from .views import BlogView, PostCommentView, PostLikeView

app_name = 'blogs1'

router = DefaultRouter()

router.register('posts',BlogView,basename='bloglist')
router.register('comment',PostCommentView,basename='comment')
router.register('reaction',PostLikeView,basename='reaction')


urlpatterns = router.urls