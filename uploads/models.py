from __future__ import unicode_literals
from django.db import models
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Milvus


# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def digest(self):
        loader = TextLoader(self.document.path)
        docs = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0)
        docs = text_splitter.split_documents(docs)
        if docs is not None and docs == []:
            embeddings = OpenAIEmbeddings(chunk_size=1)
            vector_db = Milvus.from_documents(
                docs,
                embeddings,
                connection_args={"host": "127.0.0.1", "port": "19530"},
            )
            self.is_processed = True
            self.save()
