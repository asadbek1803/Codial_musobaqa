from django.urls import path, include
from .views import QuestionList, RegisterView, LoginWithTokenView, TestAnalytics
urlpatterns = [
    path("questions/", QuestionList.as_view(), name="question-list"),
    path("regstration/", RegisterView.as_view(), name="register"),
    path("login/", LoginWithTokenView.as_view(), name="login"),
    # path("test-analyz/", TestAnalytics.as_view(), name="test-analytics")



]