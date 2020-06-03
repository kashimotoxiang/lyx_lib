rm -rf lyx.egg-info/*
rm -rf dist/*
rm -rf build/*
python setup.py sdist build
twine upload dist/*