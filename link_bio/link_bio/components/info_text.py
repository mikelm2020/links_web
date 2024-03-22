import reflex as rx
from link_bio.styles.styles import Size
from link_bio.styles.colors import TextColor


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            font_weight="bold",
            color=TextColor.HEADER.value,
        ),
        f" {body}",
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value,
    )
