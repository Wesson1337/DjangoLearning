from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from users.forms import AuthForm


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вы успешно вошли в систему')
                else:
                    auth_form.add_error('__all__', 'Ошибка. Учетная запись пользователя не активна!')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина и пароля.')
    else:
        auth_form = AuthForm()
    contex = {
        'form': auth_form
    }
    return render(request, 'users/login.html', context=contex)


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


def main(request):
    return render(request, 'users/main.html')


def logout_view(request):
    logout(request)
    return HttpResponse('Вы успешно вышли')