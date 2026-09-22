# Private workspace blueprint

Use these exact names so every skill can rediscover the system. Replace `<Name>` with the workspace name confirmed by the user.

```text
Application Agent — <Name>/
├── 00 System/
│   ├── System Index — <Name>                 Google Doc
│   ├── Ground Truth Database — <Name>         Google Sheet
│   └── Application Tracker — <Name>           Google Sheet
├── 01 CVs & Resumes/
│   ├── General/
│   └── Role-specific/
├── 02 Supporting Materials/
│   ├── Transcripts & Certificates/
│   ├── References & Letters/
│   └── Portfolio & Work Samples/
├── 03 In Progress/
├── 04 Submitted Applications/
└── 05 Templates/
```

Do not change sharing while creating or repairing the tree. If the user already has equivalent folders, prefer linking them from the System Index over copying files.

## System Index

The index is private configuration, not a narrative profile. Include:

- Workspace owner display name
- Setup state: `In progress` or `Complete`
- Root folder link
- Ground Truth Database link
- Application Tracker link
- General CV folder link
- Role-specific CV folder link
- Supporting Materials folder link
- In Progress folder link
- Submitted Applications folder link
- Templates folder link
- Current CV filename and link, or `Missing`
- Active lanes, using the canonical tab names below
- Configured application browser, defaulting to Chrome when available
- Email status-check source, or `Not connected`
- Last setup audit date

Use links or native Drive chips. Never add an anyone-with-the-link permission.

## Ground Truth Database tabs

Create these tabs:

- `Profile`
- `Education`
- `Experience`
- `Research & Publications`
- `Awards & Activities`
- `Links`
- `Reusable Answers`
- `Change Log`

Follow `profile-schema.md`. Freeze the header, enable wrapping, use filters, and keep source links clickable.

## Tracker tabs

Always create `Dashboard`, then only the selected lane tabs:

- Jobs/internships → `Jobs`
- Bachelor's/master's/PhD/other degree → `Degrees`
- Scholarships/fellowships → `Scholarships & Fellowships`
- Grants to the individual → `Grants`
- Conferences/workshops/research schools → `Events & Workshops`
- Hackathons/competitions → `Hackathons & Competitions`
- Other → a short user-confirmed tab name

All lane tabs use this status validation:

`Researching | Draft | Ready to submit | Submitted | Pending | Interview / Evaluation | Approved / Offer | Rejected | Withdrawn | Closed`

Use a real date value wherever the value is a date. Freeze and filter the header row. Use one row per opportunity and preserve existing rows on repair.

### Jobs

`Role | Organization | Location | Work Mode | Employment Type | Deadline | Status | Next Action | Next Action Date | Application Link | Application Archive | Contact | Last Update`

### Degrees

`Program | Institution | Degree | Start Term | Location | Deadline | Funding | Status | Next Action | Next Action Date | Application Link | Application Archive | Last Update`

### Scholarships & Fellowships

`Opportunity | Organization | Host / Location | Dates | Deadline | Funding | Status | Next Action | Next Action Date | Application Link | Application Archive | Last Update`

### Grants

`Grant | Funder | Track | Amount | Deadline | Applicant Type | Status | Next Action | Next Action Date | Application Link | Application Archive | Last Update`

### Events & Workshops

`Event | Organizer / Location | Event Dates | Deadline | Funding / Fee | Status | Next Action | Next Action Date | Application Link | Application Archive | Last Update`

### Hackathons & Competitions

`Event | Organizer / Location | Team | Event Dates | Deadline | Prize / Funding | Status | Next Action | Next Action Date | Application Link | Application Archive | Last Update`

### Custom lane

Start with:

`Opportunity | Organization | Location | Date / Deadline | Status | Next Action | Next Action Date | Application Link | Application Archive | Last Update`

Add fields only when the user's lane genuinely needs them.

## Dashboard

Create a small summary with links to active lane tabs, counts by status, applications with a next-action date in the next 14 days, and the last refresh time. Prefer simple formulas that remain valid when rows are appended. Do not place application records directly on the dashboard.
