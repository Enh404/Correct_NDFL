from django import forms

class ReportForm(forms.Form):
    excel_file = forms.FileField(label='Загрузите файл Excel')