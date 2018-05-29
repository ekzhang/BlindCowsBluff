rm output.txt
rm output.dat
rm output.csv
rm output-labels.csv
pushd base
./bcb-null test.dat 500 2> ../output.txt
popd
./datacollector.o output.txt output.dat 6
python transform.py
