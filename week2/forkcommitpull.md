# Terminal Commands
```
anson@DESKTOP-P49CESA:~$ gh repo fork octocat/Spoon-Knife --clone
✓ Created fork ansonjaison/Spoon-Knife
Cloning into 'Spoon-Knife'...
remote: Enumerating objects: 16, done.
remote: Total 16 (delta 0), reused 0 (delta 0), pack-reused 16 (from 1)
Receiving objects: 100% (16/16), done.
Resolving deltas: 100% (3/3), done.
Updating upstream
From https://github.com/octocat/Spoon-Knife
 * [new branch]      change-the-title -> upstream/change-the-title
 * [new branch]      main             -> upstream/main
 * [new branch]      test-branch      -> upstream/test-branch
✓ Cloned fork
anson@DESKTOP-P49CESA:~$ cd Spoon-Knife/
anson@DESKTOP-P49CESA:~/Spoon-Knife$ nano day8.md
anson@DESKTOP-P49CESA:~/Spoon-Knife$ git add .
anson@DESKTOP-P49CESA:~/Spoon-Knife$ git commit -m "Add day8.md - completed Git fork & PR task"
[main 8529a3b] Add day8.md - completed Git fork & PR task
 1 file changed, 14 insertions(+)
 create mode 100644 day8.md
anson@DESKTOP-P49CESA:~/Spoon-Knife$ git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 573 bytes | 573.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/ansonjaison/Spoon-Knife.git
   d0dd1f6..8529a3b  main -> main
anson@DESKTOP-P49CESA:~/Spoon-Knife$ gh pr create --title "Add day8.md for Git practice" \
  --body "Completed Day 8 Git task by forking Spoon-Knife, editing from WSL CLI, and opening this PR."
? Which should be the base repository (used for e.g. querying issues) for this directory? octocat/Spoon-Knife

Creating pull request for ansonjaison:main into main in octocat/Spoon-Knife

https://github.com/octocat/Spoon-Knife/pull/37046
anson@DESKTOP-P49CESA:~/Spoon-Knife$
