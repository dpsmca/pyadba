import os
import platform
import subprocess
import sys
import textwrap


def dedent_multiline_string(multiline_string):
    lines = multiline_string.splitlines()
    no_first_line = lines[1:]
    first_line = lines[0]
    fixed_content = textwrap.dedent("\n".join(no_first_line))
    fixed_line1 = textwrap.dedent(first_line)
    if not fixed_line1.strip() == "":
        fixed_content = fixed_line1 + "\n" + fixed_content
    return fixed_content


def create_venv():
    venv_dir = os.path.join(os.path.dirname(__file__), 'venv')
    if not os.path.exists(venv_dir):
        # Create virtual environment
        subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])

    # Generate wrapper scripts
    generate_wrapper_scripts(venv_dir)


def generate_wrapper_scripts(venv_dir):
    script_path = os.path.join(os.path.dirname(__file__), 'src', 'pyadba.py')
    args = '"${@}"'  # Pass all arguments

    if platform.system() == 'Windows':
        cmd_content = f"""@echo off
        if not exists "{venv_dir}" goto :venv_err
        "{venv_dir}\\Scripts\\activate.bat"
        python "{script_path}" %*
        "{venv_dir}\\Scripts\\deactivate.bat"
        goto :end
        
        :venv_err
        echo Please run the install script to create the virtual environment before running this script:
        echo python install.py
        exit /b 1

        :end
        """
        trimmed_content = dedent_multiline_string(cmd_content)
        with open('pyadba.cmd', 'w') as f:
            f.write(trimmed_content)
    else:
        sh_content = f"""#!/usr/bin/env bash

        if [[ ! -d "{venv_dir}" ]]; then
          echo "Please run the install script to create the virtual environment before running this script:"
          echo "python install.py"
          exit 1
        fi
        
        # Activate virtual environment
        source "{venv_dir}/bin/activate"
        
        # Add python lib directory to library path, if required
        PYTHON3_CMD1="$(unalias -a; command -v python3)"
        PYTHON3_CMD="$(realpath "${{PYTHON3_CMD1}}")"
        PYTHON3_BINDIR="${{PYTHON3_CMD%/*}}"
        PYTHON3_HOMEDIR="${{PYTHON3_BINDIR%/*}}"
        PYTHON3_VERSION="${{PYTHON3_HOMEDIR##*/}}"
        PYTHON3_LIBDIR="${{PYDIR}}/lib"
        if [[ -n "${{LD_LIBRARY_PATH}}" && ! "${{LD_LIBRARY_PATH}}" =~ ${{PYTHON3_LIBDIR}} ]]; then
            export LD_LIBRARY_PATH="${{PYTHON3_LIBDIR}}:${{LD_LIBRARY_PATH}}"
        else
            export LD_LIBRARY_PATH="${{PYTHON3_LIBDIR}}"
        fi
        
        python "{script_path}" {args}
        deactivate
        """
        trimmed_content = dedent_multiline_string(sh_content)
        with open('pyadba.sh', 'w') as f:
            f.write(trimmed_content)
        os.chmod('pyadba.sh', 0o755)  # Make the script executable


def install_packages():
    venv_dir = os.path.join(os.path.dirname(__file__), 'venv')
    if platform.system() == 'Windows':
        activate_script = os.path.join(venv_dir, 'Scripts', 'activate.bat')
    else:
        activate_script = os.path.join(venv_dir, 'bin', 'activate')
    if os.path.exists(activate_script):
        if platform.system() == 'Windows':
            subprocess.check_call([activate_script])
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        else:
            cmd = f"source {activate_script} && pip install -r requirements.txt".encode()
            print("Attempting to install required packages ...")
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.stdout:
                print("Results:")
                print(result.stdout)


if __name__ == '__main__':
    create_venv()
    install_packages()


