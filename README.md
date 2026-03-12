# Doc Doc Goose - Documentation Monitoring and Rot Detection

> **NOTE:** MVP work is still in progress. 

## Quick Demo 

```bash
$ ddg init 
🪿 DocDocGoose directories are ready!
Link checker successfully installed.

$ ddg scan
🪿 Scanning for documentation health...
doc_samples/doc_1.md    fresh
doc_samples/doc_2.md   due
Scan complete.
Log written to .docdocgoose/logs/scan_log.json
```

Sample output:

```json
[
  {
    "document": "doc_samples/doc_1.md",
    "url": "https://github.com/erikkai/docdocgoose_test_repo/blob/main/doc_samples/doc_1.md",
    "priority": "P1",
    "status": "fresh",
    "last_modified": "2026-03-10T21:34:55Z"
  },
  {
    "document": "doc_samples/doc_2.md",
    "url": "https://github.com/erikkai/docdocgoose_test_repo/blob/main/doc_samples/doc_2.md",
    "priority": "P1",
    "status": "due",
    "last_modified": "2026-02-20T10:12:11Z"
  }
]
```

## Try it Out 

If you want to try Doc Doc Goose, a sample repository is available: [docdocgoose_test_repo](https://github.com/erikkai/docdocgoose_test_repo/) 

The sample repository contains setup instructions and example files so you can experiment with Doc Doc Goose without modifying your own project.

## The Problem  

Technical documentation easily becomes inaccurate over time. Commands change, dependencies update, links break, formatting styles evolve, and instructions stop working. As documentation grows, the content can also become disorganized, making it difficult for users to find what they need. 

## The Solution (Current MVP)

Doc Doc Goose addresses documentation rot by monitoring documentation and detecting when information may have become outdated or invalid.

The current CLI MVP focuses on a few core capabilities: 

* Detect when documentation may be stale based on configurable review priorities
* Check documentation for broken links
* Generate structured scan logs showing which documentation may need review

## The Solution (Planned Capabilities)
Future versions of Doc Doc Goose will expand documentation monitoring to automatically detect additional types of issues.

Doc Doc Goose will check whether:
* Your code samples are still functional
* Installation instructions are still accurate
* Content has been reviewed recently and is due for an update
* Documentation contains broken links 
* Changes to code or systems may have affected your documentation 
* Documentation is properly formatted and follows selected style and grammar rules
* Pages are popular with users or not by combining documentation-specific metrics and options for users to provide feedback per page 

Doc Doc Goose also includes additional capabilities:
* A dashboard for monitoring documentation across multiple repositories
* A tool for creating a style linter using AI
* The ability to add your content to a retrieval-augmented generation (RAG) system that fetches information from your documentation to provide tailored responses to users
