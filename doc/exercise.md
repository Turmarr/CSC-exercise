The exercise can be completed by focusing exclusively on one of the following tracks:
- `backend` 
- `frontend`

## Objective

Retrieve a user's starred repositories from GitHub and display them neatly.
The relevant data to be displayed from a user's starred repositories:
- number of starred repositories
- list of repositories, each repository containing information such as: name, description, URL, license (if exists) and topics
   - Omit private repositories from the list of repositories


### Breakdown

1. Create a new [OAuth](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) application in GitHub developer settings. See also the [Authorizing OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps) documentation regarding relevant API calls and parameters. Starring related information can be found from the [GitHub API docs](https://docs.github.com/en/rest/activity/starring?apiVersion=2022-11-28)
2. Create an application that uses OAuth credentials to allow users to sign in with GitHub login
3. Use the token from the authentication to fetch the user's starred repositories
4. Display the starred repositories


### General Requirements

- create a new public GitHub repository to store your submission
- have configuration, running and testing instructions in a `README.md`
- we recommend that the application should have default configurations, only needing OAuth credentials to be added for it to work (don't add secrets to a git repository)
- if you reference other work in your solution, add comments where applicable with the URL sources where you found the information from, e.g. stackoverflow, articles, tutorials
- optionally have a [Dockerfile](https://docs.docker.com/reference/dockerfile/) (the application should be packaged into an container image)

## Tracks

### Backend Track

For a backend focused submission you should create an application that has an API which can be used either from command line, or from a browser. The starred repositories should be parsed to a neat JSON containing only relevant data.


#### Technology Options

The web app can be created either with `python` or `go`:
- **async** python, we require [aiohttp](https://docs.aiohttp.org/en/stable/) or [fastapi](https://fastapi.tiangolo.com/)
- golang, we require [net/http](https://pkg.go.dev/net/http) or [gin](https://gin-gonic.com/)

### Frontend Track

For a frontend focused submission you should create a [SPA](https://developer.mozilla.org/en-US/docs/Glossary/SPA) that has an API and can be viewed from a browser. The starred repositories should be displayed in a table containing only relevant data.

#### Technology Options

We require:
- [Vue 3](https://vuejs.org/)
- [CSC Design System v2](https://www.npmjs.com/package/@cscfi/csc-ui), library [documentation](https://design-system.csc.fi/)


