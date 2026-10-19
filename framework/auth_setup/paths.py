from pathlib import Path

FRAMEWORK_ROOT = Path(__file__).resolve().parents[1]   # framework/
AUTH_DIR = FRAMEWORK_ROOT / ".auth"
GITHUB_STATE = AUTH_DIR / "github_state.json"