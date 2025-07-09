from django.shortcuts import render
import pandas as pd

def generate_anomalies():
    df = pd.read_csv('anomaly_data.csv')
    threshold = df['value'].mean() + 2 * df['value'].std()
    anomalies = df[df['value'] > threshold]
    return anomalies, df

def dashboard(request):
    anomalies, df = generate_anomalies()
    context = {
        'total_records': len(df),
        'anomaly_count': len(anomalies),
        'sample_anomalies': anomalies.head(5).to_dict(orient='records'),
        'file_name': 'anomaly_data.csv',
    }
    return render(request, 'dashboard.html', context)
