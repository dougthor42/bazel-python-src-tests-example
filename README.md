# Bazel for Python that uses src and tests dirs

An example of how to configure bazel (via WORKSPACE, not MODULE.bazel for now) for Python
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
2. Install the package `pip install -e .[dev]`
3. Make sure non-bazel basic unit tests work `python -m unittest tests/test_foo.py`.
4. And make sure bazel unit tests work `bazel test //tests:test_foo`.

If I've set up this example correctlly, everything should pass.