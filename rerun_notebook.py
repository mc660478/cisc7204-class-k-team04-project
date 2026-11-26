"""Rerun the saved analysis using the Python environment that runs this file."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import os
import re
import sys
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter

folder = Path(__file__).resolve().parent
notebook_path = folder / "cisc7204-Class_K-Team_04_FinalAnalysis.ipynb"
with TemporaryDirectory(prefix="team04-kernel-") as temporary:
    runtime = Path(temporary)
    kernel = runtime / "kernels" / "cisc7204-team04"
    kernel.mkdir(parents=True)
    (kernel / "kernel.json").write_text(json.dumps({
        "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
        "display_name": "CISC7204 project Python", "language": "python"
    }))
    os.environ["JUPYTER_PATH"] = str(runtime)
    os.environ["MPLCONFIGDIR"] = str(runtime / "matplotlib")
    os.environ["IPYTHONDIR"] = str(runtime / "ipython")
    notebook = nbformat.read(notebook_path, as_version=4)
    NotebookClient(notebook, timeout=120, kernel_name="cisc7204-team04",
                   resources={"metadata": {"path": str(folder)}}).execute()
    nbformat.write(notebook, notebook_path)
    html, _ = HTMLExporter(template_name="lab").from_notebook_node(notebook)
    # The notebook has static tables and PNG outputs; no external scripts are needed.
    html = re.sub(r"<script\b[^>]*>[\s\S]*?</script\s*>", "", html, flags=re.IGNORECASE)
    html = html.replace("</head>", "<style>pre{white-space:pre-wrap!important;overflow-wrap:anywhere!important;word-break:break-word!important}.jp-OutputArea-output{max-height:none!important;overflow:visible!important}</style></head>")
    notebook_path.with_suffix(".html").write_text(html)
print("Analysis rerun; notebook, CSV, metrics, figures and offline HTML refreshed.")
