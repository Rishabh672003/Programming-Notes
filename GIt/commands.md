# Contribution - Getting Started

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
git switch -c branch-name
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