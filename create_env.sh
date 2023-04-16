# Ensure VENV is installed
sudo apt install python3-venv python3-pip
# Create Python virtual environment
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
echo Virtual Environment Created
python3 -m pip install -r requirements.txt