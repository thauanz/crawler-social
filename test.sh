echo "Running tests.."
docker run -it -v crawler_files:/tmp/files crawler /bin/bash -c "python -m unittest crawler_test.py"