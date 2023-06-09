from app.common.pagination import CursorPagination


class MessagePagination(CursorPagination):
    page_size = 20
    ordering = "-created_at"
