load("@rules_python//python:defs.bzl", "py_binary", "py_library")
# I don't have any pip-installed requirements in this example, but if I
# did we'd use this in `deps = [requirement("yaml")]`
# load("@pypi//:requirements.bzl", "requirement")

# A target the represents the entire python package as a whole. It can be
# referenced with `//src/mypackage` because bazel autoexpands this label to
# `//src/mypackage:mypackage`.
# Typically this target isn't use by, say, tests, because doing so would mean
# that bazel can't cache things well. For example, if bar.py changes but foo.py
# doesn't, it still means that this entire target is considered "changed".
py_library(
    name = "mypackage",
    srcs = glob(["**/*.py"]),
    imports = [".."],
)

py_library(
    name = "__init__",
    srcs = ["__init__.py"],
    imports = [".."],  # This causes `src` to get added to sys.path
    # All subpackages need to be able to access this because it's used as
    # a dep for all the other `__init__`s.
    visibility = [
        "//src/mypackage:__subpackages__",
    ],
    deps = [],
)

py_library(
    name = "foo",
    srcs = ["foo.py"],
    visibility = ["//visibility:public"],
    deps = [
        # Technically this ":__init__" isn't needed because there's nothing
        # in the __init__ file right now. However, it's how we get the sys.path
        # set correctly and we might add stuff (like package-level variables) in
        # the future.
        ":__init__",
        "//src/mypackage/subpackage:subfoo",  # relative paths not allowed.
    ],
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
