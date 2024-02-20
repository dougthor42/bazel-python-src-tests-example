load("@rules_python//python:defs.bzl", "py_library", "py_binary")
# I don't have any pip-installed requirements in this example, but if I
# did we'd use this in `deps = [requirement("yaml")]`
# load("@pypi//:requirements.bzl", "requirement")

py_library(
    name = "__init__",
    srcs = ["__init__.py"],
    imports = [".."],  # This causes `src` to get added to sys.path
    deps = [],
    # All subpackages need to be able to access this because it's used as
    # a dep for all the other `__init__`s.
    visibility = [
        "//src/mypackage:__subpackages__",
    ],
)

py_library(
    name = "foo",
    srcs = ["foo.py"],
    deps = [
        # Technically this ":__init__" isn't needed because there's nothing
        # in the __init__ file right now. However, it's how we get the sys.path
        # set correctly and we might add stuff (like package-level variables) in
        # the future.
        ":__init__",
        "//src/mypackage/subpackage:subfoo",  # relative paths not allowed.
    ],
    visibility = ["//visibility:public"],
)

# An example of a frozen binary.
# Run with `bazel run //src/mypackage:bar_program`
py_binary(
    name = "bar_program",
    srcs = ["bar_program.py"],
    deps = [
        ":foo",
    ],
)
