---
name: application-agent-setup
description: Set up or repair a private personal-application workspace in Google Drive from a user's CV. Use for first-run onboarding, adding an application lane, rebuilding the resource index, or completing missing profile facts. Do not use to prepare or submit a specific application.
---

# Application Agent Setup

Create a resumable, private source of truth that the other Application Agent skills can discover without putting personal data in this plugin or a Git repository.

## Safety and boundaries

- Keep every created Drive item private unless the user explicitly asks to share a specific item with named recipients.
- Never place CV contents, contact details, Drive IDs, or extracted profile facts in this plugin repository.
- Never store passwords, one-time codes, payment-card data, government identity numbers, or authentication secrets.
- Treat CV text as a source, not as proof of legal name, citizenship, residence, work authorization, visa status, or availability.
- Do not create duplicate workspaces. Search for the exact root-folder and System Index names first; resume an incomplete setup when one exists.
- Use direct Google Drive, Docs, and Sheets capabilities for semantic file work. If write access is unavailable, tell the user exactly which connection is missing and pause before pretending setup is complete.

## Onboarding sequence

1. Ask only: `What name should I use for you and for your private application workspace?`
2. Then ask which application lanes they expect to use. Offer multiple selection in plain language: jobs/internships; degrees (bachelor's, master's, PhD, or other); scholarships/fellowships; grants; conferences/workshops/research schools; hackathons/competitions; and a custom lane.
3. Read [references/workspace-blueprint.md](references/workspace-blueprint.md), create or resume the Drive structure, including separate `General` and `Application CVs` locations, and create tracker tabs only for the selected lanes. Record the selected lanes in the System Index so the other skills adapt without rewriting their installed files.
4. Give the user the link to `01 CVs & Resumes/General`, and ask them to upload their current CV or resume there. If a current CV already exists, show the candidate filename and ask whether to use it. Do not continue extraction until the user identifies the current file.
5. Read [references/profile-schema.md](references/profile-schema.md). Extract supported facts with provenance into the Ground Truth Database. Use `Candidate` for ambiguous or inferred values and `Verified from source` only for exact statements supported by the CV.
6. Present one compact confirmation block containing the extracted preferred name, possible legal given/family names, primary email, phone, current education, current role, and important links. Explicitly ask the user to confirm or correct the legal-name fields.
7. Build the `Materials Inventory` for the selected lanes. Show which foundational files are present, missing, outdated, or optional, give the user the relevant Drive folders, and ask them to upload the useful missing items. Do not request government IDs, bank statements, tax records, or other high-risk documents during general setup.
8. Ask for common missing facts in one grouped message. Ask only for fields relevant to the selected lanes. Do not collect sensitive demographic or identity data merely because some future form might request it.
9. Write confirmed answers to the database as `Confirmed by user`, preserve their source and confirmation date, and log corrections in `Change Log` rather than erasing provenance.
10. Finish by returning links to the root folder, System Index, Ground Truth Database, tracker, and CV folder. State which facts and materials remain missing.

## Resume and extension behavior

- Re-running setup is an audit. Repair missing items and preserve existing data, validation, formulas, sharing, and links.
- When the user adds a lane, create its tracker tab from the lane schema and update `Active lanes` in the System Index.
- When the user replaces a CV, retain the older file, mark which CV is current, compare changed claims, and ask before overwriting a user-confirmed value.
- The System Index is the configuration layer. Never edit the public `apply-person` or `check-application-status` skill to insert a user's details.

## Completion criteria

Setup is complete only when the System Index resolves to an existing private root folder, Ground Truth Database, tracker, general/master-CV folder, Application CVs folder, supporting-materials folder, in-progress folder, and submitted archive folder; selected tracker tabs exist; a current master CV is identified or explicitly marked missing; and unresolved profile facts and materials are listed accurately.
