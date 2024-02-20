load("@rules_python//python:defs.bzl", "py_library")
load("@pypi//:requirements.bzl", "requirement")

py_library(
    name = "__init__",
    srcs = ["__init__.py"],
    # By making this depend on the parent package, lines like
    # "from mypackage.subpackage import subfoo" end up working because
    # the parent `src` dir is included in sys.path.
    # The alternative is to
    # imports = ["../.."]
    # but that seems like it might be less maintainable?
    deps = ["//src/mypackage:__init__"],
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
