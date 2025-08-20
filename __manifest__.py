# -*- coding: utf-8 -*-
{
    'name': 'Ocultar Filtro Personalizado (JS)',
    'version': '17.0.2.0.0', # Incrementamos la versión
    'summary': 'Deshabilita el botón "Agregar filtro personalizado" usando JavaScript.',
    'description': """
        Este módulo utiliza un parche de JavaScript para ocultar la opción de crear
        filtros personalizados en los menús de búsqueda, evitando conflictos de vistas XML.
    """,
    'author': 'Gemini Assistant',
    'category': 'Technical',
    'depends': [
        'web',  # Ahora dependemos del módulo 'web' para los assets
    ],
    'data': [
        # Ya no necesitamos cargar un archivo XML de vistas.
    ],
    'assets': {
        'web.assets_backend': [
            # Aquí registramos nuestro archivo JS
            'hide_custom_filters_app/static/src/js/hide_filter_option.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}