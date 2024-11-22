from cofre.models import Cofre
from django import forms
from django.contrib import admin
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from .utils import criptografar
from .utils import descriptografar


@admin.register(Cofre)
class CofreAdmin(admin.ModelAdmin):
    list_display = ("descricao", "usuario", "senha_descriptografada")
    list_display_links = ("descricao",)
    search_fields = ("id", "descricao", "usuario")
    readonly_fields = ("senha_descriptografada",)

    fieldsets = (
        (
            "Identificação",
            {
                "fields": ("descricao",),
            },
        ),
        (
            "Local",
            {
                "classes": ("",),
                "fields": (("hostname", "ip"), "url", "obs"),
            },
        ),
        (
            "Credenciais",
            {
                "classes": ("",),
                "fields": (("usuario", "senha_descriptografada"), "senha"),
            },
        ),
    )

    @admin.display(
        description="Senha descriptografada",
    )
    def senha_descriptografada(self, obj):
        try:
            senha = descriptografar(str(obj.senha))
        except:  # noqa: E722
            senha = obj.senha
        # Gerar HTML seguro a partir de um template
        html = render_to_string(
            "cofre/copy_password.html",
            {"senha": senha, "obj_id": obj.id},
        )
        return mark_safe(html)  # noqa: S308

    def get_form(self, request, obj=None, **kwargs):
        """Preencher a senha criptografada no campo com type `password`"""
        form = super().get_form(request, obj, **kwargs)
        if obj:
            form.base_fields["senha"] = forms.CharField(
                label="Senha",
                required=True,
                widget=forms.PasswordInput(attrs={"value": obj.senha}),
            )
        return form

    def save_model(self, request, obj, form, change):
        # Se o campo de senha for alterado, criptografar
        if "senha" in form.changed_data:
            obj.senha = criptografar(str(obj.senha))

        super().save_model(request, obj, form, change)
