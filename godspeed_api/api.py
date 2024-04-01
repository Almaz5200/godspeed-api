from typing import List, Optional
import requests
import datetime


class AuthError(Exception):
    def __init__(self):
        super().__init__("Failed to authenticate")


class API:
    def __init__(
        self,
        username: str,
        password: str,
        hostname: str = "https://api.godspeedapp.com/",
    ):
        self.hostname = hostname

        try:
            auth_result = self._send_post_request(
                "/auth/login",
                {
                    "username": username,
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

        return self._send_post_request(
            "/tasks",
            {
                "title": title,
                "list_id": list_id,
                "location": location,
                "notes": notes,
                "due_at": str_date_time,
                "label_names": label_names,
            },
        ).json()

    def _send_post_request(
        self,
        endpoint: str,
        body: dict,
    ) -> requests.Response:
        headers = {}

        if self.token:
            headers["Authorization"] = "Bearer " + self.token

        return requests.request("POST", self.hostname + endpoint, json=body)
