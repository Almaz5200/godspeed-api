from enum import Enum
import json
from typing import List, Optional
from dacite import Config, from_dict
import requests
import datetime
import logging

from .Models.ListTasksResponse import ListTasksResponse
from .Models.Status import Status


class AuthError(Exception):
    def __init__(self):
        super().__init__("Failed to authenticate")


class Method(Enum):
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"


class API:
    def __init__(
        self,
        username: str,
        password: str,
        hostname: str = "https://api.godspeedapp.com",
    ):
        self.hostname = hostname
        self.token = None

        try:
            auth_result = self._send_request(
                "/sessions/sign_in",
                Method.POST,
                {
                    "email": username,
                    "password": password,
                },
            ).json()
            is_success = auth_result["success"] == True

        except:
            raise AuthError()

        if not is_success:
            raise AuthError()

        self.token = auth_result["token"]

    def create_task(
        self,
        title: str,
        list_id: Optional[str] = None,
        location: Optional[str] = None,
        notes: Optional[str] = None,
        due_at: Optional[datetime.datetime] = None,
        label_names: Optional[List[str]] = None,
    ) -> dict:
        str_date_time = due_at.strftime("%Y-%m-%dT%H:%M:%SZ") if due_at else None

        args = {
            "title": title,
            "list_id": list_id,
            "location": location,
            "notes": notes,
            "due_at": str_date_time,
            "label_names": label_names,
        }

        args = {k: v for k, v in args.items() if v is not None}

        return self._send_request("/tasks", Method.POST, args).json()

    def list_tasks(
        self,
        status: Optional[Status] = None,
        list_id: Optional[str] = None,
        updated_before: Optional[datetime.datetime] = None,
        updated_after: Optional[datetime.datetime] = None,
    ) -> ListTasksResponse:
        args = {
            "status": status.value if status else None,
            "list_id": list_id,
            "updated_before": self._stringify_datetime(updated_before),
            "updated_after": self._stringify_datetime(updated_after),
        }
        raw = self._send_request(
            "/tasks", Method.GET, {k: v for k, v in args.items() if v is not None}
        ).json()
        return from_dict(
            data_class=ListTasksResponse,
            data=raw,
            config=Config(type_hooks={datetime.datetime: self._parse_datetime}),
        )

    def update_task(
        self,
        task_id: str,
        title: Optional[str] = None,
        notes: Optional[str] = None,
        due_at: Optional[datetime.datetime] = None,
        starts_at: Optional[datetime.datetime] = None,
        is_complete: Optional[bool] = None,
    ):
        args = {
            "title": title,
            "notes": notes,
            "due_at": self._stringify_datetime(due_at),
            "starts_at": self._stringify_datetime(starts_at),
            "is_complete": is_complete,
        }
        args = {k: v for k, v in args.items() if v is not None}

        return self._send_request(f"/tasks/{task_id}", Method.PATCH, args).json()

    def _stringify_datetime(self, value: Optional[datetime.datetime]) -> Optional[str]:
        if not value:
            return None
        return value.isoformat()

    def _parse_datetime(self, value: str) -> Optional[datetime.datetime]:
        return datetime.datetime.fromisoformat(value)

    def _send_request(
        self,
        endpoint: str,
        method: Method,
        body: dict = {},
    ) -> requests.Response:
        headers = {}

        if self.token:
            headers["Authorization"] = "Bearer " + self.token

        if method == Method.POST:
            res = requests.post(self.hostname + endpoint, json=body, headers=headers)
        elif method == Method.PATCH:
            res = requests.patch(self.hostname + endpoint, json=body, headers=headers)
        elif method == Method.GET:
            res = requests.get(self.hostname + endpoint, data=body, headers=headers)

        logging.info(f"{method} {self.hostname + endpoint} {body} {res.status_code}")

        return res
