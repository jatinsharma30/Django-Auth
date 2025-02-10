from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(f"Received email: {email}")  # Debug print
        
        try:
            user = User.objects.get(email=email)
            print(f"Found user: {user.username}")  # Debug print
            
            # Generate token
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Create password reset link
            reset_link = f"{request.scheme}://{request.get_host()}/reset-password/{uid}/{token}/"
            print(f"Reset link generated: {reset_link}")  # Debug print
            
            subject = 'Password Reset Request'
            message = f'''
            Hello {user.username},
            
            You requested to reset your password. Please click the link below to reset it:
            
            {reset_link}
            
            If you didn't request this, please ignore this email.
            
            Thanks!
            '''
            
            try:
                print("Attempting to send email...")  # Debug print
                email_result = send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )
                print(f"Email send result: {email_result}")  # Debug print
                
                if email_result:
                    messages.success(request, 'Password reset email has been sent. Please check your inbox.')
                else:
                    messages.error(request, 'Failed to send reset email. Please try again.')
                
                return redirect('login')
                
            except Exception as e:
                print(f"Email sending failed with error: {str(e)}")  # Debug print
                messages.error(request, f'Failed to send reset email: {str(e)}')
        
        except User.DoesNotExist:
            print(f"No user found with email: {email}")  # Debug print
            messages.error(request, 'No user found with this email address.')
    
    return render(request, 'users/forgot_password.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')