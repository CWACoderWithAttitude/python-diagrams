from diagrams import Diagram
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

graph_attr = {
    "splines": "spline",
}

with Diagram("Dumb Home", direction="TB", show=False): #, graph_attr=graph_attr):
    metrics = Prometheus("metric")
    metrics << Grafana("monitoring")
