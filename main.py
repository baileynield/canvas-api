import os
from fastapi import FastAPI

from dotenv import load_dotenv
import requests

from models import Course, Discussion

# /courses/:course_id/discussion_topics
# /courses

load_dotenv()

app = FastAPI()

access_token = os.getenv("ACCESS_TOKEN")

base_url = "https://dixietech.instructure.com/api/v1"

headers: dict[str, str] = {
    "Authorization": f"Bearer {access_token}"
}


@app.get("/courses")
async def list_course() -> list[Course]:
    response = requests.get(url=f"{base_url}/courses", headers=headers)
    r_json = response.json()

    courses: list[Course] = []
    for course_json in r_json:
        course = Course(id=r_json[0]["id"], name=r_json[0]["name"])
        courses.append(course)

    return courses

@app.get("/discussions")
async def get_discussions(course_id: int) -> list:
    response = requests.get(url=f"{base_url}/courses/{course_id}/discussion_topics", headers=headers)
    r_json = response.json()

    discussions: list[Discussion] = []
    for discussion_json in r_json:
        discussion = Discussion(id=discussion_json["id"], title=discussion_json["title"])
        discussions.append(discussion)

    return discussions