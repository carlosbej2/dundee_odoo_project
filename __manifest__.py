{
    'name': 'DUNDEE Start-Up',
    'author': 'José Carlos Bayón Guerrero',
    'version': '1.1',
    'category': 'Services/Project',
    'summary': 'Módulo personalizado para la gestión del proyecto DUNDEE.',
    'depends': [
        'base',
        'project',
        'mail',

    ],
    'description': "Módulo personalizado para la gestión del proyecto de final de grado DUNDEE.",
    'data': [
        'security/ir.model.access.csv',
        'security/dundee_security.xml',
        'wizard/views/project_task_creation.xml',
        'views/project_task.xml',
        'reports/reports.xml',
        'reports/views/project_task_report_dundee.xml',
    ],
    'demo': [],
    'qweb': [],
    'test': [
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
