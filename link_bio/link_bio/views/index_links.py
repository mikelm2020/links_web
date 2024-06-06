import reflex as rx

import link_bio.constants as const
from link_bio.components.featured_link import featured_link
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.routes import Route
from link_bio.state.PageState import PageState
from link_bio.styles.styles import Color, Spacing


def index_links() -> rx.Component:
    return rx.vstack(
        title("Certificaciones y Cursos"),
        link_button(
            "Cursos tomados",
            "Los cursos que he tomado para desarrollo Backend",
            "/icons/code.svg",
            Route.COURSES.value,
            False,
            Color.SECONDARY.value,
        ),
        link_button(
            "AWS Certified Cloud Practitioner",
            "Entendimiento fundamental de los servicios IT y su uso en la Nube de AWS",
            "/icons/aws.svg",
            const.PRACTITIONER_URL,
        ),
        link_button(
            "AWS re/Start Graduate",
            "Diploma de Graduación del programa de AWS re/Start",
            "/icons/aws.svg",
            const.RESTART_URL,
        ),
        link_button(
            "Cloud Developer en AWS",
            "Bootcamp Cloud Developer en BootCamp Institute ",
            "/icons/aws.svg",
            const.CLOUD_DEVELOPER_URL,
        ),
        link_button(
            "Certificado de Inglés EF SET",
            "Certificado de calificación de prueba de Inglés EF SET",
            "/icons/efset.svg",
            const.EF_SET_URL,
        ),
        rx.cond(
            PageState.featured_info,
            rx.vstack(
                title("Curso que estoy tomando actualmente"),
                rx.flex(
                    rx.foreach(
                        PageState.featured_info,
                        featured_link,
                    ),
                    flex_direction=["column", "row"],
                    spacing=Spacing.DEFAULT.value,
                ),
                spacing=Spacing.DEFAULT.value,
            ),
        ),
        title("Repositorios importantes"),
        link_button(
            "Alquiler de propiedades Rentopia",
            "Proyecto personal de la API de un Alquiler de propiedades en colaboración con un grupo multinacional de desarrolladores a mi cargo",
            "/icons/python.svg",
            const.RENTOPIA_URL,
        ),
        link_button(
            "Backend de una Agenda similar a la de Android",
            "Poyecto de una API para una Agenda de contactos validando teléfonos",
            "/icons/python.svg",
            const.DIARY_URL,
        ),
        link_button(
            "Manejo de Roles en Django",
            "Proyecto del manejo de Roles en Django de un sistema administrativo",
            "/icons/python.svg",
            const.ROLES_URL,
        ),
        link_button(
            "Particpación del Hackaton de Nuwehack Cloud",
            "Proyecto realizado en el Hackaton de Nuwehack Cloud utilizando Terraform y Lambda Functions de AWS",
            "/icons/python.svg",
            const.NUWEHACK_URL,
        ),
        link_button(
            "Backend de la App del Buen Conejo v 2.0",
            "API para la app de la Organización del Buen Conejo",
            "/icons/python.svg",
            const.RABBIT_URL,
        ),
        link_button(
            "Plataforma del Buen Conejo v 1.0",
            "Colaboración en el proyecto de No Country en el área del Backend con Django Rest Framework",
            "/icons/python.svg",
            const.NC_RABBITS_URL,
        ),
        link_button(
            "Plataforma de busqueda de mascotas",
            "Colaboración en el proyecto de No Country en el área del Backend con Fast API",
            "/icons/python.svg",
            const.NC_PETS_URL,
        ),
        link_button(
            "API para Lista de Reproducción de Video Streaming",
            "API en Django Rest Framework para el proyecto personal",
            "/icons/python.svg",
            const.VIDEO_STREAMING_URL,
        ),
        link_button(
            "API para una Veterinaria",
            "API en Django Rest Framework usando Docker para el proyecto personal",
            "/icons/python.svg",
            const.VETERINARY_URL,
        ),
        link_button(
            "Eventos SAM Avanzados",
            "Demo de Aplicación Ecommerce para crear una orden con la Arquitectura Conducida a Eventos utilizando el framework SAM para AWS",
            "/icons/python.svg",
            const.SAM_ADVANCED_URL,
        ),
        title("Contacto"),
        link_button(
            "Email",
            const.EMAIL,
            "/icons/email.svg",
            f"mailto:{const.EMAIL}",
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
        on_mount=PageState.featured_links,
    )
