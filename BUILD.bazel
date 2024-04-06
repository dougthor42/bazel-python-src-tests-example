load("@bazel_gazelle//:def.bzl", "gazelle")
load("@buildifier_prebuilt//:rules.bzl", "buildifier")
load("@pypi//:requirements.bzl", "all_whl_requirements")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_python_gazelle_plugin//manifest:defs.bzl", "gazelle_python_manifest")
load("@rules_python_gazelle_plugin//modules_mapping:def.bzl", "modules_mapping")

# Tell bazel to include some files
filegroup(
    name = "mygroup",
    srcs = [
        "requirements_lock.txt",
    ],
)

######
# Builifier
#
# Buildifier lints and autoformats bazel (Starlark) files. Run using one or both
# of these:
# bazel run //:buildifier.fix
# bazel run //:buildifier.check
######

buildifier(
    name = "buildifier.check",
    exclude_patterns = [
        "./.git/*",
    ],
    lint_mode = "warn",
    mode = "diff",
)

buildifier(
    name = "buildifier.fix",
    exclude_patterns = [
        "./.git/*",
    ],
    lint_mode = "fix",
    mode = "fix",
)

######
# Gazelle
#
# Gazelle is an automatic BUILD(.bazel) file generator. Run via:
# bazel run //:gazelle
######

# Comments that start with "# gazelle:XYZ" are called *directives*. Some directives
# can and should be set here, in the same bazel package (BUILD file) that defines
# gazelle, while other directives (such as "# gazelle:python_root") should be
# defined in a BUILD file specific to that part of the folder tree. See
# src/BUILD for such an example - it's how we define that the "src" dir should
# be the root of python files and thus get added to sys.path.

# This directive tells gazelle that our tests are named "test_foo.py" instead
# of "foo_test.py".
# gazelle:python_test_naming_convention test_$package_name$

# This directive tells gazelle to make a single bazel target per python file.
# The default is to make a single bazel target per python _package_).
# gazelle:python_generation_mode file

# This directive would be used if, for example, we wanted to make pytest_test
# rules instead of py_test rules. However, this project doesn't use `pytest`
# so the directive is inactive (double #).
## gazelle:map_kind py_test pytest_test //tools/bazel:defs.bzl

# This directive tells gazelle to use import `foobar` using the py_library
# target, rather than the py_binary target (`foobar.py` is both a library
# and an executable, so gazelle gets confuzed, saying that multiple targets
# can satisfy the "mypackage.foobar" import).
# This directive can be set multiple times.
# gazelle:resolve py mypackage.foobar //src/mypackage:foobar

# Python's gazelle added support for the default_visibility directive in
# https://github.com/bazelbuild/rules_python/pull/1787. We can use this to make
# all targets visible by all tests.
# gazelle:python_default_visibility //$python_root:__subpackages__,//tests:__subpackages__

###### End Gazelle Directives ######

# This rule will compile the project requirements into a lock file that
# contains versions and hashes. The lock file ends up getting used when
# installing dependencies via pip.
# bazel run //:requirements.update
compile_pip_requirements(
    name = "requirements",
    src = "requirements.in",
    requirements_txt = "requirements_lock.txt",
)

# This rule fetches the metadata for python packages we depend on. That data is
# required for the gazelle_python_manifest rule to update our manifest file.
modules_mapping(
    name = "modules_map",
    wheels = all_whl_requirements,
)

# Gazelle python extension needs a manifest file mapping from
# an import to the installed package that provides it.
# This macro produces two targets:
# bazel run //:gazelle_python_manifest.update
# bazel run //:gazelle_python_manifest.test
gazelle_python_manifest(
    name = "gazelle_python_manifest",
    modules_mapping = ":modules_map",
    # This is what we called our `pip_parse` rule, where third-party
    # python libraries are loaded in BUILD files.
    pip_repository_name = "pypi",
    # This should point to wherever we declare our python dependencies
    # (the same as what we passed to the pip.parse rule in MODULE.bazel)
    # This argument is optional. If provided, the `.test` target is very
    # fast because it just has to check an integrity field. If not provided,
    # the integrity field is not added to the manifest which can help avoid
    # merge conflicts in large repos.
    requirements = "//:requirements_lock.txt",
)

# Make a target for running gazelle.
# bazel run //:gazelle
# or:
# bazel run //:gazelle update  # Note: "update" is the arg, not part of the target
gazelle(
    name = "gazelle",
    gazelle = "@rules_python_gazelle_plugin//python:gazelle_binary",
)
