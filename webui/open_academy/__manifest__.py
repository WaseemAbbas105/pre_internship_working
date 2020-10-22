{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Test',
    'version': '0.1',
    'depends': ['base'],
    # always loaded
     'data': [
         # 'security/ir.model.access.csv',
         'views/openacademy.xml',
     ],
    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo.xml',
    # ],
}