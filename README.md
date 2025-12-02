# Project assignment for EE4211 (2025-26 Semester A)

## Prerequisites

### Install and enable Git LFS

> [!CAUTION]
> Pull or clone **without Git LFS installed** will cause **files corruptions** if they stores in LFS.

Go to [official Git LFS website](https://git-lfs.com/) to install and follow instructions for
enabling LFS supports.

## Setup

### Create and activate virtual environment

Using virtual environment is preferred that it guarantee all installed packages
are applied with identical versions for specific environment when executing
Python scripts. To create virtual environment, run this command in project root
directory:

```Bash
python -m venv .venv
```

Most IDEs can activate virtual environment automatically once the integrated
terminal is opened. If the virtual environment requires being activated manually,
please type this command below:

* UNIX (includes macOS and Linux):
  ```Bash
  source .venv/bin/activate
  ```
* Windows (Command Prompt)
  ```DOS
  .venv\Scripts\activate.bat
  ```

### Install

After the virtual environment created and activated, you still need to install
dependencies to make Python script run. These dependencies are listed into
`requirements.txt` in project root directory already that all dependencies
will be installed with this command:

```Bash
pip install -r ./requirements.txt
```

> [!CAUTION]
> This approach will install **CPU ONLY** PyTorch for maximize compatability.
> 
> To enable CUDA (nVidia GPU supports in Windows and Linux) or ROCm (AMD GPU supports in Linux)
> acceleration supports, PyTorch **must be** installed with specified index URL at first:
> 
> ```bash
> # Uncomment below if using nVidia GPU
> # TORCH_COMP_PLATFORM=cu130
> 
> # Uncomment below if using AMD GPU
> # TORCH_COMP_PLATFORM=rocm6.4
> 
> pip install torch torchvision --index-url https://download.pytorch.org/whl/${TORCH_COMP_PLATFORM}
> ```
> 
> Then install other fundamentals packages:
> ```bash
> pip install ultralytics notebook ipywidgets numpy pandas
> ```

If any new dependencies installed, which not appeared in `requirements.txt`,
please update it as soon as possible by running this command:

```Bash
pip freeze > requirements.txt
```

For Windows environment, ensure the terminal using UTF-8 encoding before generate `reqeuirements.txt`:

```batch
rem Obtain current active code
chcp

rem Change to UTF-8 encoding
chcp 65001

rem Generate requirements.txt
pip freeze > requirements.txt

rem Revert to original encoding
chcp <original code>
```

Or using Powershell command (preferred):

```powershell
pip freeze | Out-File -Encoding UTF8 .\requirements.txt 
```

### Change directory for Ultralytics

YOLO sets current directory where `yolo` command invoked as default location of
`datasets_dir`, `weights_dir` and `runs_dir`. If you prefer reusing datasets across
multiple directories, please change them by either run these commands:

```Bash
yolo settings datasets_dir="path/to/your/datasets"
yolo settings weights_dir="path/to/your/weights"
yolo settings runs_dir="path/to/your/runs"
```

or edit `~/.config/Ultralytics/settings.json` (`%APPDATA%\Ultralytics\settings.json` for Windows):

```json
{
  "datasets_dir": "path/to/your/datasets",
  "weights_dir": "path/to/your/weights",
  "runs_dir": "path/to/your/runs"
}
```
