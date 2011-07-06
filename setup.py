from setuptools import setup, find_packages
setup(
    name = "mamona",
    version = "0.1",
    packages = find_packages(exclude=["test-project", "test-project.*"]),
    package_data = {
        'mamona':[
            "templates/mamona/*.html",
            "templates/mamona/*/*.html",
            "locale/*/LC_MESSAGES/*",
            ]
        },

    author = "Michal Salaban",
    author_email = "michal@salaban.info",
    description = "Fully portable Django payments application that can use any Order/Cart model.",
    url = "https://github.com/emesik/mamona",


    ## ripped from django-extensions
    license = 'New BSD License',
    platforms = ['any'],
    
    classifiers = [#'Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'],    
    )

