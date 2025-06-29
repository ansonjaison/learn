# Github Actions

- Created a github action which responds which we push something into the repo.
- For Github Action I created a holder .github/workflows/ in my repo

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

**Screenshot from actions tab in this repo**

![image](https://github.com/user-attachments/assets/7e27673f-0149-4155-b061-0aebc0504acf)
