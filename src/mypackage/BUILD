load("@rules_python//python:defs.bzl", "py_library", "py_binary")
load("@pypi//:requirements.bzl", "requirement")

py_library(
    name = "__init__",
    srcs = ["__init__.py"],
    imports = [".."],  # This causes `src` to get added to sys.path
    deps = [],
)

py_library(
    name = "foo",
    srcs = ["foo.py"],
    deps = [
        ":__init__",
    ],
    visibility = ["//visibility:public"],
)

py_binary(
    name = "bar_program",
    srcs = ["bar_program.py"],
    deps = [
        ":foo",
    ],
)
