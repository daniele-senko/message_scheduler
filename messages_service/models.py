from django.db import models

# Create your models here.
class Message(models.Model):
    #opções para o campo 'type' (email, sms, whatsapp)

    TYPE_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('whatsapp', 'WhatsApp'),
    ]

    #opções para o campo 'status'
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
    ]

    #não é necessário criar o id, pois o django cria

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    content = models.TextField() #para textos longos 

    scheduled_at = models.DateTimeField() #data/hora agendamento

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True) #gera a hora atual da criação

    def __str__(self):
        return f"{self.type} - {self.scheduled_at}"