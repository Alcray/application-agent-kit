# Tracker and archive rules

## Tracker writes

- Update one existing row when the opportunity already exists; do not append a duplicate for a second session or application stage.
- Preserve formulas, validation, conditional formatting, frozen rows, filters, column widths, and unrelated rows.
- Use only the statuses configured by setup.
- `Submitted` requires a verified success page, confirmation email, reference number, or explicit user confirmation.
- `Pending` requires explicit under-review evidence; elapsed time alone is not evidence.
- `Approved / Offer` requires a direct selection, acceptance, admission, award, or offer. An interview invite is `Interview / Evaluation`.
- Keep `Next Action` concrete and pair it with a real date when one is known.
- When a CV/resume is requested, `Tailored CV` must link to the reviewed opportunity-specific file, not the general/master CV. Leave it blank only when no CV is requested or the requirement is unresolved.

After submission, the note must be sufficient for later monitoring: organizer or recruiter, official sender/domain when known, confirmation/reference number, expected decision timing, and next follow-up.

## Pre-submit snapshot

Save the literal reviewed version in `03 In Progress` before asking for submit authorization. Include:

- opportunity, organization, form URL, applicant name, and snapshot time
- every visible question and exact response
- dropdown, radio, checkbox, and consent selections
- optional fields intentionally left blank
- uploaded filenames and Drive links
- the tailored CV's master source, final filename/link, and material-change summary
- fees, travel/attendance obligations, and material terms

Exclude passwords, one-time codes, CAPTCHA responses, payment-card data, and government identity numbers.

## Submitted archive

After verified submission, create a private application archive location in `04 Submitted Applications`. Prefer a subfolder named `YYYY-MM-DD — <Application Name>`; if the user's existing archive is intentionally flat, preserve that layout. Create a native Google Doc named:

`YYYY-MM-DD — <Application Name> — Submitted Q&A`

Record:

- program/role/opportunity and organizer
- form URL and exact applicant name used
- submission date and timezone
- confirmation state and reference number
- every exact submitted question and answer
- selections, consents, and optional blanks
- uploaded materials with exact filenames and links
- a preserved copy of the exact uploaded tailored CV and other final attachments; never revise these archived copies
- any item that could not be verified after submission

Do not reconstruct missing wording from memory and label it exact. Link the tailored working CV from `Tailored CV` and the immutable submitted archive from `Application Archive`. Add the archive link only after submission is verified. Keep `Reusable Answers` as the approved canonical library; the submitted archive is an immutable historical record.
