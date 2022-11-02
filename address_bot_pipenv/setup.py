from setuptools import setup, find_namespace_packages

setup(
    name='address_book_bot',
    version='1',
    description='Bot for saving contacts in the Address Book.',
    url='https://github.com/Andrew-157/address_book_bot',
    author='Andrew-157',
    author_email='subotinandrey5@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
   entry_points={'console_scripts': ['start_bot = address_book_bot.client_code:client_code']}
)
