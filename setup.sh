git submodule init
git submodule update
for path in voicecloning; do
    cd ${path}
    python3 setup.py develop --user
    cd -
done
./venv_setup.sh

# 2
./download.sh
