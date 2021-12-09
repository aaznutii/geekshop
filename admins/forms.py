from auth_app.forms import UserRegisterForm, UserProfileForm
from django import forms
from auth_app.models import User
from products.models import Product, ProductCategory

class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

class UserAdminProfileForm(UserProfileForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['username'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

class CategotyAdminForm(forms.ModelForm):
    name = forms.TextInput()
    description = forms.TextInput()
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategotyAdminForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ProductsForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all())
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'category':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductUpdate(ProductsForm):
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all().select_related(),
                                      empty_label=None)
    image = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'category':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'