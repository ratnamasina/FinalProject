from django import forms
from device.models import user, phone_brand, phone_modell, phone_feature, phone_feature_v, tab_brand, tab_modell, \
    tab_feature, tab_feature_v, watch_brand, watch_modell, watch_feature, watch_feature_v


class userform(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'email_id', 'password']


class phonebrandform(forms.ModelForm):
    class Meta:
        model = phone_brand
        fields = ['phone_brand_id', 'phone_brand_name']


class phonemodellform(forms.ModelForm):
    class Meta:
        model = phone_modell
        fields = ['phone_model_id', 'phone_model_name','phone_Img','phone_brand_id']


class phonefeatureform(forms.ModelForm):
    class Meta:
        model = phone_feature
        fields = ['phone_feature_id', 'phone_feature_name', 'phone_brand_id']


class phonefeaturevform(forms.ModelForm):
    class Meta:
        model = phone_feature_v
        fields = ['phone_featuree_id', 'phone_feature_v_value', 'phone_brand_id', 'phone_model_id', 'phone_feature_id']


class tabbrandform(forms.ModelForm):
    class Meta:
        model = tab_brand
        fields = ['tab_brand_id', 'tab_brand_name']


class tabmodellform(forms.ModelForm):
    class Meta:
        model = tab_modell
        fields = ['tab_model_id', 'tab_model_name','tab_Img', 'tab_brand_id']


class tabfeatureform(forms.ModelForm):
    class Meta:
        model = tab_feature
        fields = ['tab_feature_id', 'tab_feature_name', 'tab_brand_id']


class tabfeaturevform(forms.ModelForm):
    class Meta:
        model = tab_feature_v
        fields = ['tab_featuree_id', 'tab_feature_v_value', 'tab_brand_id', 'tab_model_id', 'tab_feature_id']


class watchbrandform(forms.ModelForm):
    class Meta:
        model = watch_brand
        fields = ['watch_brand_id', 'watch_brand_name']


class watchmodellform(forms.ModelForm):
    class Meta:
        model = watch_modell
        fields = ['watch_model_id', 'watch_model_name','watch_Img', 'watch_brand_id']


class watchfeatureform(forms.ModelForm):
    class Meta:
        model = watch_feature
        fields = ['watch_feature_id', 'watch_feature_name', 'watch_brand_id']


class watchfeaturevform(forms.ModelForm):
    class Meta:
        model = watch_feature_v
        fields = ['watch_featuree_id', 'watch_feature_v_value', 'watch_brand_id', 'watch_model_id', 'watch_feature_id']
