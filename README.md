# Application Agent Kit

Turn one current CV into a private, reusable application system for jobs, degrees, scholarships, fellowships, grants, conferences, workshops, research schools, hackathons, and competitions.

The kit creates the working data in **your Google Drive**, not in GitHub. It keeps a sourced ground-truth database, lane-specific tracker tabs, a separately tailored CV for every relevant opportunity, current materials, exact submitted Q&A archives, and a mandatory human review before any submission.

## Copy this and give it to your AI agent

```text
Set up my private application system using this repository:
https://github.com/Alcray/application-agent-kit

Install or activate all skills from the repository, then run the
application-agent-setup skill from beginning to end.

Requirements:
- Ask my name first.
- Ask which kinds of applications I will make: jobs/internships, degrees,
  scholarships/fellowships, grants, conferences/workshops/research schools,
  hackathons/competitions, or a custom type.
- Use my private Google Drive, Google Docs, and Google Sheets. If those tools
  are not connected with write access, stop and help me connect them.
- Create the private folder structure, System Index, Ground Truth Database,
  and only the tracker tabs needed for my selected application types.
- Ask me to upload my current CV into the created CV folder.
- Keep my general/master CV separate from Application CVs. For every
  application that requests a CV or resume, create a new opportunity-specific
  version without overwriting the master or a previously submitted version.
- Link the exact tailored CV from the tracker and preserve the uploaded version
  with the submitted-application archive.
- Build a materials inventory for my selected application types, tell me what
  useful foundational files are missing, and ask me to upload them into the
  correct private folders. Do not request high-risk identity or financial
  documents during general setup.
- Extract only facts supported by that CV, show me the inferred identity and
  contact fields, explicitly confirm my legal given and family names, ask for
  relevant missing facts, and record provenance for every value.
- Never put my CV, personal facts, Google Drive links, or credentials in the
  cloned repository or any Git commit.
- Do not submit any application during setup.

When setup is complete, give me links to the root folder, System Index,
Ground Truth Database, tracker, and CV folder, plus a short list of anything
still missing.
```

That prompt is the recommended installation path because an agent can adapt it to the available skill installer and connector UI. The repository also follows the standard skill and plugin structure described in the [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).

## What setup creates

```text
Application Agent — Your Name/
├── 00 System/
│   ├── System Index — Your Name
│   ├── Ground Truth Database — Your Name
│   └── Application Tracker — Your Name
├── 01 CVs & Resumes/
│   ├── General/
│   └── Application CVs/
├── 02 Supporting Materials/
├── 03 In Progress/
├── 04 Submitted Applications/
└── 05 Templates/
```

The tracker always has a dashboard and creates only the tabs you select. Each lane includes a `Tailored CV` link. The ground-truth sheet stores each fact with a verification state and source, plus a lane-specific materials inventory. The System Index lets the installed skills discover the right private files without modifying the public skill code.

## Included skills

- `application-agent-setup` — asks the onboarding questions, builds or repairs Drive, reads the chosen CV, verifies gaps, and configures application lanes.
- `tailor-application-cv` — creates and visually verifies a separate truthful CV for one opportunity, records what changed, and never overwrites the master.
- `apply-person` — researches, fills, reviews, archives, and tracks a specific personal application. It always stops for a fresh, application-specific final authorization.
- `check-application-status` — checks email or portals for decisions and required actions, then reconciles evidence with the tracker without replying or accepting anything.

## Requirements

- An AI client that supports agent skills, or an agent capable of reading these `SKILL.md` files.
- Google Drive, Docs, and Sheets access with permission to create private files.
- A controllable browser for application forms. The default configuration uses Chrome when available.
- Email access is optional for setup and application preparation, but required for automated status reconciliation.

## Manual Codex installation

Codex can install skills from another GitHub repository using `$skill-installer`. Ask it:

```text
Use $skill-installer to install these paths from Alcray/application-agent-kit:
- skills/application-agent-setup
- skills/tailor-application-cv
- skills/apply-person
- skills/check-application-status

Then use $application-agent-setup to set up my private application system.
```

The repo is also packaged as a plugin through `.codex-plugin/plugin.json`. Restart Codex if newly installed skills do not appear.

## Privacy and safety model

- Personal records stay in the user's private Drive.
- The repo contains schemas and instructions only.
- CV claims retain source provenance; ambiguous values stay `Candidate` until confirmed.
- Every tailored CV is a separate version tied to one opportunity; the general/master and submitted copies remain unchanged.
- Legal name, citizenship, residence, work authorization, and visa status are never guessed.
- Passwords, one-time codes, CAPTCHA responses, payment data, and government ID numbers are never archived.
- `apply-person` prepares by default and does not submit until the user reviews the exact version and gives a fresh instruction naming that application.
- Submission authorization never includes payment, enrollment, accepting an offer, signing terms, or another binding commitment.

## Typical use

After onboarding:

```text
Use $apply-person to prepare my application for [opportunity URL].
```

To tailor a CV without filling the whole application:

```text
Use $tailor-application-cv to tailor my CV for [opportunity URL].
```

After reviewing the completed browser form and exact snapshot:

```text
Submit [exact application name].
```

To reconcile outcomes:

```text
Use $check-application-status to check my applications and update the tracker.
```

## Development

Run the repository checks:

```bash
python3 scripts/validate_repo.py
```

The four skills are intentionally person-agnostic. Forks should keep private resource IDs and real applicant data out of Git.

## License

MIT. See [LICENSE](LICENSE).
