# from django.contrib.auth import logout
# from django.shortcuts import render, redirect
#
# # Create your views here.
#
#
# from .forms import CustomUserCreationForm, CustomUserLoginForm
#
#
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login')
#         else:
#             form = CustomUserCreationForm()
#         return render(request,'registration/register.html',{'form':form})
#
#
# def login(request):
#     logout(request)
#     return redirect('login')
