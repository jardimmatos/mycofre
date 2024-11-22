from django.db import models


class Cofre(models.Model):
    descricao = models.CharField(
        max_length=254,
        verbose_name="Descrição",
        blank=False,
        default="",
    )
    hostname = models.CharField(
        max_length=254,
        verbose_name="Hostname",
        blank=True,
        default="",
    )
    ip = models.CharField(max_length=254, verbose_name="IP", blank=True, default="")
    url = models.CharField(max_length=254, verbose_name="Url", blank=True, default="")
    usuario = models.CharField(
        max_length=254,
        verbose_name="Usuário",
        blank=False,
        default="",
    )
    senha = models.CharField(
        max_length=254,
        verbose_name="Senha",
        blank=False,
        default="",
        help_text=(
            "Altere este campo somente se desejar alterar a senha."
            " O campo é criptografado após salvar."
        ),
    )
    obs = models.TextField(verbose_name="Observações", blank=True, default="")

    class Meta:
        verbose_name = "Registro de Cofre"
        verbose_name_plural = "Registros de Cofre"
        unique_together = ("descricao", "usuario")

    def __str__(self):
        return f"{self.descricao}"
