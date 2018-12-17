
if [[ ! -f env/myenv/bin/activate ]]
then
   mkdir -p env && cd env && python3 -m venv myenv
   cd ..
fi
cd env
source myenv/bin/activate
cd ..

