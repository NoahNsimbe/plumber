from django.test import TestCase, Client
from django.urls import reverse
import datetime

from users.models import User, Clients, Plumber


class UserModelTest(TestCase):

    user = dict({
        "first_name": "Test",
        "last_name": "Test",
        "email": "test@gmail.com",
        "password": "password"
    })

    def setUp(self) -> None:
        self.db_user = User.objects.create(**self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.db_user), f'{self.user["first_name"]} {self.user["last_name"]}')


class ClientsModelTest(TestCase):

    user = dict({
        "first_name": "Test",
        "last_name": "Test",
        "email": "test@gmail.com",
        "password": "password"
    })

    clients = dict({
            "user": ""
        })

    def setUp(self) -> None:
        self.db_user = User.objects.create(**self.user)

        self.clients["user"] = self.db_user

        self.db_client = Clients.objects.create(**self.clients)

    def test_string_representation(self):
        self.assertEqual(str(self.db_client), str(self.clients["user"]))


class PlumberModelTest(TestCase):

    user = dict({
        "first_name": "Test",
        "last_name": "Test",
        "email": "test@gmail.com",
        "password": "password"
    })

    plumber = dict({
            "user": "",
            "location": "plumber location",
            "phone": "+256700000"
        })

    def setUp(self) -> None:
        self.db_user = User.objects.create(**self.user)

        self.plumber["user"] = self.db_user

        self.db_plumber = Plumber.objects.create(**self.plumber)

    def test_string_representation(self):
        self.assertEqual(str(self.db_plumber), str(self.plumber["user"]))

