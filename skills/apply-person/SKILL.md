---
name: apply-person
description: Research, prepare, fill, review, submit with fresh authorization, archive, and track an individual's job, degree, scholarship, fellowship, grant, event, workshop, research-school, hackathon, or competition application. Use for a specific personal application. Never use standing permission to submit or accept a binding commitment.
---

# Apply Person

Run a personal application from opportunity inspection through tracking while protecting claim integrity and keeping submission under the user's control.

## Load the private configuration

1. Search Drive for `Application Agent — *` and its `00 System/System Index — *` document. If no valid index exists, invoke `application-agent-setup` before preparing an application.
2. Read the System Index, the Ground Truth Database, the current general/master CV, the Application CVs location, the selected-lane tracker tab, and any semantically equivalent approved reusable answers.
3. Read [references/application-lanes.md](references/application-lanes.md) to choose the lane and required tracker columns. Read [references/tracker-and-archive.md](references/tracker-and-archive.md) before the first tracker or archive write.

## Inspect and ground the application

- Inspect the official opportunity page and the complete form in the user's configured browser. Record eligibility, deadline with timezone, dates, location, attendance or work-mode requirements, funding or compensation, fees, visa or work-authorization implications, required uploads, consents, and the literal final action.
- Prefer current official information over stale tracker notes. Use email only when current organizer or recruiter correspondence matters.
- When the application requests a CV or resume, use `tailor-application-cv` after inspecting the full opportunity and before uploading. Create a separate version for this opportunity, link it in the tracker's `Tailored CV` column, and verify its filename and content. Do not upload the general/master CV merely because it is convenient unless the user explicitly approves using it unchanged.
- Use only exact facts supported by a source or confirmed by the user. Do not infer citizenship, residence, legal name, work authorization, visa status, grades, rankings, publications, awards, compensation expectations, availability, team membership, or attendance commitments.
- When sources conflict, show the conflict and ask. Do not silently prefer the version that makes the application stronger.

## Answer consistently

1. Search `Reusable Answers` and submitted archives for the same or a semantically equivalent question.
2. Reuse a user-approved answer, adapting only grammar, point of view, length, and the requested format.
3. If a narrative answer is new, ask: `This answer is not yet approved in your library. Would you like an AI-generated draft from your verified context, or would you prefer to write the first version?`
4. Label a generated first version `Proposed`. Do not treat it as reusable until the user approves it.
5. Preserve the user's meaning. Never add flattering but unsupported claims.

## Fill and review

- Use direct Drive/Docs/Sheets capabilities for source files and records, and the configured browser for application-site interaction. Do not use connectors as a hidden alternate way to submit a website form.
- Inspect every field, limit, selection, consent, upload, fee, and final action before filling.
- Fill verified facts and approved answers. Leave unsupported optional fields blank. Ask about required unsupported fields.
- Update one tracker row as `Draft` when work begins and after each material change.
- Before submission, capture a literal pre-submit snapshot containing every visible question and exact response, selections, intentional blanks, the exact tailored-CV filename and link, all other uploaded filenames and links, consents, and any fee or commitment. Exclude passwords, one-time codes, CAPTCHA responses, payment data, and government ID numbers.

## Mandatory final review

Submission is a separate, one-use authorization step.

1. Never auto-submit. A request such as `apply`, `finish it`, or `take care of everything` authorizes preparation only.
2. Complete the form, upload authorized materials, save the snapshot, set the tracker to `Ready to submit`, leave the completed form open when possible, and stop before the final control.
3. Summarize unresolved facts, material edits, fees, travel or attendance obligations, legal terms, consents, attachments, and the tailored CV's source, exact filename, and material changes from the master CV.
4. Say: `The [Application Name] application is complete and ready for your final review. Nothing has been submitted. After reviewing it, tell me "Submit [Application Name]" if you want me to send this exact version.`
5. Submit only after that fresh, application-specific instruction. Authorization is consumed after one attempt and applies only to the reviewed version. Any material change requires a new review and authorization.
6. A submit instruction does not authorize payment, purchase, acceptance of an offer, enrollment, signing binding terms, or another commitment. Stop and call those out separately.
7. After submission, verify a success state or obtain explicit user confirmation before marking the row `Submitted`.

## Archive and hand off

- For a verified submission, create the immutable submitted Q&A record described in [references/tracker-and-archive.md](references/tracker-and-archive.md), preserve the exact uploaded tailored CV with it, link both from the tracker/archive, and record organizer/recruiter domain, confirmation number, expected response timing, and next follow-up.
- If the user submits personally, retain the snapshot and archive only after they confirm success. Mark unverified differences explicitly.
- Return the form, tracker row, archive, and relevant source links without exposing private Drive items more broadly than necessary.
