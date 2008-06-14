from distutils.core import setup
setup(
    name='phpserialize',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version='1.0',
    url='http://trac.pocoo.org/repos/sandbox/phpserialize',
    py_modules=['phpserialize'],
    description='a port of the serialize and unserialize '
                'functions of php to python.',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: PHP',
        'Programming Language :: Python'
    ]
)
