import os
import yaml
import json
import joblib
from ensure import ensure_annotation
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
from src.datascience import logger

@ensure_annotation
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
        reads yaml file and returns ConfigBox

        Args:
            path_to_yaml (Path): path to yaml file

        Raises:
            ValueError: if yaml file doesn't exist
            e: empty file

        Returns:
            ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"yaml file: {path_to_yaml} could not be loaded: {e}")
    except Exception as e:
        raise e

@ensure_annotation
def create_directory(path_to_directories: list, verbose=True) -> None:
    """
        creates list of directory if it doesn't exist

        Args:
            path_to_directories (list): list of directories to create):
            verbose (bool): if True, prints verbose message

        Returns:
            None
    """

    for path in path_to_directories:
        path = Path(path)
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory: {path} successfully")

@ensure_annotation
def save_json(path: Path, data: dict) -> None:
    """
        saves json file
        Args:
            path (Path: path to json file
            data (dict: data to save

        Returns:
            None
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"saved json file: {path} successfully")

@ensure_annotation
def load_json(path: Path) -> ConfigBox:
    """
        loads json file
        Args:
            path (Path: path to json file

        Returns:
            ConfigBox: ConfigBox type
    """
    with open(path,'r') as json_file:
        content = json.load(json_file)
        logger.info(f"loaded json file: {path} successfully")
        return ConfigBox(content)

@ensure_annotation
def save_bin(data: Any,  path: Path) -> None:
    """
        saves binary file
        Args:
            data (Any): data to save
            path (Path) : path to file

        Returns:
            None
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"saved binary file: {path} successfully")

@ensure_annotation
def load_bin(path: Path) -> Any:
    """
        loads binary file
        Args:
            path (Path): path to file:
        Returns:
            Any: Object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"loaded binary file: {path} successfully")
    return data
