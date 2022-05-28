python3 -m build

if  [[ $1 = "--test" ]]; then
    echo "Uploading to test"
    twine upload --repository testpypi dist/*
else
    echo "Uploading to production"
    twine upload dist/*
fi
