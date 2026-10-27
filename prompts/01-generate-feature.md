# Generate a configured feature

Add the feature PRD and optional SRS/supporting files, then configure `config/features.json` or use an exact feature-directory ID.

In **UP Testcase**, enter:

```text
start <feature-id>
```

Example syntax only:

```text
start my-feature
```

The agent resolves the configured inputs and creates the next free version under `output/<feature-id>/` without overwriting an existing artifact.
