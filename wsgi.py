from typing import Dict, Any

from flask_skeleton import create_app, db

app = create_app("dev")
app.app_context().push()


@app.shell_context_processor
def make_shell_context() -> Dict[str, Any]:
    """Make objects available during shell"""

    return {
        "db": db,
    }


if __name__ == "__main__":
    app.run(port=5000)
