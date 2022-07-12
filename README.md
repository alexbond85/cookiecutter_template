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
  - go to the created folder ```cd repository_name```
  - type ```git init```
  - type ```git add .```
  - type ```git commit -m "main initial commit"```
- Create a repository with ```repository_name``` on github 
  - go to github, create new repository with previously entered repository name
    - don't choose the option "create README file"
- Connect local folder with github:
  - git remote add origin git@github.com:shippeo/repository_name
  - git push -u origin main
- Run CI pipiline locally:
  - run ```task init``` to create .venv with dependencies
  - activate the environment (```poetry shell``` or ```source .venv/bin/activate```)
  - run ```task``` in the ```repository_name``` folder.

