import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.components.link_button import link_button
from link_bio.model.Live import Live


def header(details=True, live_status=Live(live=False, title="")) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                rx.cond(
                    live_status.live,
                    rx.link(
                        rx.avatar_badge(
                            rx.image(
                                src="/icons/twitch.svg",
                                height=Size.SMALL.value,
                                width=Size.SMALL.value,
                            ),
                            bg=Color.PURPLE.value,
                            border_color=Color.PURPLE.value,
                            class_name="blink",
                        ),
                        href=const.TWITCH_URL,
                        is_external=True,
                    ),
                ),
                name="Miguel Angel López Monroy",
                size="xl",
                src="/avatar.jpg",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.BORDER.value,
            ),
            rx.vstack(
                rx.heading("Miguel Angel López Monroy", size="lg"),
                rx.text(
                    "@miguellopezmdev",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value,
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub",
                    ),
                    link_icon(
                        "/icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X",
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn",
                    ),
                    spacing=Size.LARGE.value,
                ),
                align_items="start",
            ),
            spacing=Size.DEFAULT.value,
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience()}+",
                        "años de experiencia",
                    ),
                    rx.spacer(),
                    info_text(
                        "3+",
                        "años Python",
                    ),
                    rx.spacer(),
                    info_text(
                        "1",
                        "certificación AWS",
                    ),
                    width="100%",
                ),
                rx.cond(
                    live_status.live,
                    link_button(
                        "En directo",
                        live_status.title,
                        "/cons/twitch.svg",
                        const.TWITCH_URL,
                        highlight_color=Color.PURPLE.value,
                    ),
                ),
                rx.text(
                    f"""
            Soy ingeniero en Computación egresado de la UNAM y actualmente colaboro en el desarrollo de una API en un proyecto OpenSource
            para el control de Granjeros de conejos
            Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!
            """,
                    font_size=Size.DEFAULT.value,
                    color=TextColor.CONTENT.value,
                ),
                width="100%",
                spacing=Size.BIG.value,
            ),
        ),
        width="100%",
        spacing=Size.BIG.value,
        align_items="start",
    )


def experience() -> int:
    return datetime.date.today().year - 1997
