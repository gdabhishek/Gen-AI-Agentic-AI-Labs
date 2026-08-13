# LangGraph — Latest (Python) Reference Summary

Generated: 2026-08-13 09:10:37 (UTC)

This document summarizes the latest LangGraph (Python) documentation and quickstart information as of the generated timestamp. It collects key requirements, installation instructions, CLI usage, and a minimal Pregel example plus links to the official reference pages.

---

1) Key requirements
- Minimum Python: 3.11 (supported: 3.11–3.13 in CLI config)

2) Installation
- Typical install (verify available on PyPI for the environment before using):

```bash
pip install langgraph
```

- The LangGraph CLI enforces MIN_PYTHON_VERSION = '3.11' in its configuration.

3) CLI quick commands
- Create / initialize a new project using templates (CLI helper):

```bash
langgraph create-new <path> --template <template-name>
# or use the provided helper in some CLI versions:
langgraph up -c langgraph.json
```

- Start the LangGraph environment (docker / local runner) using `up` with options:

```bash
langgraph up -c langgraph.json  
# options include: --docker-compose, --port, --recreate, --pull, --watch, --wait, --verbose
```

- CLI configuration supports specifying python version (3.11/3.12/3.13), dependencies array, pip installer selection (auto/pip/uv), .env file management, and Dockerfile customization.

4) Minimal Pregel example (single-node graph)

```python
from langgraph.channels import EphemeralValue
from langgraph.pregel import Pregel, NodeBuilder

node1 = (
    NodeBuilder().subscribe_only("a")
    .do(lambda x: x + x)
    .write_to("b")
)

app = Pregel(
    nodes={"node1": node1},
    channels={
        "a": EphemeralValue(str),
        "b": EphemeralValue(str),
    },
    input_channels=["a"],
    output_channels=["b"],
)

result = app.invoke({"a": "foo"})
print(result)  # {'b': 'foofoo'}
```

5) Graph invocation with checkpointer / thread id
- When a checkpointer is enabled, provide a thread_id in config when invoking a graph:

```python
config = {"configurable": {"thread_id": "my-thread"}}
graph.invoke(inputs, config)
```

6) Notes about configuration and packaging
- CLI config uses a JSON structure including:
  - dependencies: array of packages to install
  - graphs: mapping of graph IDs to compiled Python definitions
  - python_version: optionally set to 3.11/3.12/3.13
  - pip_installer: auto | pip | uv (auto uses uv for supported images otherwise pip)
- LocalDeps support: real packages (pyproject.toml / setup.py) and faux packages (no packaging files) — faux packages get a minimal generated config so they can be installed by pip. requirements.txt in a local package is respected and installed first.

7) Useful official reference links
- Overview / reference home: https://reference.langchain.com/python/langgraph/overview
- CLI create_new (templates): https://reference.langchain.com/python/langgraph-cli/templates/create_new
- CLI up (start environment): https://reference.langchain.com/python/langgraph-cli/cli/up
- Pregel example: https://reference.langchain.com/python/langgraph/pregel/Pregel
- CLI config / MIN_PYTHON_VERSION: https://reference.langchain.com/python/langgraph-cli/config/MIN_PYTHON_VERSION

8) Suggested next steps for this lab
- Add a README in Lab-11-Langgraph with local setup steps:
  - Create a venv with Python 3.11
  - pip install langgraph (or add to requirements.txt)
  - Run a simple Pregel app (example above)
- Add a small example file (pregel_example.py) and a notebook demonstrating stateful invocation and checkpointer usage.
- Optionally generate a PDF of the LangGraph reference pages and add to the lab folder.

---

Sources
- Official LangGraph Python reference pages (LangChain reference site)

End of document.
