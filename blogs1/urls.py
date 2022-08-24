

from rest_framework.routers import DefaultRouter

from .views import BlogView, PostCommentView, PostLikeView, ReplyToCommentView

app_name = 'blogs1'

router = DefaultRouter()

router.register('posts',BlogView,basename='bloglist')
router.register('comment',PostCommentView,basename='comment')
router.register('reaction',PostLikeView,basename='reaction')
router.register('reply_to_comment',ReplyToCommentView,basename='reply_to_commmnet')


urlpatterns = router.urls