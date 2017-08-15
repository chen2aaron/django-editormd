from setuptools import setup

setup(
    name='django-editormd',
    version='0.3.0',
    description='django-editormd package helps integrate editor.md with Django.',
    long_description=open('README.md').read(),
    author='xixijun',
    author_email='chen2aaron@gmail.com',
    packages=['editormd'],
    include_package_data=True,
    install_requires=[
        'Pillow',
    ],
    url='http://github.com/chen2aaron/django-editormd',
    license='MIT',
    zip_safe=False,
    keywords='editor.md,django,admin,editor,text,html,editor,rich,web',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
