from rest_framework.routers import DefaultRouter
from .views import (UserViewSet , 
    UniversityMemberViewSet , 
    StudentProfileViewSet , 
    TeacherProfileViewSet)

router = DefaultRouter()
router.register('users' , UserViewSet , basename = 'user')
router.register('university-member' , UniversityMemberViewSet)
router.register('student-profiles' , StudentProfileViewSet)
router.register('teacher-profiles' , TeacherProfileViewSet)

urlpatterns = router.urls
