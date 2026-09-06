from rest_framework.routers import DefaultRouter
from .views import ProblemViewSet , TestCaseViewSet , LanguageViewSet

router = DefaultRouter()
router.register('problems' , ProblemViewSet)
router.register('testcases' , TestCaseViewSet)
router.register('languages' , LanguageViewSet)


urlpatterns = router.urls
