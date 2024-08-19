from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError

# Create your views here.


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone")

    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error("first_name", ValidationError("Deu ruim ai ", code="invalid"))
        return super().clean()


def create(request):
    if request.method == "POST":
        context = {"form": ContactForm(request.POST)}
        return render(request, "contact/create.html", context)

    context = {"form": ContactForm()}

    return render(request, "contact/create.html", context)
