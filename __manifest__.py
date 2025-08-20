# -*- coding: utf-8 -*-
{
    'name': 'Ocultar Filtro Personalizado en Productos',
    'version': '17.0.1.0.0',
    'summary': 'Deshabilita el botón "Agregar filtro personalizado" en la búsqueda de productos del TPV y Ventas.',
    'description': """
        Este módulo hereda la vista de búsqueda 'product.view.search.catalog' y le añade el atributo 'disable_custom_filters' para limpiar la interfaz.
    """,
    'author': 'Gemini Assistant',
    'category': 'Sales/Point of Sale',
    'depends': [
        'product',  # Dependencia del módulo de productos, donde está la vista original.
        'sale'
    ],
    'data': [
        'views/product_views.xml', # Carga nuestro archivo de la vista.
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}