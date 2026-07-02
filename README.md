# Georgia Election Board Governance Audit

Sanitized case study on researching Georgia county election boards, enabling legislation, outreach, and governance review workflows.

## Overview

This repository presents a sanitized public case study based on my voter-access work with the ACLU of Georgia.

The project focused on researching the legal and operational structure of county boards of elections across all 159 counties in Georgia. The goal was to help identify counties where board-governance documentation was unclear, enabling legislation was difficult to locate, or election-administration practices needed further legal or policy review.

This public version does not include internal ACLU work product, raw county notes, county-specific legal conclusions, private communications, contact details, or unredacted source records.

## Project context

County boards of elections are responsible for critical parts of election administration, but their structure can vary widely across Georgia. Some boards are created by local enabling legislation, while others may operate under different local arrangements or historical practices.

For legal and policy teams, understanding each county’s board structure requires more than a simple web search. It can involve public-records research, direct outreach, follow-up calls, county website review, document tracking, and careful distinction between verified facts and unresolved flags.

## My role

I helped build a statewide research workflow covering all **159 Georgia counties**.

The work included:

- Calling county offices across Georgia
- Sending repeated follow-up emails to county officials
- Searching for county board enabling legislation and governance documents
- Tracking whether documentation was located, unclear, missing, or required follow-up
- Recording outreach status and source availability
- Structuring county-by-county findings for legal and policy review
- Helping identify counties requiring additional review by senior staff

The project required roughly **50 hours** of direct data entry, calling, emailing, source tracking, and follow-up.

## Outreach challenge

A major part of the project was persistence.

County outreach varied widely. Some offices were helpful and responsive, while others were difficult to reach, did not respond to repeated emails, redirected requests, or resisted providing clear documentation.

The work required professional communication, careful note-taking, repeated follow-up, and the ability to stay organized while managing a statewide research process.

## Research workflow

The workflow followed a repeatable process:

```text
County list
    ↓
Public website and document search
    ↓
Phone and email outreach
    ↓
Follow-up tracking
    ↓
Source and document review
    ↓
Structured data entry
    ↓
Flag for legal or policy review
```

## What was tracked

The internal project tracked information such as:

- County name
- Board of elections structure
- Availability of enabling legislation
- Source links or document references
- Outreach attempts
- Response status
- Confidence level
- Follow-up needs
- Potential governance or documentation concerns

This public version uses sanitized examples and a mock data schema only.

## Mock data workflow

This repository includes a small mock data workflow to demonstrate how county-by-county governance research could be structured.

**Mock data:** [`data/sample_county_governance_records.csv`](data/sample_county_governance_records.csv)  
**Summary script:** [`analysis/summarize_governance_flags.py`](analysis/summarize_governance_flags.py)
**Privacy notes:** [`docs/privacy_and_scope_notes.md`](docs/privacy_and_scope_notes.md)

To run the script locally:

```bash
pip install -r requirements.txt
python analysis/summarize_governance_flags.py

