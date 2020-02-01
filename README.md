# data_wrangling_challenge

requirements.txt contains few packages which can be installed in the virtual environment.

virtualenv -p python3 venv-data-wrangling
source venv-data-wrangling/bin/activate
python data_wrangling_challenge.py

This python script will store updated CSV files in their respective folders. Daily gas price file will be located in daily/data/daily_gas_price.csv.

Each granularity has its own visualization. Once you are in the project root directory, you need to execute:

python -m SimpleHTTPServer 8080

Daily Gas Price d3 graph can be visualized at http://127.0.0.1:8080/daily/line_graph.html
Weekly Gas Price d3 graph can be visualized at http://127.0.0.1:8080/weekly/line_graph.html
Monthly Gas Price d3 graph can be visualized at http://127.0.0.1:8080/monthly/line_graph.html
