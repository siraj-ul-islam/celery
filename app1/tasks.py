from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(name="add_2_number_task")
def add(x, y):
    logger.info("add 2 numbers")
    return x + y
