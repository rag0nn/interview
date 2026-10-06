from django.db import models


class ServiceRequest(models.Model):
	class Service(models.TextChoices):
		WEBSITE = 'website', 'Web sitesi tasarımı ve geliştirme'
		BACKEND = 'backend', 'Backend ve API geliştirme'
		CONSULTING = 'consulting', 'Teknik danışmanlık'
		AUTOMATION = 'automation', 'Süreç otomasyonu'

	name = models.CharField('Ad soyad', max_length=100)
	email = models.EmailField('E-posta', max_length=254)
	service = models.CharField('Hizmet', max_length=20, choices=Service.choices)
	description = models.TextField('Proje açıklaması', max_length=1500)
	created_at = models.DateTimeField('Oluşturulma tarihi', auto_now_add=True)

	class Meta:
		ordering = ['-created_at']
		verbose_name = 'Hizmet talebi'
		verbose_name_plural = 'Hizmet talepleri'

	def __str__(self):
		return f'{self.name} — {self.get_service_display()}'
