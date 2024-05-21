# Commit Message Format

*Specifications for this repository commit messages*

## Commit structure

```
<type>(<scope>): <short summary>
  │       │             │
  │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │       │
  │       └─⫸ Commit Scope
  │
  └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test|chore
```

The `<type>` and `<summary>` fields are mandatory, the `(<scope>)` field is
optional.

### Type

Must be one of the following:

* **build** : Changes that affect the build system or external dependencies (
  example scopes: gulp, broccoli, npm)
* **ci** : Changes to our CI configuration files and scripts (examples:
  CircleCi, SauceLabs)
* **docs** : Documentation only changes
* **feat** : A new feature
* **fix** : A bug fix
* **perf** : A code change that improves performance
* **refactor** : A code change that neither fixes a bug nor adds a feature
* **test** : Adding missing tests or correcting existing tests
* **chore** : Chore changes (update .gitignore, dependencies, etc)

### Scope

The scope should be the name of the file, the directory or the feature involved
in the commit.

Here are some examples:

* gitignore
* main
* action
* readme

### Summary

Use the summary field to provide a succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize the first letter
* no dot (.) at the end

## GitHub Branches

If you want to work on a feature you have to create a branch for it. To create a
branch you have to create it directly on a GitHub issue. For the name Github
will automatically use the following pattern:

```
<issue-number>-<short-description>
```

You can use it as is.

## GitHub Issues

If you want to create an issue you have to use the following rules:

- Name the issue with a short description
- Describe the issue with a description
- Add labels to the issue

## GitHub Pull Requests

When you do a pull request you have to use the following rules:

- Name the pull request with the issue number and the short description
- Add minimum two reviewers to the pull request
- You have to squash your commits to one commit with the number of the issue and
  the short description