# class ArticlesViewSetTest(TestCase):
#
#     article = dict({
#             "author_name": "Noah",
#             "title": "New Heavens",
#             "read_time": datetime.timedelta(seconds=60),
#             "bait": "Thinking about it",
#             "body": "Ouch...got nothing to say",
#             "featured": True,
#             "topic": "ANNOUNCEMENTS"
#         })
#
#     def setUp(self) -> None:
#         self.client = Client()
#         self.api_version = settings.REST_FRAMEWORK['DEFAULT_VERSION']
#
#         Articles.objects.create(**self.article)
#
#     def test_articles_view_set_list(self):
#         """GET / returns a list of articles"""
#         url = reverse("articles-list", args=(self.api_version,))
#
#         response = self.client.get(url)
#         number_of_articles = len(response.json())
#
#         self.assertEqual(response.status_code, 200, f'Expected 200 OK. got: {response.status_code}')
#         self.assertGreaterEqual(number_of_articles, 1, f'Expected at least 1 article. got: {number_of_articles}')
#
#         search_url = url + "?search=noah"
#         search_response = self.client.get(search_url)
#         search_count = search_response.data["count"]
#
#         self.assertEqual(search_response.status_code, 200, f'Expected 200 OK. got: {response.status_code}')
#         self.assertGreaterEqual(search_count, 1, f'Expected at least 1 article. got: {search_count}')
#
#     def test_articles_view_set_clap(self):
#         """POST /make a clap to an article"""
#
#         last_saved_article = Articles.objects.last()
#
#         url = reverse("articles-detail", args=(self.api_version, last_saved_article.id))
#
#         response = self.client.patch(url, data=None, content_type='application/json')
#         number_of_claps = response.data["claps"]
#
#         self.assertEqual(response.status_code, 200, f'Expected 200 OK. got: {response.status_code}')
#         self.assertEqual(number_of_claps, 1, f'Expected 1 clap. got: {number_of_claps}')
#
#         fail_response = self.client.patch(url, data=None, content_type='application/json')
#         self.assertEqual(fail_response.status_code, 400, f'Expected 400. got: {fail_response.status_code}')
#
#         updated_article = Articles.objects.get(id=last_saved_article.id)
#
#         self.assertEqual(fail_response.data["claps"], updated_article.claps, f'Expected claps not to increase')
#
#     def test_articles_view_featured(self):
#         """ Only one article can be featured at a time """
#
#         articles = [
#             dict({
#                 "author_name": "Noah",
#                 "title": "New Heavens",
#                 "read_time": datetime.timedelta(seconds=60),
#                 "bait": "Thinking about it",
#                 "body": "Ouch...got nothing to say",
#                 "featured": True,
#                 "topic": "ANNOUNCEMENTS"
#             }),
#             dict({
#                 "author_name": "Noah",
#                 "title": "New Heavens",
#                 "read_time": datetime.timedelta(seconds=60),
#                 "bait": "Thinking about it",
#                 "body": "Ouch...got nothing to say",
#                 "featured": True,
#                 "topic": "ANNOUNCEMENTS"
#             }),
#             dict({
#                 "author_name": "Noah",
#                 "title": "New Heavens",
#                 "read_time": datetime.timedelta(seconds=60),
#                 "bait": "Thinking about it",
#                 "body": "Ouch...got nothing to say",
#                 "featured": True,
#                 "topic": "ANNOUNCEMENTS"
#             })
#         ]
#
#         for article in articles:
#             Articles.objects.create(**article)
#
#         featured_article = Articles.objects.all().filter(featured=True)
#
#         self.assertEqual(featured_article.count(), 1, f'Expected 1 article. got: {featured_article.count()}')
#
#     def test_articles_view_search(self):
#         """ GET / returns a list of articles from a search """
#
#         articles = [
#             dict({
#                 "author_name": "Noah",
#                 "title": "New Heavens",
#                 "read_time": datetime.timedelta(seconds=60),
#                 "bait": "Thinking about it",
#                 "body": "Ouch...got nothing to say",
#                 "featured": True,
#                 "topic": "ANNOUNCEMENTS"
#             }),
#             dict({
#                 "author_name": "Yusuf",
#                 "title": "Amazing bird",
#                 "read_time": datetime.timedelta(seconds=60),
#                 "bait": "Thinking about it",
#                 "body": "Ouch...got nothing to say",
#                 "featured": True,
#                 "topic": "BEHIND THE SCENES"
#             }),
#             dict({
#                 "author_name": "John",
#                 "title": "New Heavens",
#                 "read_time": datetime.timedelta(seconds=60),
#                 "bait": "Thinking about it",
#                 "body": "Ouch...got nothing to say",
#                 "featured": True,
#                 "topic": "BEHIND THE SCENES"
#             })
#         ]
#
#         for article in articles:
#             Articles.objects.create(**article)
#
#         author_url = reverse("articles-list", args=(self.api_version,)) + "?author_name=Noah"
#
#         response = self.client.get(author_url)
#         number_of_articles = len(response.json())
#
#         self.assertGreaterEqual(number_of_articles, 1, f'Expected at least 1 article. got: {number_of_articles}')
#
#         topic_url = reverse("articles-list", args=(self.api_version,)) + "?topic=BEHIND"
#
#         topic_response = self.client.get(topic_url)
#         number_of_articles_by_topic = len(topic_response.json())
#
#         self.assertGreaterEqual(number_of_articles_by_topic, 1,
#                                 f'Expected at least 1 article. got: {number_of_articles_by_topic}')
#
#         search_topic = "Doesnt"
#
#         topic_url_null = reverse("articles-list", args=(self.api_version,)) + f"?topic={search_topic}"
#
#         topic_response_null = self.client.get(topic_url_null)
#
#         topic = topic_response_null.json()["topic"]
#
#         self.assertEqual(topic, [f'Select a valid choice. {search_topic} is not one of the available choices.'])
#
#
# class FaqsViewSetTest(TestCase):
#
#     faq = dict({
#             "title": "title",
#             "summary": "summary",
#             "body": "body"
#         })
#
#     def setUp(self) -> None:
#         self.client = Client()
#         self.api_version = settings.REST_FRAMEWORK['DEFAULT_VERSION']
#
#         Faqs.objects.create(title=self.faq["title"],
#                             summary=self.faq["summary"],
#                             body=self.faq["body"])
#
#     def test_faqs_view_set_list(self):
#         """GET / returns a list of faqs"""
#         url = reverse("faqs-list", args=(self.api_version,))
#
#         resp = self.client.get(url)
#         number_of_faqs = len(resp.json())
#
#         self.assertEqual(resp.status_code, 200, f'Expected 200 OK. got: {resp.status_code}')
#         self.assertGreaterEqual(number_of_faqs, 1, f'Expected at least 1 faq. got: {number_of_faqs}')
