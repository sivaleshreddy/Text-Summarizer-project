import setuptools

with open('README.md','r',encoding='utf-8' ) as f:
    long_description = f.read()
    
__version__ = "0.0.0"

Repo_Name = "Text-Summarization-project"
AUTHOR_USERNAME = "sivaleshreddy"
SRC_REPO = 'Text Summarizer'
AUTHOR_EMAIL = 'sivaleshkailasam@gmail.com'

setuptools.setup(
    name=Repo_Name,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description= 'A small project on text summarization',
    long_description= long_description,
    long_description_content='text/markdown',
    url=f"https://github.com/{AUTHOR_USERNAME}/{Repo_Name}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{Repo_Name}/issues",
    },
    package_dir = {"":"src"},
    packages=setuptools.find_packages(where="src")
    
)