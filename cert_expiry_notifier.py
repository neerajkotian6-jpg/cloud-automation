import requests
import pandas as pd
from datetime import datetime

class CertExpiryNotifier:
    def __init__(self, metadata_path):
        # Uses Pandas for efficient metadata mapping
        self.customer_df = pd.read_csv(metadata_path)

    def get_metrics(self, api_url, token):
        # Your actual PromQL logic refactored for public display
        query = (
            '((x509_cert_not_after - time()) / 86400) < 14 and '
            '((x509_cert_not_after - time()) / 86400) > 0'
        )
        params = {"query": query}
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(api_url, headers=headers, params=params)
        return response.json()["data"]["result"]

    def notify_stakeholders(self, namespace, days, cn):
        # Matches technical namespace to Account Owner via Pandas
        match = self.customer_df[self.customer_df["Namespace"] == namespace]
        owner = match["Account_Owner"].iloc[0] if not match.empty else "On-Call"
        
        print(f"ALERT: Cert for {cn} in {namespace} expires in {days:.2f} days. Notifying {owner}.")

if __name__ == "__main__":
    notifier = CertExpiryNotifier("dummy_customers.csv")
    # Logic: Fetch metrics -> Map to Owner -> Notify
    # notifier.run(...)
