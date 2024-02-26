load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "subpackage",
    srcs = glob(["**/*.py"]),
    imports = ["../.."],
)

py_library(
    name = "__init__",
    srcs = ["__init__.py"],
    # Make sure the `src` dir, and all subpackages, are in sys.path.
    imports = ["../.."]
)

py_library(
    name = "subfoo",
    srcs = ["subfoo.py"],
    # only visiable to parent package and to tests
    visibility = [
        "//src/mypackage:__pkg__",
        "//tests/subpackage:__pkg__",
    ],
    deps = [":__init__"],
)
