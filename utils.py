
industries = {
    'Apparel': {
        'name': 'Apparel',
        'category': 'Consumer Products',
    },
    'Food and beverage processing': {
        'name': 'Food and beverage processing',
        'category': 'Consumer Products',
    },
    'Furniture': {
        'name': 'Furniture',
        'category': 'Consumer Products',
    },
    'Printing and Related Support Activities': {
        'name': 'Printing and Related Support Activities',
        'category': 'Consumer Products',
    },
    'Recreational Boats': {
        'name': 'Recreational Boats',
        'category': 'Consumer Products',
    },
    'Sporting and Athletic Goods': {
        'name': 'Sporting and Athletic Goods',
        'category': 'Consumer Products',
    },
    'Textile': {
        'name': 'Textile',
        'category': 'Manufacturing Industries',
    },
    'Wood Product Manufacturing': {
        'name': 'Wood Product Manufacturing',
        'category': 'Manufacturing Industries',
    },
    'Aerospace and Defence': {
        'name': 'Aerospace and Defence',
        'category': 'Manufacturing Industries',
    },
    'Automotive': {
        'name': 'Automotive',
        'category': 'Manufacturing Industries',
    },
    'Biomanufacturing': {
        'name': 'Biomanufacturing',
        'category': 'Manufacturing Industries',
    },
    'Chemicals': {
        'name': 'Chemicals',
        'category': 'Manufacturing Industries',
    },
    'Hydrogen and Fuel Cells': {
        'name': 'Hydrogen and Fuel Cells',
        'category': 'Manufacturing Industries',
    },
    'Medical Devices': {
        'name': 'Medical Devices',
        'category': 'Manufacturing Industries',
    },
    'Plastics': {
        'name': 'Plastics',
        'category': 'Manufacturing Industries',
    },
    'Primary Metals': {
        'name': 'Primary Metals',
        'category': 'Manufacturing Industries',
    },
    'Rubber': {
        'name': 'Rubber',
        'category': 'Manufacturing Industries',
    },
    'Shipbuilding and Industrial Marine': {
        'name': 'Shipbuilding and Industrial Marine',
        'category': 'Manufacturing Industries',
    },
    'Logistics': {
        'name': 'Logistics',
        'category': 'Service Industries',
    },
    'Retail Trade': {
        'name': 'Retail Trade',
        'category': 'Service Industries',
    },
    'Specialized Design Services': {
        'name': 'Specialized Design Services',
        'category': 'Service Industries',
    },
    'Tourism': {
        'name': 'Tourism',
        'category': 'Service Industries',
    },
    'Canadian space industry': {
        'name': 'Canadian space industry',
        'category': 'Technologies',
    },
    'Digital Technologies': {
        'name': 'Digital Technologies',
        'category': 'Technologies',
    },
    'Life Sciences': {
        'name': 'Life Sciences',
        'category': 'Technologies',
    },
    'Nanotechnologies': {
        'name': 'Nanotechnologies',
        'category': 'Technologies',
    },
    'Community': {
        'name': 'Non-profit',
        'category': 'Non-profit',
    }
}


def get_industries_and_categories():
    industries_and_categories = {}
    for industry in industries.values():
        category = industry["category"]
        if category not in industries_and_categories:
            industries_and_categories[category] = []
        industries_and_categories[category].append(industry["name"])
    return industries_and_categories
