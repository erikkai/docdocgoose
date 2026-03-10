# Doc Doc Goose - Documentation Monitoring and Rot Detection

> **NOTE:** MVP work is still in progress. 

## Try it Out 

If you want to try Doc Doc Goose, a sample repository is available: [docdocgoose_test_repo](https://github.com/erikkai/docdocgoose_test_repo/) 

The sample repository contains setup instructions and example files so you can experiment with Doc Doc Goose without modifying your own project.

## The Problem  

Technical documentation easily becomes inaccurate over time. Commands change, dependencies update, links break, formatting styles evolve, and instructions stop working. As documentation grows, the content can also become disorganized, making it difficult for users to find what they need. 

## The Solution

Doc Doc Goose solves these problems by monitoring documentation and detecting when information may have become outdated or invalid. 

Doc Doc Goose automatically checks whether:
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

## Project Status

This repo contains the CLI MVP (Minimum Viable Product). Doc Doc Goose is currently an early release focused on several core documentation monitoring features. This repository contains the first CLI tool which allows you to: 

* Automatically detect documentation rot at priority-based intervals
* Check for bad links in documentation 
* Run documented commands or code samples inside a selected Docker container to verify they execute successfully
