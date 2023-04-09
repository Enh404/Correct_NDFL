from django import forms
from .models import Report

class ReportForm(forms.Form):
    excel_file = forms.FileField(label='Загрузите файл Excel')