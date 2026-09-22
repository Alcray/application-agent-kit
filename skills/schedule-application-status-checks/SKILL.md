---
name: schedule-application-status-checks
description: Create, inspect, update, pause, resume, or remove a recurring schedule that runs the application status checker at a user-confirmed time and timezone. Use when the user asks to check applications daily, periodically, from time to time, or on a schedule. Do not create duplicate schedules or infer an exact timezone.
---

# Schedule Application Status Checks

Configure a product-native recurring task that invokes `check-application-status`; do not replace the host scheduler with a raw cron string or an improvised background process.

## Verify readiness

1. Confirm that `check-application-status` is installed and that the user's private System Index and tracker resolve correctly.
2. Run one ordinary status check before scheduling. Verify that the task can read the tracker and the intended email source. If a required connection, permission, or skill is unavailable, report it and stop before creating a schedule that cannot work.
3. Inspect existing scheduled tasks or automations for the same workspace and purpose. Update the matching task when one exists instead of creating a duplicate.

## Resolve the schedule

- If the user did not provide them, ask for the frequency, local run time, and timezone in one concise question. Offer daily as the default.
- Use a confirmed timezone from the System Index when available, but state it and let the user correct it. Otherwise require an IANA timezone such as `Europe/Yerevan`; do not infer timezone from a phone number, CV location, browser locale, or current IP.
- Ask whether the user wants notifications only for meaningful changes and required actions, or a report after every run. Recommend change-only notifications.
- Ask for an optional end condition only when relevant. Do not silently stop monitoring while active applications remain.

## Create or update the recurring task

Use the host product's native scheduled-task or automation capability. Prefer a task attached to the current application-monitoring conversation when that preserves useful prior-run context; otherwise create a standalone recurring task.

Read [references/scheduled-prompt.md](references/scheduled-prompt.md) and save a prompt that explicitly invokes `$check-application-status`. The saved prompt must remain valid on future runs without relying on today's conversational wording.

The task must:

- use the user's confirmed local time and timezone;
- check only the private application System Index, active tracker rows, connected application email, and portals available to the scheduled surface;
- update tracker status only from evidence accepted by `check-application-status`;
- notify only on a meaningful status change, urgent deadline, failure, or required user action unless the user requested a full report;
- stay quiet when nothing actionable changed;
- never send or reply to messages, schedule interviews, upload materials, pay, accept, decline, withdraw, or submit anything;
- identify a missing connection or permission instead of guessing.

For portability, default to a time-based daily check. Create an event-triggered email task only when the user explicitly requests it and the current account, surface, and connected email app support it.

## Confirm and manage

After creation or update, return the task name, frequency, local time, timezone, next run when available, sources it can access, notification policy, and any unresolved dependency. Explain how to pause, resume, edit, or delete the task in the host product.

When the user later changes the time or frequency, modify the existing task. When they ask to pause, report the paused state and stop. Delete only when they explicitly ask to remove the schedule.
