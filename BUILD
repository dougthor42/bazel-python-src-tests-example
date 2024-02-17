load("@rules_python//python:defs.bzl", "py_library", "py_test")

# Tell bazel to include some files
filegroup(
    name = "mygroup",
    srcs = [
        "requirements_lock.txt",
    ],
)

py_library(
    name = "mypackage-src",
    srcs = glob(["src/mypackage/**/*.py"]),
    imports = ["src"],
    visibility = ["//visibility:public"],
    deps = [],
)

py_test(
	name = "test_foo",
	srcs = glob(["tests/**/*.py"]),
	deps = [":mypackage-src"],
)
