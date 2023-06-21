# Git - Basics

- Make a new **Directory** (file).

```
mkdir <folderName>
```

- Make a new **file**

```
touch <fileName>
```

- Current Directory

```
cd .
```

- Go to Previous Directory

```
cd ..
```

- One more directory back

```
cd ../..
```

# Absolute & Relative Path

## 1. Absolute Paths :

- An absolute path provides the complete location of a file or directory from the **root directory** or drive.
- It specifies the entire path hierarchy, starting from the root directory or drive letter, and provides an unambiguous reference to the location.
- Absolute paths are longer and less flexible but ensure a fixed and definite location regardless of the current working directory.

```
C:\Users\User\folder\file.txt
```

this refers to a file named "file.txt" located in the "folder" directory, which is inside the "User" directory, inside the "Users" directory, starting from the "C:" drive in Windows systems.

## 2. Relative Path :

- A relative path specifies the location of a file or directory relative to the current working directory.
- It does not start with the root directory (e.g., C:\ in Windows systems).
- Instead, it starts from the **current directory** and navigates to the **desired location** using relative references such as '..' (parent directory) or directory names.
- Relative paths are shorter and more flexible but depend on the current working directory to determine the absolute location.

```
cd ./folder/file.txt
```

This refers to a file named "file.txt" located in the "folder" directory in the current directory.

```
cd ../parent-folder/file.txt
```

This refers to a file named "file.txt" located in the "parent-folder" directory, which is one level above the current directory.

<hr>

## List the files in our current working directory:

```
ls
```

**Files in your Git repository folder can be in one of 2 states:**

- Tracked - files that Git knows about and are added to the repository.
- Untracked - files that are in your working directory, but not added to the repository.

When you first add files to an empty repository, they are all untracked. To get Git to track them, you need to stage them, or add them to the staging environment.

**We will cover the staging environment in the next chapter.**
