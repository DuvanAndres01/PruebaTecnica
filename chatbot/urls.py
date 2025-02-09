from django.urls import path, include
from .views import ComputadorListView, ChatBotView

urlpatterns = [
    path('computadores/', ComputadorListView.as_view(), name='computadores'),
    path('chatbot/', ChatBotView.as_view(), name='chatbot'),
]