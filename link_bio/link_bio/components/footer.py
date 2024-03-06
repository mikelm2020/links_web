import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor
from link_bio.components.ant_components import float_button


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            height=Size.VERY_EXTRA_BIG.value,
            width=Size.VERY_EXTRA_BIG.value,
            alt="Logotipo de miguellopezmdev.",
        ),
        rx.link(
            rx.box(
                f"© 2020-{datetime.date.today().year} ",
                rx.span(
                    "miguellopezmdev by Miguel Angel López", color=Color.PRIMARY.value
                ),
                " v1.",
                padding_top=Size.DEFAULT.value,
            ),
            href=const.LOPEZ_DEV_URL,
            is_external=True,
            font_size=Size.MEDIUM.value,
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                ),
                rx.text(
                    "BACKEND DEVELOPER EN CIUDAD DE MEXICO",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value,
                ),
            ),
            href=const.REPO_URL,
            is_external=True,
        ),
        float_button(
            icon=rx.Image(src="/icons/donate.svg"),
            href=const.PAYPAL_ME_URL,
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.ZERO.value,
        color=TextColor.FOOTER.value,
    )
