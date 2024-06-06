from diagrams import Cluster,Diagram
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka
from diagrams.custom import Custom
from urllib.request import urlretrieve
from diagrams.onprem.container import Docker

with Diagram("Dumb Home", direction="TB", show=False):
    metrics = Prometheus("metrics")
    metrics << Grafana("Dashboards")

    fritz_icon = 'https://upload.wikimedia.org/wikipedia/de/thumb/6/68/Fritz%21_Logo.svg/270px-Fritz%21_Logo.svg.png'
    diagrams_url = "https://github.com/mingrammer/diagrams/raw/master/assets/img/diagrams.png"
    diagrams_icon = "270px-Fritz%21_Logo.svg.png"
    urlretrieve(fritz_icon, diagrams_icon)
    diagrams = Custom("Diagrams", diagrams_icon)


    with Cluster("Raspi4"):
        grpcsvc = [
            Docker("grpc1"),
            Server("grpc2"),
            Server("grpc3")]
        

