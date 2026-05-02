from django.contrib.auth.mixins import AccessMixin,LoginRequiredMixin
from django.http import JsonResponse

'''class LoginRequiredJSONMixin(AccessMixin):
    def dispach(self,request):
        if not request.user.is_authenticated:
            return JsonResponse({'code':400,'errmsg':'没有登入'})
        return super().dispach(request)'''

class LoginRequiredJSONMixin(LoginRequiredMixin):

    def handle_no_permission(self):
        return JsonResponse({'code':400,'errmsg':'没有登入'})