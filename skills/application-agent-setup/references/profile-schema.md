# Ground Truth Database schema

Every factual row must retain provenance. Never upgrade an ambiguous extraction merely because it is plausible.

Use these verification values:

- `Candidate`: inferred, ambiguous, or awaiting confirmation
- `Verified from source`: stated exactly in the linked source
- `Confirmed by user`: explicitly confirmed in chat or another direct user statement
- `Disputed`: sources conflict or the user rejected the value
- `Unknown`: required field is not yet known

## Profile

Columns:

`Field | Value | Verification | Source | Source Detail | Last Confirmed | Notes`

Seed only useful fields. Common fields include preferred name, legal given name, legal family name, other names, primary application email, backup email, phone with country code, current city and country, timezone, personal website, LinkedIn, GitHub, and portfolio.

The name printed on a CV may be a preferred or professional name. Store it as a candidate and explicitly confirm the legal-name fields. Do not infer nationality, citizenship, residence status, work authorization, visa needs, date of birth, gender, ethnicity, disability, marital status, government IDs, or financial data. Ask for a sensitive fact only when a current application requires it, and ask whether the user wants it saved for reuse.

## Education

Columns:

`Institution | Program / Degree | Field | Start Date | End Date | Status | Location | Grade / GPA | Verification | Source | Last Confirmed | Notes`

Do not convert an expected date into a completed degree. Preserve the grading scale exactly.

## Experience

Columns:

`Organization | Role | Start Date | End Date | Current | Location | Summary | Verification | Source | Last Confirmed | Notes`

Do not infer full-time status, employment type, seniority, compensation, or current employment from ordering alone.

## Research & Publications

Columns:

`Type | Title | Venue / Organization | Date | Authors / Contributors | DOI / URL | Status | Verification | Source | Last Confirmed | Notes`

Preserve publication status such as submitted, accepted, preprint, or published. Never estimate citation counts.

## Awards & Activities

Columns:

`Type | Name | Organization | Date | Result / Role | URL | Verification | Source | Last Confirmed | Notes`

Keep nominations, participation, finalist status, wins, and funding distinct.

## Links

Columns:

`Label | URL | Purpose | Verification | Last Checked | Notes`

## Reusable Answers

Columns:

`Canonical Question | Approved Answer | Status | Applicable Lanes | Length / Format | Approved On | Source Applications | Notes`

Allowed statuses are `Proposed`, `Approved`, and `Deprecated`. Only `Approved` answers may be reused without another content-approval round.

## Change Log

Columns:

`Timestamp | Tab | Field / Record | Previous Value | New Value | Reason | Evidence`

Record user corrections and material source conflicts. Do not log secrets or highly sensitive rejected values.

## Extraction pass

1. Identify the exact CV file and modified date.
2. Extract contact details, links, education, experience, research/publications, awards, and activities.
3. Preserve wording and dates; do not fill gaps with assumptions.
4. Add source links and page/section details where available.
5. Show identity/contact candidates and all ambiguous values for confirmation.
6. Ask for selected-lane gaps in one compact batch, then write the user's corrections with `Confirmed by user`.
