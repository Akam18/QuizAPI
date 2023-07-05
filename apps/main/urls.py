from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, AnswerViewSet

router = DefaultRouter()

router.register('quiz', QuizViewSet)
router.register('question', QuestionViewSet)
router.register('answer', AnswerViewSet)

urlpatterns = router.urls
