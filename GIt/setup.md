# Git Installation

You can download Git for free from the following website:

```
https://www.git-scm.com/
```

# Using Git with Command Line

- To start using Git, we are first going to open up our **Command shell**.

- For Windows, you can use **Git bash**, which comes included in Git for Windows. For Mac and Linux you can use the built-in terminal.

- The first thing we need to do, is to check if Git is properly installed:

```git
git -v
```

# Configure Git

- Now let Git know who you are.
- This is important for version control systems, as each Git commit uses this information.

```git
git config --global user.name <yourName>
git config --global user.email <yourEmail>
```

# Check your Configuration

```git
git config --list
```

By running this command you'll be able to see your username and email at the end.
