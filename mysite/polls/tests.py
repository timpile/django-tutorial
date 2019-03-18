import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question

def create_question(question_text, days):
  """
  Create a question with the give `question_text` and published the
  given number of `days` offset to now (negative for questions published
  in the past, positive for questions published in the future).
  """
  time = timezone.now() + datetime.timedelta(days=days)
  return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTest(TestCase):

  def test_no_questions(self):
    """
    If no questions exist, an appropriate message is displayed
    """
    response = self.client.get(reverse('polls:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No polls are available.")
    self.assertQuerysetEqual(response.context['latest_question_list'], [])
  
  def test_past_questions(self):
    """
    Question with pub_date in the past are displayed on the
    index page.
    """
    create_question(question_text="Past question.", days=-30)
    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['latest_question_list'],
      ['<Question: Past question.>']
    )

  def test_future_question(self):
    """
    Question with pub_date in the future aren't displayed on the
    index page.
    """
    create_question(question_text="Future question.", days=30)


class QuestionModelsTest(TestCase):

  def test_was_published_recently_with_future_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is in the future.
    """
    future_question = create_question("Future question", 30)
    self.assertIs(future_question.was_published_recently(), False)

  def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is more than 1 day old.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

  def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions who pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
