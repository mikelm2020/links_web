import reflex as rx

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://miguellopezmdev-links-web.vercel.app",
    ],
)
