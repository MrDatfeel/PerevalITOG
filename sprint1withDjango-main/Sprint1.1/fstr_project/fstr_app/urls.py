from django.urls import path
from .views import SubmitDataView, GetSubmissionView, EditSubmissionView, GetUserSubmissionsView

urlpatterns = [
    path('submitData/', SubmitDataView.as_view(), name='submit_data'),  # Существующий маршрут
    path('submitData/<int:id>/', GetSubmissionView.as_view(), name='get_submission'),  # Получение записи по ID
    path('submitData/edit/<int:id>/', EditSubmissionView.as_view(), name='edit_submission'),  # Редактирование записи
    path('submitData/user/', GetUserSubmissionsView.as_view(), name='get_user_submissions'),  # Получение всех записей пользователя
]
