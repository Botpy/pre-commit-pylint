## Usage

Add follow content to `.pre-commit-config.yaml`


```yaml
-   repo: git@github.com:coldnight/pre-commit-pylint.git
    sha: v0.0.1
    hooks:
    -   id: pylint-py3k
    -   id: pylint-score-limit
        args:
        - --limit=8.5
        - --rcfile=./.pylintrc
        additional_dependencies:
        - libary1
        - libary2
        - libary3
```
