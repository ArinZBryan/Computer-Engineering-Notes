### 2.2 Software
- `pwsh.exe` (Powershell 7.4.5)
- `python.exe` (Python 3.11.9)
- `notepad.exe` (Notepad as of Win10 22H2)
- `vscode.exe` (Visual Studio Code 1.9.2)
### 2.3 Logic

| Formula                 | Meaning                                                         | `x = 3` | `x = 4` |
| ----------------------- | --------------------------------------------------------------- | ------- | ------- |
| `x == 4`                | `x` and `4` has **equal** values                                | `false` | `true`  |
| `x > 4`                 | `x` is **greater** than `4`                                     | `false` | `false` |
| `x >= 4`                | `x` is **greater than or equal** to `4`                         | `false` | `true`  |
| `x != 4`                | `x` **does not equal** `4`                                      | `true`  | `false` |
| `x > 2` **and** `x < 8` | `x` is **greater** than `2` **and** `x` is **smaller** than `8` | `true`  | `true`  |
| `x > 8` **or** `x < 2`  | `x` is **greater** than `8` **or** `x` is **smaller** than `2`  | `false` | `false` |
### 2.4 Running Python
1. REPL from the terminal
	> run `python` in a shell prompt 
2. Module / Script from the terminal
	> run `python` in a shell prompt with the path to the script as the first argument
3. VSCode Debugger
	> with a python file open in the active panel, press `f5`, or click *Run and Debug* in the relevant panel.
4. VSCode Jupyter Notebook
	> create a new Jupyter Notebook (file with the `.ipynb` extension) in VSCode. Run code by clicking the play button by each code block.
	> Note that this requires the following extension: *Jupyter*
