load("@buildifier_prebuilt//:rules.bzl", "buildifier")

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
