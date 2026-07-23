import flet as ft
from models import User, Event, Tag, AttendanceRecord, AbsenceRequest

from views.calendar_view import CalendarView


def main(page: ft.Page):
    page.title = "Band Attendance"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    current_user = None  # Replace with login later

    calendar = CalendarView(
        page,
        current_user
    )

    page.add(
        calendar
    )

    calendar.render_calendar()


ft.run(main)
