load("@rules_python//python:defs.bzl", "py_library")
load("@pypi//:requirements.bzl", "requirement")

py_library(
    name = "__init__",
    srcs = ["__init__.py"],
    deps = [],
)

py_test(
    name = "test_main",
    srcs = ["test_main.py"],
    deps = [
        # To reference something defined in another BUILD file, prefex with
        # "//". Note that the path is relative to the top-level WORKSPACE.
        "//src/myproject:main",
        # Reference to current BUILD file
        ":__init__",
    ],
)
