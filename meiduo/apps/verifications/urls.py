from django.urls import path, register_converter
from apps.verifications.views import ImageCodeView,SmsCodeView
from utils.converters import MobileConverter

#register_converter(MobileConverter, 'mobile')
urlpatterns = [
    path('image_codes/<uuid>/',ImageCodeView.as_view()),
    path('sms_codes/<mobile:mobile>/',SmsCodeView.as_view()),


]