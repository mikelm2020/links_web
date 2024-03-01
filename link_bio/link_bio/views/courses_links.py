import reflex as rx
import link_bio.constants as const
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size


def courses_links() -> rx.Component:
    return rx.vstack(
        title("Mis Cursos tomados en la Plataforma Platzi"),
        link_button(
            "Amazon DynamoDB",
            "Curso de la base de datos relacional de Amazon",
            "/icons/challenges.png",
            const.DYNAMO_DB_URL,
            highlight=True,
        ),
        link_button(
            "Roles y Seguridad con IAM",
            "Curso práctico de AWS usando IAM",
            "/icons/python.svg",
            const.IAM_URL,
        ),
        link_button(
            "Fundamentos de Web Scraping con Python y XPath",
            "Curso para hacer scraping en sitios web",
            "/icons/git.svg",
            const.XPATH_URL,
        ),
        link_button(
            "Curso de Scrapy",
            "Curso para hacer scraping en sitios web con Scrapy ",
            "/icons/sql.svg",
            const.SCRAPY_URL,
        ),
        link_button(
            "Introduccion a Selenium con Python",
            "Curso para hacer automatización con Selenium",
            "/icons/code.svg",
            const.SELENIUM_URL,
        ),
        link_button(
            "PostgreSQL",
            "Curso de la base de datos relacional PostgreSQL",
            "/icons/twitch.svg",
            const.POSTGRES_URL,
        ),
        link_button(
            "Introducción a AWS: Cómputo, Almacenamiento y Bases de datos",
            "Curso de los servicios AWS para esas áreas",
            "/icons/youtube.svg",
            const.AWS_COMPUTO_URL,
        ),
        link_button(
            "Introducción a AWS: Fundamentos de Cloud Computing",
            "Teoría de los servicios en la Nube de AWS",
            "/icons/youtube.svg",
            const.AWS_CLOUD_URL,
        ),
        link_button(
            "Introducción a AWS: Redes. Gobernanza y Machine Learning",
            "Teoría de esos temas aplicados a servicios de AWS",
            "/icons/challenges.png",
            const.AWS_REDES_URL,
        ),
        link_button(
            "Docker", "Curso práctico de Docker", "/icons/python.svg", const.DOCKER_URL
        ),
        link_button(
            "Curso básico de Django",
            "Curso práctico del framework Django",
            "/icons/git.svg",
            const.DJANGO_BASICO_URL,
        ),
        link_button(
            "Curso de Django Intermedio: Testing, Static Files, Django Admin",
            "Curso práctico de Django intermedio",
            "/icons/sql.svg",
            const.DJANGO_INTERMEDIO_URL,
        ),
        link_button(
            "POO y Algoritmos con Python",
            "Curso de la complejidad agoritmica con Python",
            "/icons/code.svg",
            const.POO_PYTHON_URL,
        ),
        link_button(
            "Fundamentos de Bases de Datos",
            "Teoría de bases de datos relacionales",
            "/icons/twitch.svg",
            const.FUNDA_DB_URL,
        ),
        link_button(
            "Introducción al desarrollo Backend",
            "Teoría para el desarrollo Backend",
            "/icons/youtube.svg",
            const.BACKEND_URL,
        ),
        link_button(
            "Curso Práctico de SQL",
            "Aplicacioón de comandos SQL con PostgreSQL",
            "/icons/youtube.svg",
            const.SQL_URL,
        ),
        link_button(
            "Fundamentos de Ingeniería de Software",
            "Teoría de la Ingeniería de Software",
            "/icons/challenges.png",
            const.ING_SW_URL,
        ),
        link_button(
            "Programación Orientada a Objetos: POO",
            "Curso práctico de POO en los siguientes lenguajes: Python, JavaScript, PHP y Java",
            "/icons/python.svg",
            const.POO_URL,
        ),
        link_button(
            "Curso Práctico de Python: Creación de un CRUD",
            "Curso para crear un CRUD en Python para ejecutar en Consola",
            "/icons/git.svg",
            const.CRUD_URL,
        ),
        link_button(
            "Curso básico de Python",
            "Curso inicial para aprender Python",
            "/icons/sql.svg",
            const.PYTHON_BASICO_URL,
        ),
        link_button(
            "Introduccion a la Terminal y Línea de Comandos",
            "Curso para aprender a manejar una terminal Linux",
            "/icons/code.svg",
            const.TERMINAL_URL,
        ),
        link_button(
            "Curso de Python Intermedio: Comprehensions, Lambdas y Manejo de Errores",
            "Curso intermedio y práctico de Python",
            "/icons/twitch.svg",
            const.PYTHON_INTER_URL,
        ),
        link_button(
            "Curso de ECMAScript 6+",
            "Curso práctico de la versión de JavaScript",
            "/icons/youtube.svg",
            const.ECMASCRIPT_URL,
        ),
        link_button(
            "Curso profesional de Git y Github",
            "Curso práctico de Git y Github",
            "/icons/youtube.svg",
            const.GIT_GITHUB_URL,
        ),
        link_button(
            "Curso básico de JavaScript",
            "Teoría y práctico de JavaScript Vanilla",
            "/icons/youtube.svg",
            const.JAVASCRIPT_URL,
        ),
        link_button(
            "Curso definitivo de HTML y CSS",
            "Curso práctico para crear paginas web básicas con HTML 5.0 y CSS 3.0",
            "/icons/youtube.svg",
            const.HTML_CSS_URL,
        ),
        width="100%",
        spacing=Size.DEFAULT.value,
    )
