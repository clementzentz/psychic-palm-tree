import datetime

from django.test import TestCase
from django.utils import timezone

from ..models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """ was_published_recently() returns False for 
            questions whose pub_date is in the future. """ 
        # future question
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question=Question(pub_date=future_time) 
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """ was_published_recently() returns False for 
        questions whose pub_date is older than 1 day. """
        # old question
        past_time = timezone.now() - datetime.timedelta(
            days=1, seconds=1)
        old_question = Question(pub_date=past_time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """ was_published_recently() returns True for 
        questions whose pub_date is within the last day. """
        # recent question
        time = timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)