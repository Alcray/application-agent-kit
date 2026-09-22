---
name: check-application-status
description: Check email and application portals for decisions, interviews, missing materials, deadlines, and follow-ups, then reconcile evidence with the private application tracker. Use for one-time or periodic status checks. Do not send replies, accept offers, schedule interviews, or submit materials without separate user authorization.
---

# Check Application Status

Reconcile application status from current evidence while avoiding false positives from newsletters, marketing, and stale tracker notes.

## Load scope

1. Locate the user's private System Index and tracker created by `application-agent-setup`. If either is unavailable, report the missing resource instead of creating a competing tracker.
2. Read active rows in `Submitted`, `Pending`, or `Interview / Evaluation`, plus rows whose next-action date is due. Respect the selected application lanes.
3. Read [references/evidence-and-actions.md](references/evidence-and-actions.md) before changing any status.

## Check evidence

- Search connected email using the exact opportunity and organization, known official sender/domain, confirmation/reference number, and recent dates. If email access is unavailable, ask the user to connect it or paste/forward the relevant message; do not guess.
- Open a portal in the configured browser only when email and the tracker do not establish the current state or when the portal is the named source of truth.
- Treat a direct organizer/recruiter message or authenticated portal state as stronger than automated marketing, third-party summaries, or a prior tracker note.
- Distinguish received, under review, waitlisted, interview invited, missing material, accepted/offer, rejected, and withdrawn. Do not collapse an invitation to apply, generic congratulations, or a completed registration into acceptance.

## Reconcile

- Update a status only when the evidence satisfies the mapping in the reference. Preserve the prior status and add a dated note when evidence is informative but inconclusive.
- Record a concise evidence trail: date, sender/domain or portal, exact outcome category, deadline or response date, confirmation/reference number, and next action.
- Surface urgent items first: missing-material deadlines, interview scheduling windows, offer/acceptance deadlines, payments, and travel or attendance commitments.
- Never reply, schedule, upload, pay, accept, decline, withdraw, or click a confirmation control without a separate user request and the relevant skill's review checkpoint.
- If a verified submitted application lacks an archive, flag it; do not reconstruct exact submitted wording from memory.

## Report

Return a compact summary grouped as `Action required`, `Status changed`, `No change`, and `Could not verify`. Include links to the evidence and tracker rows where available. Stay quiet about unchanged non-actionable items when running as a recurring monitor unless the user requested a full report.
