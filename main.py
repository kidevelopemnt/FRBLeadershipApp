import flet as ft
from models import User, Event, Tag, AttendanceRecord, AbsenceRequest

from views.calendar_view import CalendarView
from views.event_view import EventView


# FIXME: Bold attendance status text not changing (event_view.py)
# FIXME: No way to exit attendance (event_view.py)
# FIXME: Color not clearing when marking as Not Recorded (event_view.py)
# FIXME: Filter by tag still not working


async def main(page: ft.Page):
    page.title = "Band Attendance"

    current_user = User.objects.get(id=1)

    async def on_route_change(e: ft.RouteChangeEvent):

        page.controls.clear()

        if page.route == "/calendar":

            page.add(
                CalendarView(
                    page,
                    current_user
                )
            )

        elif page.route.startswith("/event/"):

            event_id = int(
                page.route.split("/")[-1]
            )

            event = Event.objects.get(id=event_id)

            page.add(
                EventView(
                    page,
                    current_user,
                    event
                )
            )

        page.update()

    page.on_route_change = on_route_change

    await page.push_route("/calendar")


ft.run(main)
