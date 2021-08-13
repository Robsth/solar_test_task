from celery import shared_task

from django.utils import timezone

from .models import Site
from .services import get_site_availability


@shared_task
def refresh_site_statuses() -> None:
    """
    Обновление статуса сайта и времени опроса на основе его доступности
    """
    sites = Site.objects.all()
    for site in sites:
        site.last_ping_date = timezone.now()
        site.availability_status = get_site_availability(site.url)
        site.save()

