import logging

from django.contrib import messages
from django.db import DatabaseError
from django.shortcuts import redirect, render

from .forms import ServiceRequestForm

logger = logging.getLogger(__name__)


def home(request):
	form = ServiceRequestForm(request.POST or None)
	submission_error = None

	if request.method == 'POST' and form.is_valid():
		try:
			form.save()
		except DatabaseError:
			logger.exception('Service request could not be saved.')
			submission_error = 'Talebiniz şu anda kaydedilemedi. Lütfen tekrar deneyin.'
		else:
			messages.success(request, 'Talebiniz ulaştı. En kısa sürede size dönüş yapacağım.')
			return redirect('requests_app:home')

	return render(request, 'requests_app/home.html', {
		'form': form,
		'submission_error': submission_error,
	})
