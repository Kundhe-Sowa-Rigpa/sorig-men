from terminusdb_client import WOQLClient

team = "10zinten|f7fb"
db = "sorig_medicines"
client = WOQLClient(f"https://cloud.terminusdb.com/{team}/")

client.connect(team=team, use_token=True, db=db)
