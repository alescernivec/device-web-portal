from django import forms

class DeviceForm(forms.Form):
    device_name = forms.CharField(required=False)
    device_desc = forms.CharField(required=False)
    create_date = forms.CharField(required=False)
    rs232_settings = forms.CharField(required=False)
    last_sent_command = forms.CharField(required=False)
    command_to_send = forms.CharField(widget=forms.Textarea)
