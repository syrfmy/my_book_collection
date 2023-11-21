
import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)



@csrf_exempt
def register(request):
    print(f"Request user: {request.user}")
    
    data = json.loads(request.body)
    name = data['username']
    passkey = data['password']
    
    try:
        user = User.objects.create_user(username=name, password=passkey)
        print("User created")
        return JsonResponse({
            "username": name,
            "status": "success",
            "message": "Pendaftaram akun berhasil!"
        }, status=200)
    except Exception as e:
        # Log the actual exception for debugging purposes
        print(f"Error creating user: {e}")
        return JsonResponse({
            "status": "gagal",
            "message": "Pendaftaran akun gagal."
        }, status=401)
