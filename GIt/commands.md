# Contributing to a Repository.

## 1. Fork a GitHub Repository

## 2. Cloning the repo to your device.

- Click on the **<> Code** button on the right side and copy the repo's **HTTPS url** which looks like [https://github.com/username/repo-name.git]()
- Open Git Bash, locate your directory, and clone this repo with the help of this command :

```
git clone https://github.com/username/repo-name.git
```

**You'll be able to see something similar to this:**

```
Cloning into 'repo-name'...
remote: Enumerating objects: 32, done.
remote: Counting objects: 100% (2/2), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 32 (delta 0), reused 0 (delta 0), pack-reused 30
Receiving objects: 100% (32/32), 23.68 KiB | 516.00 KiB/s, done.
Resolving deltas: 100% (7/7), done.
```

**Your Repo is cloned :)**

## 3. Making your personal branch.

**What's branch btw ?**
In Git, a branch is a new/separate version of the main repository.
_Learn more about branch at [Branch](./branch.md)._

To make a branch:

```
git switch -c your-branch-name
```

**This will create a branch and switch to it.**

## 4. Open IDE (VS Code Probably)

**Once your branch is made, open the repo in an IDE.**

Use the below command to directly open the IDE from terminal.

```
code .
```

## 5. Make changes in the repo which you were supposed to.

## 6. Adding changes to stagged area.

- As you are working, you may be **adding**, **editing** and **removing** files.
- But whenever you hit a milestone or finish a part of the work, you should **add** the files to a **Staging Environment.**
  Use the command :

```
git add .
```

**Note: ' . ' stands for All changes**

## 7. Commiting the Changes.

- Since we have finished our work, we are ready move from stage to commit for our repo.

- Adding commits keep track of our progress and changes as we work.

- Git considers each commit change point or "save point". It is a point in the project you can go back to if you find a bug, or want to make a change.

- When we commit, we should always include a message.

```
git commit -m "your message"
```

## 8. Pull changes from main branch.

**Pulling to Keep up-to-date with Changes**

- When working as a team on a project, it is important that everyone stays up to date.

- Any time you start working on a project, you should get the most recent changes to your local copy.

- With Git, you can do that with pull.

```
git pull origin main
```

## 9. Push your changes.

- Now push the branch from our local Git repository, to GitHub, where everyone can see the changes:

```
git push origin your-branch-name
```

- Go to GitHub, and confirm that the repository has a new branch.

## 10. Open a Pull Request

- Click the **Compare & pull request** , you can go through the changes made and new files added.
- If the changes look good, you can go forward, creating a **pull request**.
- A pull request is how you propose changes. You can ask some to review your changes or pull your contribution and merge it into their branch.

**Note: You can merge your pull request yourself if is your own repository.**
