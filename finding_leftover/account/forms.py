
from django.contrib.auth.models import User
from django import forms
from store.models import Store
from django import forms
from django.forms import ModelForm

from django.db import models
from betterforms.multiform import MultiModelForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# 회원가입 기능을 위한 Form입니다.
class CreateUserForm(UserCreationForm):
    #password1,2는 form에서 선언된 필드입니다. 그 필드에서는 Meta.widgets가 적용될수 없습니다!
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password from numbers and letters of the Latin alphabet'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))
    
    class Meta:
        model = User
        fields = ('username', 'password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력 가능합니다.'}),
        } 
    
        
    # 생성한 user를 저장합니다.    
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user

# 회원가입할 때 store에 관한 정보도 한꺼번에 받아서 저장하기 위해서 StoreForm도 추가했습니다.
# Store Model은 post 앱에서 만들었습니다.(post/models.py)
class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('store_name', 'store_memo', 'store_image')
        widgets = {
            'store_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력 가능합니다.'}),
            #'store_address' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력 가능합니다.'}),
            'store_memo' : forms.Textarea(attrs={'class': 'form-control'}),
        }

# CreateUserForm과 StoreForm을 합치기 위해서 MultimodelForm을 사용했습니다
class UserCreationMultiForm(MultiModelForm):
    form_classes={
        'user' : CreateUserForm,
        'store' : StoreForm,
    }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']