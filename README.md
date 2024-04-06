# Bazel for Python that uses src and tests dirs

An example of how to configure bazel (via the new bzlmod `MODULE.bazel`) for Python
projects that use a `src` dir and have tests outside of the package in a separate
`tests` dir.


## Key points that make this example interesting:

+ All python code is in a `src` dir, as recommended by the [Python Packaging
  User Guide][packaging_guide].
+ Tests are outside of the package and thus not shipped with distributions.
+ The package must be installed before tests will work.
  + Typically this is done via editable installs `pip install -e .`.


[packaging_guide]: https://packaging.python.org/en/latest/tutorials/packaging-projects/


## Usage

1. Clone the repo.
1. Make a venv and activate it.
1. Install the package `pip install -e .[dev]`
1. Make sure non-bazel basic unit tests work `python -m unittest`.
1. And make sure bazel unit tests work `bazel test //...`.
1. And that bazel run works: `bazel run //src/mypackage:mypackage_bin`.

If I've set up this example correctlly, everything should pass.


### Buildifier

[Buildifier][buildifier] is a linter and autoformatter for [Starlark][starlark],
the language used by Bazel.

Run with one or both of:

```shell
bazel run //:buildifier.fix
bazel run //:buildifier.check
```


[buildifier]: https://github.com/bazelbuild/buildtools/blob/master/buildifier/README.md
[starlark]: https://github.com/bazelbuild/starlark


### Gazelle

[Gazelle][gazelle] is a tool for autogenerating `BUILD(.bazel)` files from source
code.

Run by calling all these, in order:

```shell
# If any python dependencies change:
bazel run //:requirements.update
bazel run //:gazelle_python_manifest.update
# Run gazelle and generate BUILD files and targets:
bazel run //:gazelle
```

[gazelle]: https://github.com/bazelbuild/bazel-gazelle
