# Worst Fix Ever: Funniest Commit Message

Entry: one commit-message line for a bug fix that made everything worse.

```
fix: login bug by logging everyone in as admin
```

The joke: a login bug is annoying, but the "fix" hands every single user
admin access — the repair is a far bigger security disaster than the bug
it was meant to solve. It reads like a tired engineer's real commit
subject at the end of a bad day, and the irony is specific: the fix
didn't just fail, it upgraded the problem.

`main.py` (Python stdlib only) writes that single line to
`/output/entry.txt` and checks first that it is one non-empty line of
at most 100 characters.
