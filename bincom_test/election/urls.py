from django.urls import path
from .views import index, UnitResultView, LGAResultView, AddPollResultView

urlpatterns = [
    path('', index, name='home'),
    path('unit', UnitResultView.as_view(), name='unit'),
    path('lga', LGAResultView.as_view(), name='lga'),
    path('new_result', AddPollResultView.as_view(), name='new_result'),
]
