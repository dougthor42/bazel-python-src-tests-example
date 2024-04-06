load("@rules_python//python:defs.bzl", "py_library", "py_test")

py_library(
    name = "__init__",
    srcs = ["__init__.py"],
    deps = [],
)

py_test(
    name = "test_foo",
    srcs = ["test_foo.py"],
    deps = [
        # To reference something defined in another BUILD file, prefex with
        # "//". Note that the path is relative to the top-level WORKSPACE.
        "//src/mypackage:foo",
        # Reference to current BUILD file
        ":__init__",
    ],
)

py_test(
    name = "test_foobar",
    srcs = ["test_foobar.py"],
    deps = ["//src/mypackage:foobar"],
)
