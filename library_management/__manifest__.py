{
    "name": "Library Management",
    "version": "1.0",
    "description": "A module for managing library operations.",
    "author": "Carlo",
    "depends": ["base", "portal"],
    "images": [
        "static/description/icon.png"
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/library_management_views.xml",
        "views/book_portal_templates.xml",
    ],
    "installable": True,
    "application": True,
}
