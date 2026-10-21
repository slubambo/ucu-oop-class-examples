# Get the files and run a story

You need **Python 3** and a text editor. We use **VS Code** in class. You do not need to install any Python packages for these examples.

For the group assignment, follow [GROUP_ASSIGNMENT.md](GROUP_ASSIGNMENT.md) first: use the **group fork**, rather than editing or cloning only the lecturer's copy. These download steps are also useful for reading the original examples.

## 1. Download the examples

On the main page of this repository, open **Code**, then choose **Download ZIP**. Find the downloaded ZIP file and extract it. On Windows, use **Extract All**. On a Mac, you can usually double-click the ZIP file to extract it.

If you already use Git, you can download the same files with:

```sh
git clone https://github.com/slubambo/ucu-oop-class-examples.git
```

Choose either ZIP or Git. You do not need to do both.

## 2. Open the folder

Open VS Code. Choose **File → Open Folder** and select the extracted repository folder. In the file list, open `stories`, then open the folder for your chosen story.

Open that story's `README.md` first. Then open `story.py`.

## 3. Run the code

With `story.py` open, use **Run Python File in Terminal** if that option is available in VS Code. This uses the Python extension used in class.

You can also run the code in a terminal. Open **Terminal → New Terminal**. If you opened the whole repository folder in VS Code, run these commands for the lunch story:

**Windows:**

```sh
py -3 stories/01_rolex_rescue/story.py
```

**macOS or Linux:**

```sh
python3 stories/01_rolex_rescue/story.py
```

Some computers use `python` instead. Check that it is Python 3 with `python --version` before using that command.

For another story, replace `01_rolex_rescue` with its folder name. Each story's README gives the exact command.

The program prints the whole story and finishes. You do not need to type answers into the terminal.

## 4. Read what happened

Open `expected_output.txt` in the same story folder. Compare it with your terminal output. It shows the output from the original, unchanged code.

Read `story.py` in order, from Act 1 to Act 5. A line starting with `#` is a comment for the reader. Python does not run that line.

## If something goes wrong

| What you see | What to do |
|---|---|
| `python3` or `py` is not recognised | Try the other Python command above, or ask for help checking your Python installation. Python can be installed from [python.org](https://www.python.org/downloads/). |
| `can't open file` or `No such file or directory` | Check that the terminal is in the repository folder and that the story path matches the command. |
| VS Code asks you to select an interpreter | Choose your installed Python 3 interpreter. |
| The run option is missing | Use the terminal command above. The run option depends on the Python extension. |
| `SyntaxError` or `IndentationError` after an edit | Check the changed lines. Python uses indentation to group code. Re-download the original file if you need a fresh copy. |

`abc` comes with Python. You do not need to run `pip install abc`.
