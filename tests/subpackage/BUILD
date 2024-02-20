load("@rules_python//python:defs.bzl", "py_library", "py_test")

py_test(
    name = "test_subfoo",
    srcs = ["test_subfoo.py"],
    deps = [
        "//src/mypackage/subpackage:subfoo",
    ],
)
