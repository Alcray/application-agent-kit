---
name: tailor-application-cv
description: Create a separate, opportunity-specific CV or resume from a verified general/master CV while preserving factual accuracy and formatting. Use whenever a job, degree, fellowship, grant, event, or competition application requests a CV/resume, or when the user asks to tailor one. Never overwrite the master CV or a previously submitted version.
---

# Tailor Application CV

Produce the strongest truthful CV for one named opportunity and keep the exact uploaded version traceable from the application tracker and archive.

## Load sources and requirements

1. Locate the private System Index created by `application-agent-setup`, the current general/master CV, the Ground Truth Database, `Application CVs`, and the matching tracker row. If no current master CV is identified, stop and ask the user to choose one.
2. Inspect the official opportunity description and form before editing. Extract the responsibilities, required and preferred qualifications, evaluation criteria, keywords, document limits, accepted file types, and any template or anonymization rule.
3. Read [references/tailoring-standard.md](references/tailoring-standard.md). Map each important requirement to exact evidence in the Ground Truth Database or master CV. Leave unsupported requirements unmapped; never manufacture a match.

## Create the application-specific copy

- Create a new file in `Application CVs`; never edit the general/master CV in place and never overwrite a CV used for another opportunity.
- If the existing workspace has a root-level `Application CVs` folder, use it and record its link in the System Index rather than moving or duplicating it.
- Name the editable file `YYYY-MM-DD — Organization — Opportunity — CV — v01.docx` where supported. Increment the version for material revisions. Create an upload-ready PDF with the same base name when the portal accepts PDF.
- Prefer duplicating the best current editable CV so its established layout survives. If only a PDF is available and reliable editing cannot preserve it, ask for an editable source or clearly limit the deliverable to a proposed content plan.

## Tailor without changing the truth

- Reorder and select experiences, projects, research, publications, skills, and awards according to relevance.
- Rewrite summaries and bullets for clarity and alignment while preserving the original meaning, scope, dates, titles, collaborators, metrics, and outcomes.
- Emphasize supported keywords naturally. Do not keyword-stuff or claim proficiency merely because the posting names a tool.
- Remove or compress lower-relevance material when space is limited, but do not hide a fact the application explicitly requires.
- Never invent or upgrade titles, employers, degrees, grades, dates, publications, awards, responsibilities, metrics, leadership, language proficiency, citizenship, work authorization, or security clearance.
- When a proposed rewrite could materially broaden a claim, keep the verified wording and flag the alternative for the user's review.

## Verify the document

- Preserve the source document's visual system unless the user asks for a redesign.
- Render or preview the final document and inspect every page for overflow, clipped text, broken bullets, inconsistent spacing, font substitution, accidental blank pages, incorrect links, and unreadable density.
- Check names, contact details, chronology, section order, tense, page count, filename, and portal format constraints.
- Compare the final CV against the requirement-to-evidence map and the master CV. Every material claim must resolve to verified evidence.

## Review, link, and archive

1. Give the user the editable file, upload-ready file, and a concise change summary: sections reordered, bullets materially rewritten, items added or removed, and requirements intentionally left unsupported.
2. Record the exact final CV link in the tracker row's `Tailored CV` column. Keep it `Draft` until it is the reviewed upload candidate.
3. `apply-person` may include CV review in the application's mandatory final review; do not create a separate submission authorization.
4. Before upload, verify the browser attachment filename matches the reviewed file. Never silently substitute the general CV.
5. After verified submission, preserve a copy of the exact uploaded CV with the submitted application archive. Do not revise that archived copy; create a new version for later applications.
