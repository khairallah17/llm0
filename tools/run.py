from pathlib import Path
from datetime import datetime as dt

from pipelines import data_etl
from pipelines.hello import hello_pipeline

from steps import load_to_db_vector


def main():

    root_dir = Path(__file__).resolve().parent.parent
    pipeline_args = {
        "enable_cache": False
    }
    
    run_args_etl = {}
    pipeline_args["config_path"] = root_dir / "configs" / "digital_data_etl_mohammed.yaml"
    assert pipeline_args["config_path"].exists(), f"Config file not found: {pipeline_args["config_path"]}"
    pipeline_args["run_name"] = f"export_artifact_to_json_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
    data_etl.with_options(**pipeline_args)(**run_args_etl)

if __name__ == "__main__":
    main()