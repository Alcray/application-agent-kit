# Saved prompt for recurring application checks

Adapt resource names to the user's private System Index, but do not paste CV contents, contact details, credentials, or other unnecessary personal data into the task instructions.

```text
Use $check-application-status to review my active applications.

At each run:
1. Locate my private Application Agent System Index and tracker.
2. Review Submitted, Pending, and Interview / Evaluation rows, plus due or
   overdue Next Action dates.
3. Search the connected application email source using the exact opportunity,
   organization, official sender/domain, and confirmation number when known.
4. Check an application portal only when it is available to this scheduled
   surface and email or tracker evidence is insufficient.
5. Update the tracker only when current evidence supports the status change.
6. Notify me only when there is a meaningful status change, an urgent deadline,
   a failed check, or an action I must take. Stay quiet when nothing actionable
   changed.

Never reply or send messages, schedule interviews, upload documents, pay,
accept, decline, withdraw, or submit anything. If a connection or permission is
missing, tell me exactly what must be restored and do not guess.
```

If the user requested a report after every run, replace the change-only sentence with a concise `Action required / Status changed / No change / Could not verify` report requirement.

## Preflight checklist

- `check-application-status` resolves on the scheduled surface.
- The System Index and tracker are reachable.
- The intended email account is connected and readable.
- The time and IANA timezone are explicit.
- Notification settings match the user's preference.
- No task with the same scope already exists.
