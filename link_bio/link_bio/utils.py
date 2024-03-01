import reflex as rx

# Común


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = "https://moure.dev/preview.jpg"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@miguellopezmdev"},
]

# Index

index_title = "miguellopezmdev | Busco trabajo como desarrollador Backend"
index_description = "Hola, mi nombre es Miguel Angel López. Soy ingeniero en Computacón, desarrollador backend con Python"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# Cursos

courses_title = (
    "miguellopezmdev | Cursos tomados para aprender desarrollo backend con Python"
)
courses_description = (
    "Este es un listado de los cursos que tomé en la plataforma Platzi"
)

courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]
courses_meta.extend(_meta)
