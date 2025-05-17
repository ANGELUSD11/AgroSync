from django.db import models

# Create your models here.

class Cosecha(models.Model):
    TIPOS_CULTIVO = [
        ('maiz', 'Maíz'),
        ('trigo', 'Trigo'),
        ('arroz', 'Arroz'),
        ('cafe', 'Café'),
        ('soya', 'Soya'),
        ('cebada', 'Cebada'),
        ('avena', 'Avena'),
        ('otro', 'Otro'),
    ]

    tipo_cultivo = models.CharField(
        max_length=20,
        choices=TIPOS_CULTIVO,
        default='otro'
    )
    cantidad_cosechada = models.DecimalField(
        max_digits=10,  # Hasta 99999999.99
        decimal_places=2,
        help_text="Cantidad en kilogramos"
    )
    fecha_siembra = models.DateField(null=True, blank=True)
    fecha_recoleccion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_tipo_cultivo_display()} - {self.cantidad_cosechada} kg"

    class Meta:
        verbose_name = "Cosecha"
        verbose_name_plural = "Cosechas"
        ordering = ['-fecha_recoleccion']