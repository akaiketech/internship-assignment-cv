import pathlib
from importlib import util as import_util

import pytest
from flake8.api import legacy as f8


def compare_results(actual_co_ords):
    co_ords = []

    IM_W, IM_H = 480, 640
    tol_eps = 0.1

    with open("data/ground_truth.csv") as fp:
        for xy in fp.readlines():
            x, y = xy.strip().split(",")
            x, y = int(x), int(y)
            co_ords.append((x, y))

    x_tols, y_tols = [], []
    for ((ax, ay), (cx, cy)) in zip(actual_co_ords, co_ords):
        x_diff = abs(ax - cx)
        y_diff = abs(ay - cy)
        x_tols.append(x_diff / IM_W)
        y_tols.append(y_diff / IM_H)

    return all([
        sum(x_tols) / len(x_tols) < tol_eps,
        sum(y_tols) / len(y_tols) < tol_eps,
    ])


def get_submission_files():
    path = pathlib.Path("submissions")
    py_files = [str(p) for p in path.glob("*.py")]
    return py_files


@pytest.mark.parametrize(
    "submission_file", get_submission_files()
)
def test_submission_dev(submission_file):
    module, _ = submission_file.split(".")
    spec = import_util.spec_from_file_location(module, submission_file)
    submission_module = import_util.module_from_spec(spec)
    spec.loader.exec_module(submission_module)

    submission_function = submission_module.submission
    actual = submission_function("data/img.png")
    assert compare_results(actual)


# def test_code_quality():
#     style_guide = f8.get_style_guide(ignore=[])
#     report = style_guide.check_files(['submission.py'])
