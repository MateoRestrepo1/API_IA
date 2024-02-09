import os
import pandas as pd
from flask import Flask, request, jsonify



file_path = os.environ.get('FILE_PATH', 'Templates/rates.csv')
columns = os.environ.get('COLUMNS', '').split(',')

def read_csv(file_path, columns):
    df = pd.read_csv(file_path, sep=',')
    df = df[columns]
    return df.to_dict(orient='records')

app = Flask(__name__)

@app.route('/api/v1/rates', methods=['GET'])
def get_rates():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rates.csv')
    columns_str = request.args.get('columns', '')
    columns = columns_str.split(',') if columns_str else None
    data = read_csv(file_path, columns)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
    
    
    
    
    
   