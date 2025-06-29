# Github Actions

- Created a github action which responds which we push something into the repro.
- For Github Action I created a holder .github/workflows/ in my repro

**Github Action Code**

```
name: Echo Text 
on:
  push:          
    branches:
      - main     
jobs:
  say-hello:
    runs-on: ubuntu-latest 
    
    steps:
      - name: Say Hello
        run: echo "Hello from GitHub Actions!" 

```