Prerequisites: 
 - taskfile https://taskfile.dev/installation/
 - poetry https://python-poetry.org/docs/#installation

### USAGE

- Create new repository:
  - activate a virtual environment containing cookiecutter
  - run ```cookiecutter <PATH_TO>/cookiecutter_template```
    - fill in the fields (repository_name, package_name...)
  - deactivate the environment
- Add version control:
```cd repository_name
git init
git add .```
git commit -m "main initial commit"
```
- Create a repository with ```repository_name``` on github 
  - go to github, create new repository with previously entered repository name
    - don't choose the option "create README file"
- Connect local folder with github:
```commandline
git remote add origin git@github.com:shippeo/repo_name.git
git branch -M main
git push -u origin main
```
- Run CI pipiline locally:
  - run ```task init``` to create .venv with dependencies
  - activate the environment (```poetry shell``` or ```source .venv/bin/activate```)
  - run ```task``` in the ```repository_name``` folder.
- Check the CI/CD pipeline on github actions. 
  - Package uploading would require PYPI_PWD to be set in secrets.

