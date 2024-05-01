import datetime
import json
import logging
from os import environ
import godspeed_api
import unittest


class TestAPI(unittest.TestCase):
    def setUp(self):
        super().setUp()

        logging.basicConfig(level=logging.DEBUG)
        self.login = environ["GODSPEED_LOGIN"]
        self.password = environ["GODSPEED_PASS"]

    def test_login(self):
        api = godspeed_api.API(self.login, self.password)

    def test_create_task(self):
        api = godspeed_api.API(self.login, self.password)

        due_at = datetime.datetime.now() + datetime.timedelta(days=1)

        api.create_task(
            "Test task for testing",
            notes="This is a test task",
            due_at=due_at,
            # TODO: Uncomment after api either allows for new tags here or returns an error
            # label_names=["test"],
        )

    def test_list_tasks(self):
        api = godspeed_api.API(self.login, self.password)

        result = api.list_tasks()

        for task in result.tasks:
            print(task.title)

    def test_update_task(self):
        api = godspeed_api.API(self.login, self.password)

        result = api.list_tasks().tasks[0]

        print(f"Updating task {result.title}")
        api.update_task(
            result.id,
            title=result.title + " [Upd]",
            due_at=datetime.datetime.now() + datetime.timedelta(days=1),
        )
