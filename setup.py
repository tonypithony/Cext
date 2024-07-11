# После написания кода на Си нужно скомпилировать его в модуль для Питона
# — к счастью, для этого есть множество встроенных инструментов.

# apt install python3-dev

# import tools to create the C extension
# https://stackoverflow.com/questions/25337706/setuptools-vs-distutils-why-is-distutils-still-a-thing
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from distutils.core import Extension

module_name = 'c_module'
# the files your extension is comprised of
c_files = ['c_module.c']

extension = Extension(
    module_name,
    c_files
)

setup(
    name=module_name,
    version='1.0',
    description='The package description',
    author='Nicholas Obert',
    author_email='nchlsuba@gmail.com',
    url='https://my.web.site/some_page',
    ext_modules=[extension]
)


'''
В командной строке выполните следующее:

>>> python3 setup.py build

В результате появится каталог с именем build, внутри которого будут скомпилированные библиотеки. После завершения работы команды выполните:

>>> sudo python3 setup.py install

В систему будут установлены только что собранные библиотеки, и ими можно будет пользоваться откуда угодно.
'''

# Installed /usr/local/lib/python3.10/dist-packages/c_module-1.0-py3.10-linux-x86_64.egg
# Processing dependencies for c-module==1.0
# Finished processing dependencies for c-module==1.0