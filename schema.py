from typing import Optional

from terminusdb_client.woqlschema import (DocumentTemplate, LexicalKey,
                                          WOQLSchema)

schema = WOQLSchema()


class Drug(DocumentTemplate):
    _schema = schema
    _key = LexicalKey(["name"])
    name: str
    botanital_name: Optional[str]

if __name__ == "__main__":
    from client import client
    schema.commit(client, commit_msg="Add Drug Schema")
