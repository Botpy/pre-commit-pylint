## Usage

Add follow content to `.pre-commit-config.yaml`


```yaml
-   repo: git@github.com:coldnight/pre-commit-pylint.git
    sha: v0.0.2
    hooks:
    -   id: pylint-py3k
    -   id: pylint-score-limit
        args:
        - --limit=8.5
        - --rcfile=./.pylintrc
```

## Note

Before `pre-commit` run, you should install pylint and requirements manually:

```shell
$ pip install --upgrade pylint
$ pip install --upgrade requirements.txt
$ pre-commit run
# or
$ git commit -m 'commit message'
```
